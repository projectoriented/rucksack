#!/usr/bin/env python3

from collections import Counter
import pandas as pd
from pybedtools import BedTool
import os
import re
import sys

QUERY_BED = sys.argv[1]
QUERY_FASTA = sys.argv[2]


def read_fasta(path) -> tuple:
    with open(path) as infile:
        content = infile.read()
        seq = content[content.index("\n") + 1:].replace("\n", "")
        contig = content[1:content.index("\n") + 1].replace("\n", "")
        return contig, seq.upper()


def subset_fasta(bed, fasta_path) -> str:
    """
    Get the overlapping regions of interest in the FASTA file.
    :param bed: regions of interest
    :param fasta_path: FASTA file used by variant caller
    :return: A new fasta file
    """
    a = BedTool(bed)
    a = a.sequence(fi=fasta_path)
    return a.seqfn


def get_fasta_dict(fasta: tuple, fpath: str) -> dict:
    contig_name = amend_name(fpath, fasta[0])
    dt = {contig_name: Counter(fasta[1])}
    return dt


def amend_name(abs_path:str, contig: str) -> str:
    base_name = os.path.basename(abs_path)
    if base_name.startswith("assembly"):
        r = abs_path.split("/")
        r.reverse()
        base_name = r[0].replace("assembly", r[1]+"-verkko")
    p = re.compile("(^.+?)\.")
    match = p.search(base_name).group(1)
    return f"{contig}_{match}"


fasta_dict = {}
q_bed = QUERY_BED
if len(sys.argv) > 2:
    for fasta in sys.argv[2:]:
        print(f"Currently processing: {os.path.basename(fasta)}")
        fasta_file = subset_fasta(q_bed, fasta)
        fasta_tuple = read_fasta(fasta_file)
        fasta_dict.update(get_fasta_dict(fasta_tuple, fasta))

df = pd.DataFrame.from_dict(fasta_dict, orient='columns')
df = df.apply(lambda x: round(x/df.sum(axis=0), 2), axis=1)
print(df.to_csv(sep='\t'))

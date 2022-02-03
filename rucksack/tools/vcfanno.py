#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Resources required to run VCFAnno"""

import re

from tomlkit import parse
from typing import List, Optional
from pydantic import BaseModel, validator

from rucksack.utils.path import copy_files, get_cwd, prepend_path


class Annotation(BaseModel):
    file: str
    fields: List[str] = ["GQ"]
    ops: List[str] = ["self"]
    names: List[str] = ["exac"]
    columns: Optional[int] = None
    type: Optional[str] = None

    @validator("file")
    def name_must_contain_ext(cls, v):
        ext_regex = re.compile(r'(\.[a-zA-Z]{2,4})$')
        if not ext_regex.search(v):
            raise ValueError('must contain a valid extension')
        return v


# def stage_files_to_cwd(base_toml: str, resource_dir: str):
#     with open(base_toml) as f:
#         for i, line in enumerate(f):
#             if line.startswith("file"):
#                 reference_file = parse(line)["file"]
#                 absolute_path = prepend_path(reference_file, resource_dir)
#                 copy_files(absolute_path, get_cwd())

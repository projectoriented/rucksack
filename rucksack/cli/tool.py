#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

from tomlkit import parse
from rucksack.utils.path import copy_files, get_cwd, prepend_path, search_tools


@click.group()
def tool():
    """Generate resources needed by a tool + list available tools"""
    pass


@tool.command()
def show():
    """Show available tools"""
    click.echo(search_tools())


@tool.command()
@click.option('--base-toml', nargs=1, required=True, help="Your VCFanno TOML file")
@click.option('--resource-dir', nargs=1, required=True, help="The location of all referenced files")
def vcfanno(base_toml, resource_dir):
    """Stage files"""
    with open(base_toml) as f:
        for i, line in enumerate(f):
            if line.startswith("file"):
                reference_file = parse(line)["file"]
                absolute_path = prepend_path(reference_file, resource_dir)
                copy_files(absolute_path, get_cwd())

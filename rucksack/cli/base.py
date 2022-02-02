#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Command line interface (CLI) for rucksack"""

import logging
import click

from .tool import tool
from rucksack.__version__ import __version__

LOG = logging.getLogger(__name__)


@click.group("rucksack")
@click.version_option(__version__)
def cli_base(**_):
    """Entry point to a rucksack of preprocessing tools"""
    pass


cli_base.add_command(tool)

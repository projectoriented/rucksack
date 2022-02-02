#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import os


@click.group()
def tool():
    """Generate resources needed by a tool + list available tools"""
    pass


@tool.command()
def show():
    """Show available tools"""
    tools_available = os.listdir("rucksack/tools")
    for item in tools_available:
        if not item.startswith("_"):
            click.echo(os.path.splitext(item)[0])


@tool.command()
@click.argument('name', nargs=1)
@click.option('--base-toml', nargs=1, type=click.File(), required=True)
def generate(name):
    """Gather resources for tool"""
    click.echo(name)


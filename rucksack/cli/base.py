"""Command line interface (CLI) for rucksack1"""
import logging
import click

from rucksack import __version__

LOG = logging.getLogger(__name__)


@click.group("rucksack")
@click.version_option(__version__)
@click.pass_context
def base_command(context: click.Context, log_level: str):
    """A rucksack of preprocessing tools"""
    pass

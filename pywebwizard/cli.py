# Entry point for the cli
# pywebwizard/cli.py
import click
from pywebwizard.commands.create import create

@click.group()
def cli():
    pass

cli.add_command(create)
# Add other commands here as needed
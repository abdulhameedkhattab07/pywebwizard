# pywebwizard/commands/create.py
import click
import questionary
# Import the generators for different frameworks
from pywebwizard.generators.flask import flask
from pywebwizard.generators.django import django
from pywebwizard.generators.fastapi import fastapi

@click.command()
@click.argument("framework", required=False)
@click.argument("name", required=False)
def create(framework, name):
    """Create a new web project"""
    
    if not name:
        name = click.prompt("Project name")

    if not framework:
        framework = questionary.select(
            "Select framework",
            choices=["Django", "Flask", "FastAPI"]
        ).ask()

    framework = framework.lower()
    
    # Delegate to the appropriate generator
    if framework == "django":
        django.generate(name)
    elif framework == "flask":
        flask.generate(name)
    elif framework == "fastapi":
        fastapi.generate(name)
    else:
        click.echo("Unsupported framework.")
        click.echo("Please choose from Django, Flask, or FastAPI.")
    click.echo(f"Creating a new {framework.capitalize()} project named '{name}'...")
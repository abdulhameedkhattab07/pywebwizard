# pywebwizard/generators/django.py
import os
import questionary
import click
from pywebwizard.generators.django.web_setup import setup_django_web_project

def generate(name):
    click.echo(f"Setting up Django project: {name}")
    
    # Ask the required questions
    app_type = questionary.select(
        "Type of app:",
        choices=["web", "api"]
    ).ask()
    
    db = questionary.select(
        "Database:",
        choices=["SQLite", "PostgreSQL", "MySQL"]
    ).ask()
    
    auth = questionary.select(
        "Authentication:",
        choices=["session", "jwt", "none"]
    ).ask()

    # For now just simulate steps
    if app_type == "web":
        setup_django_web_project(name, os.getcwd(), db, auth)
    elif app_type == "api":
        click.echo("API setup is not implemented yet.")

# pywebwizard/generators/flask.py
import questionary
import click

def generate(name):
    click.echo(f"Setting up Flask project: {name}")

    app_type = questionary.select(
        "Type of app",
        choices=["web", "api"]
    ).ask()

    db = questionary.select(
        "Database",
        choices=["SQLite", "PostgreSQL", "MySQL"]
    ).ask()

    auth = questionary.select(
        "Authentication",
        choices=["session", "jwt", "none"]
    ).ask()

    # Simulate setup steps
    click.echo("Installing Flask and dependencies...")
    click.echo("Creating folder structure...")
    click.echo("Generating config files...")
    click.echo("✅ Flask project created successfully!")

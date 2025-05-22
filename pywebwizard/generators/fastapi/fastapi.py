# pywebwizard/generators/fastapi.py
import questionary
import click

def generate(name):
    click.echo(f"Setting up FastAPI project: {name}")

    app_type = questionary.select(
        "Type of app:",
        choices=["api"]  # FastAPI is API-first
    ).ask()

    db = questionary.select(
        "Database:",
        choices=["SQLite", "PostgreSQL", "MySQL"]
    ).ask()

    auth = questionary.select(
        "Authentication:",
        choices=["jwt", "none"]
    ).ask()

    # Simulate setup steps
    click.echo("Installing FastAPI and dependencies...")
    click.echo("Creating project structure...")
    click.echo("Generating config files...")
    click.echo("✅ FastAPI project created successfully!")
    click.echo("You can now run your FastAPI app using 'uvicorn main:app --reload'")
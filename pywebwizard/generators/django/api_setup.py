import os
import subprocess
import click

def setup_django_api_project(project_name, base_dir, db_type, auth_type):
    """
    Sets up a Django Rest Framework project with the specified configurations.
    Args:
        project_name (str): The name of the Django project.
        base_dir (str): The base directory where the project will be created.
        db_type (str): The type of database to use (e.g., SQLite, PostgreSQL).
        auth_type (str): The type of authentication to use (e.g., session, JWT).
    """
    project_path = os.path.join(base_dir, project_name)

    try:
        # Step 1: Install Django if not installed
        click.echo("Installing Django...")
        subprocess.run(["pip", "install", "django"], check=True)
        click.echo("Django installed successfully!")
        # Step 1.1: Install Django Rest Framework
        click.echo("Installing Django Rest Framework...")
        subprocess.run(["pip", "install", "djangorestframework"], check=True)
        click.echo("Django Rest Framework installed successfully!")
        # Step 1.2: Install Django CORS Headers
        click.echo("Installing Django CORS Headers...")
        subprocess.run(["pip", "install", "django-cors-headers"], check=True)
        click.echo("Django CORS Headers installed successfully!")
        # Step 1.3: Install Dot Env
        click.echo("Installing Dot Env...")
        subprocess.run(["pip", "install", "dotenv"], check=True)
        click.echo("Dot Env installed successfully!")
        # Step 1.4: Install Django REST Auth
        click.echo("Installing Django REST Auth...")
        subprocess.run(["pip", "install", "djangorestframework-simplejwt"], check=True)
        click.echo("Django REST Auth installed successfully!")
        # Step 1.5: Install Django All Auth
        click.echo("Installing Django All Auth...")
        subprocess.run(["pip", "install", "django-allauth"], check=True)
        click.echo("Django All Auth installed successfully!")
        
        # Step 2: Create Django project
        click.echo(f"Creating Django project at {project_path}...")
        subprocess.run(["django-admin", "startproject", project_name, base_dir], check=True)
        click.echo("Django project created successfully!")
        # Step 3: Navigate into project and create main app
        os.chdir(project_path)
        click.echo("Creating main app...")
        subprocess.run(["python", "manage.py", "startapp", "main"], check=True)
        click.echo("Main app created successfully!")

        # Step 4: Update settings.py
        settings_path = os.path.join(project_path, project_name, "settings.py")
        click.echo("Updating settings.py...")
        update_settings(settings_path, db_type)
        click.echo("settings.py updated successfully!")
        
        # Step 6: Create requirements.txt
        click.echo("Creating requirements.txt...")
        requirements_path = os.path.join(project_path, "requirements.txt")
        with open(requirements_path, "w") as f:
            f.write("Django\n")
            f.write("djangorestframework\n")
            f.write("django-cors-headers\n")
            f.write("dotenv\n")
            f.write("djangorestframework-simplejwt\n")
            f.write("django-allauth\n")
            
        click.echo("requirements.txt created successfully! to actually get all your dependencies, run `pip freeze > requirements.txt`")
        
        # Step 7: Create .gitignore
        click.echo("Creating .gitignore...")
        gitignore_path = os.path.join(project_path, ".gitignore")
        with open(gitignore_path, "w") as f:
            f.write("*.pyc\n")
            f.write("__pycache__/\n")
            f.write("db.sqlite3\n")
            f.write(".env\n")
        click.echo(".gitignore created successfully!")
        
        # Step 8: Initialize git repository
        click.echo("Initializing git repository...")
        subprocess.run(["git", "init"], check=True)
        click.echo("Git repository initialized successfully!")
        
        # Step 9: Create README.md
        click.echo("Creating README.md...")
        readme_path = os.path.join(project_path, "README.md")
        with open(readme_path, "w") as f:
            f.write(f"# {project_name}\n")
            f.write("This is a Django Rest Framework project.\n")
        click.echo("README.md created successfully!")
        
        # Step 10: Create .env file
        click.echo("Creating .env file...")
        env_path = os.path.join(project_path, ".env")
        with open(env_path, "w") as f:
            f.write("DEBUG=True\n")
            f.write("SECRET_KEY='your_secret_key'\n")
            f.write("ALLOWED_HOSTS='localhost,127.0.1'\n")
            f.write("ACCESS_TOKEN_LIFETIME=5\n")
            f.write("REFRESH_TOKEN_LIFETIME=1440\n")
            f.write("ROTATE_REFRESH_TOKENS=False\n")
            f.write("BLACKLIST_AFTER_ROTATION=True\n")
            f.write("ALGORITHM=HS256\n")
            f.write("AUTH_HEADER_TYPES=Bearer\n")
            f.write("USER_ID_FIELD=id\n")
            f.write("USER_ID_CLAIM=user_id\n")
            f.write("TOKEN_TYPE_CLAIM=token_type\n")
            f.write("JTI_CLAIM=jti\n")
            
        click.echo(".env file created successfully!")

        click.echo("✅ Django Rest Framework project setup complete!")

    except Exception as e:
        click.echo(f"❌ Error setting up Django web project: {e}")


def update_settings(settings_path, db_type):
    """Adds common settings for api like templates and static dirs."""
    with open(settings_path, "r") as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        # Load environment variables from .env file
        if line.startswith("from pathlib import Path"):
            new_lines.append("from dotenv import load_dotenv\n")
            new_lines.append("import os\n")
            new_lines.append("load_dotenv()\n")
        
        new_lines.append(line)
        if line.startswith("INSTALLED_APPS = ["):
            new_lines.append("    'main', # Created By pywizard-cli\n")
            new_lines.append("    'rest_framework', # Created By pywizard-cli\n")
            new_lines.append("    'corsheaders', # Created By pywizard-cli\n")
            new_lines.append("    'rest_framework_simplejwt', # Created By pywizard-cli\n")
            new_lines.append("    'allauth', # Created By pywizard-cli\n")
            new_lines.append("    'allauth.account', # Created By pywizard-cli\n")
            new_lines.append("    'allauth.socialaccount', # Created By pywizard-cli\n")
            
        
        if line.startswith("MIDDLEWARE = ["):
            new_lines.append("    'corsheaders.middleware.CorsMiddleware', # Created By pywizard-cli\n")
            new_lines.append("    'django.middleware.common.CommonMiddleware', # Created By pywizard-cli\n")
        
        if line.startswith("ROOT_URLCONF = '"):
            new_lines.append("    'corsheaders.middleware.CorsPostCsrfMiddleware', # Created By pywizard-cli\n")
            
        # Add REST Framework configuration
        new_lines.append("\n")
        new_lines.append("# Django REST Framework Configuration\n")
        new_lines.append("REST_FRAMEWORK = {\n")
        new_lines.append("    'DEFAULT_AUTHENTICATION_CLASSES': [\n")
        new_lines.append("        'rest_framework_simplejwt.authentication.JWTAuthentication',\n")
        new_lines.append("    ],\n")
        new_lines.append("    'DEFAULT_PERMISSION_CLASSES': [\n")
        new_lines.append("        'rest_framework.permissions.IsAuthenticated',\n")
        new_lines.append("    ],\n")
        new_lines.append("}\n")
        
        # Add Simple JWT configuration
        new_lines.append("\n")
        new_lines.append("# Simple JWT Configuration\n")
        new_lines.append("from datetime import timedelta\n")
        new_lines.append("SIMPLE_JWT = {\n")
        new_lines.append("    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),\n")
        new_lines.append("    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),\n")
        new_lines.append("    'ROTATE_REFRESH_TOKENS': False,\n")
        new_lines.append("    'BLACKLIST_AFTER_ROTATION': True,\n")
        new_lines.append("    'ALGORITHM': 'HS256',\n")
        new_lines.append("    'SIGNING_KEY': SECRET_KEY,\n")
        new_lines.append("    'VERIFYING_KEY': None,\n")
        new_lines.append("    'AUTH_HEADER_TYPES': ('Bearer',),\n")
        new_lines.append("    'USER_ID_FIELD': 'id',\n")
        new_lines.append("    'USER_ID_CLAIM': 'user_id',\n")
        new_lines.append("    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),\n")
        new_lines.append("    'TOKEN_TYPE_CLAIM': 'token_type',\n")
        new_lines.append("    'JTI_CLAIM': 'jti',\n")
        new_lines.append("}\n")
        
        if line.startswith("DATABASES = {"):
            new_lines.append("    # Configured by pywizard-cli, modify as youwant{\n")
            if db_type.lower() == "sqlite":
                new_lines.append("    'default': {\n")
                new_lines.append("        'ENGINE': 'django.db.backends.sqlite3',\n")
                new_lines.append("        'NAME': BASE_DIR / 'db.sqlite3',\n")
                new_lines.append("    },\n")
            elif db_type.lower() == "postgresql":
                new_lines.append("    'default': {\n")
                new_lines.append("        'ENGINE': 'django.db.backends.postgresql',\n")
                new_lines.append("        'NAME': 'your_db_name',\n")
                new_lines.append("        'USER': 'your_db_user',\n")
                new_lines.append("        'PASSWORD': 'your_db_password',\n")
                new_lines.append("        'HOST': 'localhost',\n")
                new_lines.append("        'PORT': '5432',\n")
                new_lines.append("    },\n")
            elif db_type.lower() == "mysql":
                new_lines.append("    'default': {\n")
                new_lines.append("        'ENGINE': 'django.db.backends.mysql',\n")
                new_lines.append("        'NAME': 'your_db_name',\n")
                new_lines.append("        'USER': 'your_db_user',\n")
                new_lines.append("        'PASSWORD': 'your_db_password',\n")
                new_lines.append("        'HOST': 'localhost',\n")
                new_lines.append("        'PORT': '3306',\n")
                new_lines.append("    },\n")
            else:
                raise ValueError(f"Unsupported database type: {db_type}")

    # Add static settings at the bottom
    new_lines.append("\n")
    new_lines.append("# Static Config\n")
    new_lines.append("STATIC_URL = '/static/'\n")
    new_lines.append("STATICFILES_DIRS = [BASE_DIR / 'static']\n")

    with open(settings_path, "w") as file:
        file.writelines(new_lines)

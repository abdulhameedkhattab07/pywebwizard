from setuptools import setup, find_packages

#  pip install -e . 
setup(
    name='pywebwizard',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'pywebwizard-cli=pywebwizard.cli:cli'
        ]
    },
    author='Khattab Abdulhameed',
    description='CLI tool to scaffold Flask, Django, and FastAPI projects easily',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
# This setup.py file is used to package the pywebwizard CLI tool.
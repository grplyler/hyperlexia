from setuptools import setup, find_packages

setup(
    name="hyperlexia",
    description="A high-level machine learning text summarization library",
    version="0.1",
    author="Ryan Plyler <grplyler@liberty.edu>",
    packages=find_packages(),
    install_requires=[
        "click",
        "coloredlogs",   
        "Jinja2",
        "numpy",
        "nltk",
        "networkx"

    ],
    entry_points={
        "console_scripts": [
            "lexi = hyperlexia.cli:cli"
        ]
    },
)
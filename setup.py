"""
ARCHITECT-GPT - Intelligent Architecture Assistant
Created by: Levansh Bhan

Setup script for the ARCHITECT-GPT intelligent assistant application.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="architect-gpt",
    version="1.0.0",
    author="Levansh Bhan",
    author_email="levansh.bhan@example.com",
    description="Intelligent Architecture Assistant - A sophisticated AI assistant for IT architects and technical professionals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/levanshbhan/architect-gpt",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "architect-gpt=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.png"],
    },
) 
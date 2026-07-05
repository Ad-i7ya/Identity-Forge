from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="identityforge-cli",
    version="1.0.1",
    author="Ad-i7ya",
    description="Developer-friendly toolkit for generating synthetic identities via CLI, Python, and REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ad-i7ya/Identity-Forge",
    license="MIT",

    packages=find_packages(),

    install_requires=[
        "requests",
        "colorama",
    ],

    entry_points={
        "console_scripts": [
            "identityforge=identityforge.cli:main",
        ],
    },

    python_requires=">=3.7",

    keywords=[
        "identity",
        "identity-generator",
        "synthetic-data",
        "fake-data",
        "testing",
        "mock-data",
        "opsec",
        "privacy",
        "cli",
        "api",
        "python",
    ],

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)

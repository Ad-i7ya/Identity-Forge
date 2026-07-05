from setuptools import setup, find_packages

setup(
    name="identityforge",
    version="1.0.0",
    description="OPSEC-style synthetic identity generator CLI tool",
    author="Ad-i7ya",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "identityforge=identityforge.cli:main"
        ]
    },
    python_requires=">=3.7",
)

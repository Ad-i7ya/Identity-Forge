from setuptools import setup, find_packages

setup(
    name="identityforge",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "identityforge=identityforge.cli:main"
        ]
    },
)

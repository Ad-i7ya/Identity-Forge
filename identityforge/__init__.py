"""
IdentityForge

A developer-friendly toolkit for generating synthetic identities.

CLI:
    identityforge --help

Python:
    from identityforge import generate_identity, get_countries
"""

from .core import generate_identity, get_countries

__version__ = "1.0.0"
__author__ = "Ad-i7ya"

__all__ = [
    "generate_identity",
    "get_countries",
]

"""Sentino API Client: Python package for personality analysis."""

from .client import SentinoClient
from .demo_data import SAMPLE_TEXTS

__version__ = "0.1.0"
__all__ = ["SentinoClient", "SAMPLE_TEXTS"]
"""
arrow_v - High-performance CSF to Parquet conversion library.

This module provides Python bindings for the Rust-based arrow_v tool,
enabling efficient conversion of large Configuration State Function (CSF)
text files to compressed Parquet format.
"""

from io import TextIOBase
from pathlib import Path
from typing import Any, Optional, TextIO, Union

from . import _csfs_loader

__all__ = [
    "__version__",
    "convert_csf_text_to_parquet",
    "read_csf_from_parquet",
    "get_parquet_info",
]

__version__ = "0.1.0"

def convert_csf_text_to_parquet(*args, **kwargs):
    """Fallback function - requires Rust extension to be built."""
    raise ImportError(
        "Rust extension not built. Install with: pip install -e ."
    )

def read_csf_from_parquet(*args, **kwargs):
    """Fallback function - requires Rust extension to be built."""
    raise ImportError(
        "Rust extension not built. Install with: pip install -e ."
    )

def get_parquet_info(*args, **kwargs):
    """Fallback function - requires Rust extension to be built."""
    raise ImportError(
        "Rust extension not built. Install with: pip install -e ."
    )


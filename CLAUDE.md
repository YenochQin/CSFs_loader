# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CSFs_loader is a high-performance mixed Rust-Python library for converting Configuration State Function (CSF) text files to compressed Parquet format. The project uses Rust for performance-critical operations and Python for user interface through PyO3 bindings.

### Core Functionality
- Converts CSF text files (3-line format with header) to Parquet format using Arrow/Parquet libraries
- Provides high-performance batched processing with configurable chunk sizes
- Supports line truncation to handle extremely long CSF entries
- Offers both Rust binary and Python module interfaces

## Build Commands

### Prerequisites
- Rust 1.91+ (toolchain managed through pixi)
- Python 3.10+
- uv package manager (for Python builds)
- pixi (for Rust environment)

### Development Build
```bash
# Install dependencies and pre-commit hooks
make install

# Build development version (no optimization)
make build-dev

# Build production version (optimized)
make build-prod

# Alternative: Direct uv commands
uv run maturin develop --uv          # Development build
uv run maturin develop --release --uv  # Production build
```

### Rust Binary Build
```bash
# Build standalone binary
cargo build --release

# Run standalone binary
cargo run --bin csfs_loader
```

### Testing
```bash
# Run all tests
make test

# Run tests with coverage
make testcov

# Run specific test file
uv run pytest tests/test_specific.py

# Run benchmarks (requires pytest-speed)
uv run pytest -m benchmark
```

### Code Quality
```bash
# Format code (Python + Rust)
make format

# Lint code
make lint

# Type checking (Python)
make typecheck

# Individual linting
make lint-python
make lint-rust
```

## Architecture

### Core Components

**Rust Core (`src/main.rs`)**
- `convert_csf_text_to_parquet()`: Main conversion function that processes CSF text files in configurable chunks
- `read_csf_from_parquet()`: Reads back CSF data from Parquet files with optional limits
- `get_parquet_info()`: Displays Parquet file metadata and schema information
- Processes CSF files with 5-line headers followed by 3-line CSF records

**Python Bindings (`src/lib.rs`)**
- PyO3 wrapper functions providing Python interface to Rust core
- `py_convert_csf_text_to_parquet()`: Python-accessible conversion function
- `py_read_csf_from_parquet()`: Python-accessible read function
- `py_get_parquet_info()`: Python-accessible metadata function

**Python Module (`python/csfs_loader/`)**
- Fallback implementations that raise ImportError if Rust extension not built
- Type hints in `_csfs_loader.pyi` for the actual PyO3 bindings
- Module name `arrow_v` exported to Python

### Data Processing Flow

1. **Input Processing**: Reads CSF text files with 5-line headers
2. **Chunked Processing**: Processes data in configurable chunk sizes (default 30,000 lines)
3. **Schema Definition**: Uses Arrow schema with 3 string columns (line1, line2, line3)
4. **Compression**: Writes Parquet files with GZIP compression (level 4)
5. **Memory Management**: Uses StringBuilder with pre-allocated capacity for efficiency
6. **Error Handling**: Comprehensive error propagation through Result types

### Build System Integration

**Maturin Integration**: Uses maturin for Rust-Python bindings with:
- Extension module compilation
- Python source directory binding
- PyO3 feature flags for extension module generation

**Multi-language Support**:
- Standalone Rust binary for direct usage
- Python wheel for distribution and pip installation
- Static/shared library options in Cargo.toml

## Key Configuration

### Python Package Configuration (pyproject.toml)
- Uses maturin build backend with PyO3 bindings
- Supports Python 3.10-3.14
- Configured for pytest with coverage and benchmarking
- Type checking with mypy, formatting with ruff

### Rust Configuration (Cargo.toml)
- Dependencies: arrow, parquet, pyo3 for bindings
- Optimized release profile with LTO and single codegen unit
- Multiple crate types: cdylib, rlib, staticlib

### Development Environment
- pixi for Rust environment management
- uv for Python package management
- Pre-commit hooks for code quality
- Comprehensive Makefile for common operations

## Important Notes

- The Python module requires the Rust extension to be built (`make build-dev` or `pip install -e .`)
- CSF files must have exactly 5 header lines followed by 3-line CSF records
- Default maximum line length is 256 characters (configurable)
- Headers are extracted to separate `.headers.txt` files
- The project is designed for handling large CSF files efficiently through batched processing
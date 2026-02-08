# Zaptos API Wrapper Tests

This directory contains unit tests for the Zaptos API wrapper.

## Prerequisites

Ensure you have the development dependencies installed. From the repository root, run:

```bash
pip install -e "wrapper[dev]"
```

## Running Tests

To run the full test suite, use `pytest` from the repository root:

```bash
python -m pytest wrapper/tests
```

Or from the `wrapper` directory:

```bash
cd wrapper
python -m pytest tests
```

## Test Structure

- `conftest.py`: Shared fixtures (mock clients, config).
- `test_client.py`: Tests for `ZaptosClient` methods.
- `test_ghl.py`: Tests for `GHLClient`.
- `test_endpoints_*.py`: Tests for CLI command groups.
- `test_cli.py`: Legacy CLI tests.
- `test_config.py`: Configuration tests.

# Bao

A small Python project scaffold.

## Layout

```
Bao/
├── pyproject.toml
├── src/
│   └── bao/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # macOS / Linux

pip install -e .
python -m bao
```

## Test

```bash
pip install pytest
pytest
```

## Usage

```python
from bao import greet

print(greet("world"))   # Hello, world!
```

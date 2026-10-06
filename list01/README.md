# List 1: PyTorch & Training Fundamentals

This folder contains the solution and resources for Exercise List 1.

## Contents
- `list01.ipynb`: Completed Jupyter notebook with code, outputs, plots, and explanations.
- `the-verdict.txt`: Dataset used for Task 2.3 & 2.4 (Edith Wharton, *The Verdict*).
- `requirements.txt`: Minimal dependencies for `pip`.
- `pyproject.toml`: Dependency configuration for `uv`.

## How to Run

### Option 1: Using `uv` (Recommended)
You can launch Jupyter directly without manually configuring a virtual environment:
```bash
uv run --with jupyterlab jupyter lab list01.ipynb
```
Or sync a local virtual environment first:
```bash
uv sync
uv run jupyter lab list01.ipynb
```

### Option 2: Using standard `venv` and `pip`
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install jupyterlab
jupyter lab list01.ipynb
```

### Option 3: VS Code / Cursor / PyCharm
Open the folder in your IDE, open `list01.ipynb`, and select the Python environment as your kernel.

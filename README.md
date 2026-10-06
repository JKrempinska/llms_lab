# Large Language Models — Lab Repository

Repository for the **Large Language Models** lab course at Wrocław University of Science and Technology.

Managed with [**uv**](https://docs.astral.sh/uv/) for high-speed package management and reproducible environments.

---

## 📁 Repository Structure

```text
lab/
├── .python-version              # Python version pinned to 3.12
├── pyproject.toml               # Course-wide project dependencies (torch, numpy, matplotlib, etc.)
├── uv.lock                      # Deterministic lockfile across all packages
├── .venv/                       # Local virtual environment (ignored in git)
├── scripts/
│   └── pack_submission.py       # Helper script to validate & package submissions
│
├── list01/                      # Exercise List 1: PyTorch & Training Fundamentals
│   ├── list01.ipynb             # Main Jupyter notebook with tasks, code, & explanations
│   ├── the-verdict.txt          # Text dataset (Edith Wharton, The Verdict)
│   ├── list01.pdf               # Task sheet
│   ├── materials01.pdf          # Course background materials
│   ├── requirements.txt         # Standalone pip requirements for submission
│   ├── pyproject.toml           # Standalone uv config for submission
│   └── README.md                # Quick execution guide for the professor
│
└── list02/                      # Future exercise lists (follow same structure)
```

---

## 🚀 Getting Started

### 1. Requirements
Ensure `uv` is installed (already installed via Homebrew):
```bash
uv --version
```

### 2. Syncing Environment
To install or synchronize the exact locked dependencies into `.venv`:
```bash
uv sync
```

### 3. Running Jupyter Notebooks

#### In your IDE (VS Code / Antigravity / Cursor / PyCharm)
1. Open `list01/list01.ipynb`.
2. When prompted to select a Python Kernel, choose the workspace environment:
   `./.venv/bin/python` (Python 3.12).
3. Run cells interactively!

#### In Jupyter Lab / Browser via `uv`
```bash
uv run jupyter lab
```
(Opens the Jupyter interface with the repository environment already activated).

---

## 📦 How to Package & Submit an Exercise List

When you complete a list (e.g., `list01.ipynb`):
1. Make sure all notebook cells are **run from top to bottom with outputs saved** (required by course instructions).
2. Write the 2–4 sentence explanations in the designated markdown cells.
3. Run the submission packaging script:
   ```bash
   uv run python scripts/pack_submission.py list01
   ```
4. The script will validate your notebook and generate `list01_submission.zip` containing:
   - `list01.ipynb` (with code, outputs, and explanations)
   - `the-verdict.txt` (and any local list data)
   - `requirements.txt` & `pyproject.toml` (so the professor can run with either `pip` or `uv`)
   - `README.md` (clean instructions for running)

---

## 🛠 Adding Future Packages
If a future lab requires extra libraries (e.g., Hugging Face transformers, datasets, or tiktoken):
```bash
uv add tiktoken transformers datasets
```
`uv` will update `pyproject.toml` and `uv.lock` in milliseconds.

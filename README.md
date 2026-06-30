# Quantum Single Systems

Python + Qiskit workspace for learning and experimenting with single-system quantum vectors and matrices.

## Prerequisites

- Python 3.13 (recommended for this workspace)
- macOS/Linux shell (`zsh` examples below)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Run the Python Script

```bash
source venv/bin/activate
python src/vector_matrices.py
```

## Run the Jupyter Notebook

```bash
source venv/bin/activate
jupyter lab notebooks/vector_matrices.ipynb
```

If you prefer classic notebook UI:

```bash
source venv/bin/activate
jupyter notebook
```

Then open `notebooks/vector_matrices.ipynb` from the browser.

## Project Layout

```text
.
├── notebooks/
│   └── vector_matrices.ipynb      # Interactive notebook (best for LaTeX display)
├── src/
│   ├── __init__.py
│   ├── vector_matrices.py          # Script version
│   ├── quantum_states.py           # Reusable ket/superposition helpers
│   └── quantum_operators.py        # Reusable operator helpers
├── tests/                          # Unit tests
├── requirements.txt                # Runtime dependencies
└── pyproject.toml                  # Project/tool configuration
```

## Notes

- `array_to_latex` output renders best in Jupyter.
- In plain terminal output, LaTeX objects are shown as text representation.

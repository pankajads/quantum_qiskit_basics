# Quantum Single Systems

Python + Qiskit workspace for learning and experimenting with quantum states, operators, circuits, and entanglement.

## Prerequisites

- Python 3.13 (recommended)
- macOS/Linux shell (`zsh` examples below)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Run the Scripts

Every script under `src/` is self-contained and runnable directly:

```bash
source venv/bin/activate

python src/quantum_states.py    # Basis states, superposition, measurement
python src/quantum_operators.py # Gates (X, Z, H), composition, evolve
python src/vector_matrices.py   # Numpy vectors/matrices + Qiskit Statevector/Operator
python src/tensor_product.py    # Tensor products of states and operators
python src/entanglement.py      # Bell-state circuit
python src/circuits.py          # Minimal single-qubit circuit
```

`vector_matrices.py` also saves a histogram and circuit diagram as PNG files in the project root.

## What Each Script Covers

| Script | Topics |
|---|---|
| `quantum_states.py` | `\|0⟩`, `\|1⟩`, normalised `\|+⟩`/`\|−⟩`, orthogonality, probabilities, measurement |
| `quantum_operators.py` | Pauli X/Z, Hadamard, H²=I, operator composition, Qiskit `Operator` unitary check |
| `vector_matrices.py` | Numpy matrix–vector multiply, weighted operator mix, `Statevector`, `Operator`, circuit |
| `tensor_product.py` | Multi-qubit states, `⊗` via Qiskit, gate combinations, W-state, partial measurement |
| `entanglement.py` | Two-qubit Bell state (H + CNOT) |
| `circuits.py` | Single-qubit `QuantumCircuit` skeleton |

## Run the Tests

```bash
source venv/bin/activate
python -m pytest tests/ -v
```

## Project Layout

```text
.
├── src/
│   ├── __init__.py
│   ├── quantum_states.py           # Basis states, superposition, Statevector demo
│   ├── quantum_operators.py        # Gates as matrices, composition, Operator demo
│   ├── vector_matrices.py          # Vectors, matrices, states, operators, circuit
│   ├── tensor_product.py           # Tensor products of states and operators
│   ├── entanglement.py             # Bell-state circuit
│   └── circuits.py                 # Minimal circuit placeholder
├── tests/
│   └── test_vector_matrices.py     # 27 tests: basis states, superposition, operators
├── requirements.txt
└── pyproject.toml
```

## Notes

- `array_to_latex` output renders best in Jupyter; in a plain terminal it prints as LaTeX source.
- Each `src/` file is independent — no cross-file imports — so any script can be studied or run on its own.

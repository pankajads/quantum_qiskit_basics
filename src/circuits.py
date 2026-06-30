"""Quantum circuits.

Converted from notebooks/circuits.ipynb, which was empty. Placeholder
module kept so the conversion is complete; runnable directly:

    python src/circuits.py
"""

from qiskit import QuantumCircuit


def main() -> None:
    circuit = QuantumCircuit(1)
    print("Empty single-qubit circuit:")
    print(circuit.draw(output="text"))


if __name__ == "__main__":
    main()

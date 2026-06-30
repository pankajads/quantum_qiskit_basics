"""Entanglement basics.

Converted from notebooks/entanglement.ipynb. Runnable directly:

    python src/entanglement.py
"""

from qiskit import QuantumCircuit



def main() -> None:
    # Build a 2-qubit Bell state: H on qubit 0, then CNOT entangles 0 -> 1.
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    print("Bell-state circuit:")
    print(circuit.draw(output="text"))




if __name__ == "__main__":
    main()

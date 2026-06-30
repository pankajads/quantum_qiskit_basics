"""Tensor products of quantum states and operators.

Converted from notebooks/tensor_product.ipynb. Runnable directly:

    python src/tensor_product.py
"""

import qiskit
from qiskit.quantum_info import Statevector, Operator
from numpy import sqrt


def main() -> None:
    # Print which Qiskit version is running.
    print("Qiskit version:", qiskit.__version__)

    # Create the basic |0> state (like "off" for one qubit).
    zero = Statevector.from_label("0")
    # Create the basic |1> state (like "on" for one qubit).
    one = Statevector.from_label("1")

    print("\n|0>:")
    print(zero.draw("text"))
    print("\n|1>:")
    print(one.draw("text"))

    # Combine |0> and |1> into a 2-qubit state using tensor product.
    psi = zero.tensor(one)
    print("\n|0> ⊗ |1>:")
    print(psi.draw("text"))

    # Create |+> state (equal mix of |0> and |1>).
    plus = Statevector.from_label("+")
    # Create |-> state (equal mix with minus sign).
    minus = Statevector.from_label("-")

    print("\n|+>:")
    print(plus.draw("text"))
    print("\n|->:")
    print(minus.draw("text"))

    # Create right-circular basis state (often called +i).
    plusi = Statevector.from_label("r")
    # Create left-circular basis state (often called -i).
    minusi = Statevector.from_label("l")

    print("\n|r> (right-circular):")
    print(plusi.draw("text"))
    print("\n|l> (left-circular):")
    print(minusi.draw("text"))

    # Combine |+> with the left-circular state into another 2-qubit state.
    phi = plus.tensor(minusi)
    print("\n|+> ⊗ |l>:")
    print(phi.draw("text"))

    # Build single-qubit gate operators.
    H = Operator.from_label("H")  # Hadamard gate
    Id = Operator.from_label("I")  # Identity gate (does nothing)
    X = Operator.from_label("X")  # Pauli-X gate (bit-flip)

    # Combine gates for two qubits: H on first qubit, I on second qubit.
    print("\nH ⊗ I:")
    print(H.tensor(Id).draw("text"))

    # Apply X gate to |+> (state evolves under the operator), then show result.
    print("\nX|+>:")
    print(plus.evolve(X).draw("text"))

    # A normalized 3-qubit "W-like" state.
    w = Statevector([0, 1, 1, 0, 1, 0, 0, 0] / sqrt(3))
    print("\nw:")
    print(w.draw("text"))

    result, state = w.measure([0])
    print(f"\nMeasured qubit 0: {result}\nState after measurement:")
    print(state.draw("text"))

    result, state = w.measure([0, 1])
    print(f"\nMeasured qubits 0,1: {result}\nState after measurement:")
    print(state.draw("text"))

    # Inspect every valid single-qubit Statevector label.
    valid_labels = ["0", "1", "+", "-", "r", "l"]
    print("\nValid Statevector labels in this Qiskit version:", valid_labels)
    for label in valid_labels:
        state = Statevector.from_label(label)
        print(f"\nLabel '{label}' as text:")
        print(state.draw("text"))


if __name__ == "__main__":
    main()

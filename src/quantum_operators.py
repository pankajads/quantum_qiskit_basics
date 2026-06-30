"""Quantum operators and gates: matrices, composition, and application.

Demonstrates unitary gates as matrices and how they transform quantum states.
Runnable directly:

    python src/quantum_operators.py
"""

import numpy as np
from qiskit.quantum_info import Operator, Statevector


def main() -> None:
    # --- Common single-qubit gates as numpy arrays ---
    I  = np.array([[1.0,  0.0 ], [0.0,  1.0 ]])   # Identity
    X  = np.array([[0.0,  1.0 ], [1.0,  0.0 ]])   # Pauli-X  (bit-flip)
    Z  = np.array([[1.0,  0.0 ], [0.0, -1.0 ]])   # Pauli-Z  (phase-flip)
    H  = np.array([[1.0,  1.0 ], [1.0, -1.0 ]]) / np.sqrt(2)  # Hadamard
    M1 = np.array([[1.0,  1.0 ], [0.0,  0.0 ]])   # Custom non-unitary operator

    print("Identity (I):");       print(I)
    print("\nPauli-X (bit-flip):"); print(X)
    print("\nPauli-Z (phase-flip):"); print(Z)
    print("\nHadamard (H):"); print(H)
    print("\nCustom M1:"); print(M1)

    # --- Applying operators to states ---
    ket0 = np.array([[1.0], [0.0]])
    ket1 = np.array([[0.0], [1.0]])

    print("\n--- Apply X (bit-flip) ---")
    print(f"X|0> = {(X @ ket0).flatten()}  (should be |1>)")
    print(f"X|1> = {(X @ ket1).flatten()}  (should be |0>)")

    print("\n--- Apply H (superposition) ---")
    h_ket0 = H @ ket0
    h_ket1 = H @ ket1
    print(f"H|0> = {h_ket0.flatten()}  (should be |+>)")
    print(f"H|1> = {h_ket1.flatten()}  (should be |->)")

    print("\n--- Apply Z (phase-flip) ---")
    print(f"Z|0> = {(Z @ ket0).flatten()}  (unchanged)")
    print(f"Z|1> = {(Z @ ket1).flatten()}  (sign flipped)")

    # --- Composing operators (matrix multiplication) ---
    print("\n--- Operator composition ---")
    HH = H @ H          # H applied twice should recover identity
    print("H @ H (should equal I):")
    print(np.round(HH, 4))

    ZX = Z @ X          # Z then X
    print("\nZ @ X:")
    print(ZX)

    # --- Weighted combination of two operators ---
    M2 = I
    M_combined = 0.5 * M1 + 0.5 * M2
    print("\nM_combined = 0.5*M1 + 0.5*I:")
    print(M_combined)

    result = M_combined @ M_combined
    print("\nM_combined @ M_combined:")
    print(result)

    # --- Qiskit Operator: unitary check and evolve ---
    print("\n--- Qiskit Operator examples ---")
    op_H = Operator([[1 / np.sqrt(2),  1 / np.sqrt(2)],
                     [1 / np.sqrt(2), -1 / np.sqrt(2)]])
    op_X = Operator([[0, 1], [1, 0]])
    op_Z = Operator([[1, 0], [0, -1]])

    for name, op in [("H", op_H), ("X", op_X), ("Z", op_Z)]:
        print(f"\nOperator {name}  is_unitary={op.is_unitary()}")
        print(op.draw("text"))

    # Apply via Statevector.evolve
    sv = Statevector([1, 0])
    sv_after_H = sv.evolve(op_H)
    sv_after_HX = sv_after_H.evolve(op_X)
    print("\nStart:   |0>")
    print("After H: ", sv_after_H.data.round(4))
    print("After X: ", sv_after_HX.data.round(4))


if __name__ == "__main__":
    main()

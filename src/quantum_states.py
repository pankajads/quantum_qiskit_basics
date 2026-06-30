"""Quantum state vectors: basis states, superposition, and measurement.

Demonstrates the core building blocks of quantum computing with Qiskit.
Runnable directly:

    python src/quantum_states.py
"""

import numpy as np
from qiskit.quantum_info import Statevector


def main() -> None:
    # --- Basis states as numpy column vectors ---
    ket0 = np.array([[1.0], [0.0]])
    ket1 = np.array([[0.0], [1.0]])
    print("Basis state |0>:")
    print(ket0)
    print("\nBasis state |1>:")
    print(ket1)

    # --- Orthogonality: <0|1> = 0 ---
    inner = float((ket0.T @ ket1).item())
    print(f"\n<0|1> (inner product, should be 0): {inner}")

    # --- Equal superposition: (|0> + |1>) / 2 ---
    superposition = ket0 / 2 + ket1 / 2
    print("\nEqual superposition (|0> + |1>) / 2  [unnormalised mix]:")
    print(superposition)

    # --- Proper normalised superposition |+> = (|0> + |1>) / sqrt(2) ---
    plus = (ket0 + ket1) / np.sqrt(2)
    print("\nNormalised |+> = (|0> + |1>) / sqrt(2):")
    print(plus)
    print(f"  norm: {np.linalg.norm(plus):.4f}  (should be 1.0)")

    # --- Normalised |->) = (|0> - |1>) / sqrt(2) ---
    minus = (ket0 - ket1) / np.sqrt(2)
    print("\nNormalised |-> = (|0> - |1>) / sqrt(2):")
    print(minus)

    # --- Qiskit Statevector: richer representation ---
    print("\n--- Qiskit Statevector examples ---")

    sv_0 = Statevector([1, 0])
    sv_1 = Statevector([0, 1])
    sv_plus = Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
    sv_minus = Statevector([1 / np.sqrt(2), -1 / np.sqrt(2)])

    for label, sv in [("0", sv_0), ("1", sv_1), ("+", sv_plus), ("-", sv_minus)]:
        print(f"\n|{label}>  valid={sv.is_valid()}")
        print(sv.draw("text"))

    # --- Probabilities ---
    print("\n--- Probabilities for |+> ---")
    probs = sv_plus.probabilities_dict()
    for outcome, prob in probs.items():
        print(f"  P(|{outcome}>) = {prob:.4f}")

    # --- Complex state and measurement ---
    sv_complex = Statevector([(1 + 2j) / 3, -2 / 3])
    print(f"\nComplex state  valid={sv_complex.is_valid()}:")
    print(sv_complex.draw("text"))

    outcome, post_state = sv_complex.measure()
    print(f"\nMeasured: |{outcome}>")
    print("Post-measurement state:")
    print(post_state.draw("text"))

    # --- Sample 1 000 shots ---
    counts = sv_complex.sample_counts(1000)
    print(f"\nSampled counts (1000 shots): {dict(counts)}")


if __name__ == "__main__":
    main()

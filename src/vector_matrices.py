"""Vectors, matrices, states, operators and simple circuits.

Converted from notebooks/vector_matrices.ipynb. Runnable directly:

    python src/vector_matrices.py

Matplotlib figures are saved as PNG files next to this script instead of
being displayed inline.
"""

from pathlib import Path

import numpy as np
from qiskit.visualization import array_to_latex

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    # Format numpy output to always show a decimal point.
    np.set_printoptions(formatter={"float_kind": lambda x: f"{x:.1f}"})

    # --- Quantum state vectors: |0> and |1> ---
    ket0 = np.array([[1.0], [0.0]])
    ket1 = np.array([[0.0], [1.0]])
    print("ket0 (|0>):")
    print(ket0)
    print("\nket1 (|1>):")
    print(ket1)

    # --- Superposition: (|0> + |1>)/2 ---
    superposition = ket0 / 2 + ket1 / 2
    print("\nSuperposition (|0> + |1>)/2:")
    print(superposition)

    # --- Quantum matrices (operators) ---
    M1 = np.array([[1.0, 1.0], [0.0, 0.0]])   # custom operator
    M2 = np.array([[1.0, 0.0], [0.0, 1.0]])   # identity
    M = 0.5 * M1 + 0.5 * M2
    print("\nM1 (Custom operator):")
    print(M1)
    print("\nM2 (Identity):")
    print(M2)
    print("\nM = (M1 + M2)/2:")
    print(M)

    # --- Matrix-vector multiplication ---
    result1 = M1 @ ket1
    print("\nM1 @ ket1 (Apply M1 to |1>):")
    print(result1)

    # --- Matrix-matrix multiplication ---
    result2 = M1 @ M2
    print("\nM1 @ M2 (Compose operators):")
    print(result2)

    # --- Self-composition: apply M twice ---
    result3 = M @ M
    print("\nM @ M (Apply M twice):")
    print(result3)

    # --- LaTeX representation (printed as LaTeX source) ---
    print("\nM1 @ ket1 in LaTeX:")
    print(array_to_latex(M1 @ ket1).data)
    print("\nM1 @ M2 in LaTeX:")
    print(array_to_latex(M1 @ M2).data)
    print("\nM @ M in LaTeX:")
    print(array_to_latex(M @ M).data)

    # --- Statevectors, measurements and probabilities ---
    from qiskit.quantum_info import Statevector
    from numpy import sqrt

    u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
    v = Statevector([(1 + 2.0j) / 3, -2 / 3])
    w = Statevector([1 / 3, 2 / 3])

    print("\nu is valid statevector:", u.is_valid())
    print("w is valid statevector:", w.is_valid())

    print("\nv:")
    print(v.draw("text"))

    outcome, state = v.measure()
    print(f"\nMeasured: {outcome}\nPost-measurement state:")
    print(state.draw("text"))

    # Sample measurement outcomes and save a histogram.
    from qiskit.visualization import plot_histogram

    statistics = v.sample_counts(1000)
    print("\nSampled counts:", statistics)
    fig = plot_histogram(statistics)
    hist_path = PROJECT_ROOT / "vector_matrices_histogram.png"
    fig.savefig(hist_path)
    print(f"Saved histogram to {hist_path}")

    # --- Operators / unitary gates ---
    from qiskit.quantum_info import Operator

    Y = Operator([[0, -1.0j], [1.0j, 0]])
    H = Operator([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]])
    S = Operator([[1, 0], [0, 1.0j]])
    T = Operator([[1, 0], [0, (1 + 1.0j) / sqrt(2)]])

    print("\nT operator:")
    print(T.draw("text"))

    # Apply a sequence of unitary operations to a state vector via evolve().
    v = Statevector([1, 0])
    v = v.evolve(H)
    v = v.evolve(T)
    v = v.evolve(H)
    v = v.evolve(S)
    v = v.evolve(Y)
    print("\nState after H, T, H, S, Y:")
    print(v.draw("text"))

    # --- Preview of an equivalent quantum circuit ---
    from qiskit import QuantumCircuit

    circuit = QuantumCircuit(1)
    circuit.h(0)
    circuit.t(0)
    circuit.h(0)
    circuit.s(0)
    circuit.y(0)
    print("\nCircuit:")
    print(circuit.draw(output="text"))

    fig = circuit.draw(output="mpl")
    circuit_path = PROJECT_ROOT / "vector_matrices_circuit.png"
    fig.savefig(circuit_path)
    print(f"Saved circuit diagram to {circuit_path}")


if __name__ == "__main__":
    main()

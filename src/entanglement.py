"""Entanglement basics: Bell state and quantum teleportation protocol.

Runnable directly:

    python3 src/entanglement.py
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile  # core Qiskit circuit building blocks
from qiskit_aer import AerSimulator                                               # local quantum circuit simulator
from qiskit.result import marginal_distribution                                   # extract per-qubit measurement results
from qiskit.circuit.library import UGate                                          # general single-qubit rotation gate U(θ,φ,λ)
from math import pi
import random

SHOTS = 1024   # number of simulation shots

# ANSI colour codes — applied to gate tokens in the ASCII circuit text
RESET  = "\033[0m"
GATE_COLORS = {
    "┤ H ├":   "\033[38;5;203m",   # coral      — Hadamard
    "┤ X ├":   "\033[38;5;75m",    # sky blue   — Pauli-X / CNOT target
    "┤ Z ├":   "\033[38;5;114m",   # sage green — Pauli-Z
    "┤M├":     "\033[38;5;228m",   # yellow     — Measure
    "■":       "\033[38;5;80m",    # teal       — CNOT control dot
    "░":       "\033[38;5;183m",   # plum       — Barrier
    "┤ H ├":   "\033[38;5;203m",   # (duplicate key kept for clarity)
    "If":      "\033[38;5;214m",   # amber      — classical if block
    "End":     "\033[38;5;214m",   # amber      — classical if end
}


# One colour per bar, cycling if there are more outcomes than colours
BAR_COLORS = [
    "\033[38;5;75m",   # sky blue
    "\033[38;5;203m",  # coral
    "\033[38;5;114m",  # sage green
    "\033[38;5;228m",  # yellow
    "\033[38;5;80m",   # teal
    "\033[38;5;183m",  # plum
    "\033[38;5;214m",  # amber
]


def draw_histogram(counts: dict, title: str, bar_width: int = 40) -> None:
    """Render measurement counts as a colourful horizontal bar chart."""
    total    = sum(counts.values())
    max_count = max(counts.values())
    label_w  = max(len(k) for k in counts)          # align outcome labels

    print(f"\n\033[1;97m{'═' * 60}\033[0m")
    print(f"\033[1;97m  {title}  (shots={total})\033[0m")
    print(f"\033[1;97m{'═' * 60}\033[0m\n")

    for i, (outcome, count) in enumerate(sorted(counts.items())):
        pct     = count / total * 100
        bar_len = int(count / max_count * bar_width)
        color   = BAR_COLORS[i % len(BAR_COLORS)]
        bar     = "█" * bar_len
        print(f"  {color}|{outcome:<{label_w}}⟩  {bar:<{bar_width}}  {count:5d}  ({pct:5.1f}%){RESET}")

    print()


def colorize(circuit_text: str) -> str:
    """Wrap known gate tokens with ANSI colour codes."""
    for token, color in GATE_COLORS.items():
        circuit_text = circuit_text.replace(token, f"{color}{token}{RESET}")
    return circuit_text


def draw(circuit: QuantumCircuit, title: str) -> None:
    """Print a colourful ASCII circuit to the terminal."""
    print(f"\n\033[1;97m{'═' * 50}\033[0m")         # bold white separator
    print(f"\033[1;97m  {title}\033[0m")             # bold white title
    print(f"\033[1;97m{'═' * 50}\033[0m\n")
    print(colorize(circuit.draw(output="text").__str__()))


def main() -> None:
    # --- Bell state ---
    circuit = QuantumCircuit(2)            # two qubits, both initialised to |0>
    circuit.h(0)                           # Hadamard on qubit 0: superposition (|0> + |1>) / sqrt(2)
    circuit.cx(0, 1)                       # CNOT: entangles qubits into Bell state (|00> + |11>) / sqrt(2)
    draw(circuit, "Bell State Circuit")

    # --- Quantum teleportation protocol ---
    qubit = QuantumRegister(1, 'q')        # qubit whose state Alice wants to teleport to Bob
    ebit0 = QuantumRegister(1, 'A')        # Alice's half of the shared entangled pair
    ebit1 = QuantumRegister(1, 'B')        # Bob's half of the shared entangled pair
    a = ClassicalRegister(1, 'a')          # stores Alice's first measurement result
    b = ClassicalRegister(1, 'b')          # stores Alice's second measurement result

    protocol = QuantumCircuit(qubit, ebit0, ebit1, a, b)  # assemble all registers into one circuit

    # Step 1 — create entangled pair shared between Alice and Bob
    protocol.h(ebit0)                      # Hadamard on Alice's ebit: puts it in superposition
    protocol.cx(ebit0, ebit1)              # CNOT entangles Alice's ebit with Bob's ebit → Bell pair
    protocol.barrier()                     # visual separator: end of entanglement-setup stage

    # Step 2 — Alice's Bell measurement: entangle q with her ebit, then measure both
    protocol.cx(qubit, ebit0)              # CNOT: q as control, Alice's ebit as target (entangles them)
    protocol.h(qubit)                      # Hadamard on q: rotates into measurement basis
    protocol.measure(ebit0, a)             # measure Alice's ebit → classical bit a
    protocol.measure(qubit, b)             # measure q → classical bit b
    protocol.barrier()                     # visual separator: end of measurement stage

    # Step 3 — Bob applies corrections based on Alice's classical bits
    with protocol.if_test((a, 1)):
        protocol.x(ebit1)                  # if a==1, Bob applies X (bit-flip) to his qubit to recover the state
    with protocol.if_test((b, 1)):
        protocol.z(ebit1)                  # if b==1, Bob applies Z (phase-flip) to his qubit to recover the state

    draw(protocol, "Quantum Teleportation Protocol")

    #UGate
    random_gate = UGate(
        theta=random.random() * 2 * pi,
        phi=random.random() * 2 * pi,
        lam=random.random() * 2 * pi,
        )
    
    print(random_gate.to_matrix())

    #create a new testing circuit that first applies our random gate to Q
    #Q, then runs the teleportation circuit, and finally applies the inverse of our random gate to the qubit B and measures.
    test = QuantumCircuit(qubit, ebit0, ebit1, a, b)
    test.append(random_gate, [qubit[0]])
    test.barrier()

    # Append the entire teleportation protocol from above.
    test = test.compose(protocol)
    test.barrier()

    # Finally, apply the inverse of the random unitary to B and measure
    test.append(random_gate.inverse(), ebit1)
    result = ClassicalRegister(1, "Result")
    test.add_register(result)
    test.measure(ebit1, result)
    draw(test, "Teleportation with Random Unitary Gate")

    # Run on AerSimulator and display results as a terminal histogram
    simulator  = AerSimulator()
    compiled   = transpile(test, simulator)               # transpile to simulator's native gate set
    job_result = simulator.run(compiled, shots=SHOTS).result()
    counts     = job_result.get_counts()

    # Extract only the "Result" register (Bob's final qubit) for clarity
    result_only = marginal_distribution(counts, indices=[2])  # index 2 = Result register (added last → leftmost bit)
    draw_histogram(result_only, "Teleportation Result (Bob's qubit)")
    draw_histogram(counts,      "All register outcomes")


if __name__ == "__main__":
    main()                                 # run when the script is executed directly

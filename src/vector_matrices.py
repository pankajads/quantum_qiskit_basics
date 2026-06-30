import numpy as np
from qiskit.visualization import array_to_latex
from IPython.display import display, Latex
from qiskit.quantum_info import Statevector
from numpy import sqrt

# Format numpy output to always show decimal point
np.set_printoptions(formatter={'float_kind': lambda x: f'{x:.1f}'})

#two column vectors
ket0 = np.array([[1.0], [0.0]])
ket1 = np.array([[0.0], [1.0]])

print(ket0)
print(ket1)
print("\n Using column vector array\n")
print(ket0 / 2 + ket1 / 2)


#use array to create matrices
print("\n Using array to create matrices\n")
M1 = np.array([[1.0, 1.0], [0.0, 0.0]])
M2 = np.array([[1.0, 0.0], [0.0, 1.0]])
M = M1 / 2 + M2 / 2
print(M)

print("\n Using matrix multiplication M1 & ket1\n")
print(M1 @ ket1)

print("\n Using matrix multiplication M1 & M2\n")
print(M1 @ M2)

print("\n Using matrix multiplication M & M\n")
print(M @ M)


print("\n Using array_to_latex to display matrices\n")
print("M1 @ ket1 =")
print(array_to_latex(M1 @ ket1).data)
print("\nM1 @ M2 =")
print(array_to_latex(M1 @ M2).data)
print("\nM @ M =")
print(array_to_latex(M @ M).data)


#vector states, measurements, and probabilities



u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
w = Statevector([1 / 3, 2 / 3])

display(u.draw("text"))
display(u.draw("latex"))
print(u.draw("latex_source"))
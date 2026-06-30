"""Tests for the standalone quantum state and operator scripts."""

import numpy as np
import pytest
from qiskit.quantum_info import Statevector, Operator


class TestBasisStates:
    def setup_method(self):
        self.ket0 = np.array([[1.0], [0.0]])
        self.ket1 = np.array([[0.0], [1.0]])

    def test_ket0_shape(self):
        assert self.ket0.shape == (2, 1)

    def test_ket1_shape(self):
        assert self.ket1.shape == (2, 1)

    def test_ket0_values(self):
        np.testing.assert_array_equal(self.ket0, [[1.0], [0.0]])

    def test_ket1_values(self):
        np.testing.assert_array_equal(self.ket1, [[0.0], [1.0]])

    def test_orthogonality(self):
        dot = float((self.ket0.T @ self.ket1).item())
        assert dot == 0.0

    def test_ket0_norm(self):
        assert pytest.approx(np.linalg.norm(self.ket0)) == 1.0

    def test_ket1_norm(self):
        assert pytest.approx(np.linalg.norm(self.ket1)) == 1.0


class TestSuperposition:
    def setup_method(self):
        ket0 = np.array([[1.0], [0.0]])
        ket1 = np.array([[0.0], [1.0]])
        self.plus  = (ket0 + ket1) / np.sqrt(2)
        self.minus = (ket0 - ket1) / np.sqrt(2)
        self.unnorm = ket0 / 2 + ket1 / 2

    def test_plus_is_normalised(self):
        assert pytest.approx(np.linalg.norm(self.plus)) == 1.0

    def test_minus_is_normalised(self):
        assert pytest.approx(np.linalg.norm(self.minus)) == 1.0

    def test_plus_amplitudes(self):
        expected = 1 / np.sqrt(2)
        assert pytest.approx(float(self.plus[0].item()), abs=1e-9) == expected
        assert pytest.approx(float(self.plus[1].item()), abs=1e-9) == expected

    def test_minus_amplitudes(self):
        expected = 1 / np.sqrt(2)
        assert pytest.approx(float(self.minus[0].item()), abs=1e-9) ==  expected
        assert pytest.approx(float(self.minus[1].item()), abs=1e-9) == -expected

    def test_plus_minus_orthogonal(self):
        dot = float((self.plus.T @ self.minus).item())
        assert pytest.approx(dot, abs=1e-9) == 0.0

    def test_unnormalised_values(self):
        np.testing.assert_array_almost_equal(self.unnorm, [[0.5], [0.5]])

    def test_qiskit_statevector_valid(self):
        sv = Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
        assert sv.is_valid()

    def test_qiskit_statevector_probabilities(self):
        sv = Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
        probs = sv.probabilities()
        assert pytest.approx(probs[0]) == 0.5
        assert pytest.approx(probs[1]) == 0.5


class TestOperators:
    def setup_method(self):
        self.I  = np.eye(2)
        self.X  = np.array([[0.0, 1.0], [1.0, 0.0]])
        self.Z  = np.array([[1.0, 0.0], [0.0, -1.0]])
        self.H  = np.array([[1.0, 1.0], [1.0, -1.0]]) / np.sqrt(2)
        self.M1 = np.array([[1.0, 1.0], [0.0, 0.0]])
        self.ket0 = np.array([[1.0], [0.0]])
        self.ket1 = np.array([[0.0], [1.0]])

    def test_x_flips_ket0_to_ket1(self):
        np.testing.assert_array_almost_equal(self.X @ self.ket0, self.ket1)

    def test_x_flips_ket1_to_ket0(self):
        np.testing.assert_array_almost_equal(self.X @ self.ket1, self.ket0)

    def test_h_squared_is_identity(self):
        np.testing.assert_array_almost_equal(self.H @ self.H, self.I)

    def test_h_on_ket0_gives_plus(self):
        plus = np.array([[1.0], [1.0]]) / np.sqrt(2)
        np.testing.assert_array_almost_equal(self.H @ self.ket0, plus)

    def test_z_leaves_ket0_unchanged(self):
        np.testing.assert_array_equal(self.Z @ self.ket0, self.ket0)

    def test_z_negates_ket1(self):
        np.testing.assert_array_equal(self.Z @ self.ket1, -self.ket1)

    def test_identity_preserves_state(self):
        np.testing.assert_array_equal(self.I @ self.ket1, self.ket1)

    def test_compose_m1_with_identity(self):
        np.testing.assert_array_equal(self.M1 @ self.I, self.M1)

    def test_combine_operators_half_half(self):
        M = 0.5 * self.M1 + 0.5 * self.I
        expected = np.array([[1.0, 0.5], [0.0, 0.5]])
        np.testing.assert_array_almost_equal(M, expected)

    def test_apply_m1_to_ket1(self):
        result = self.M1 @ self.ket1
        np.testing.assert_array_equal(result, [[1.0], [0.0]])

    def test_qiskit_operator_unitary(self):
        op = Operator([[1 / np.sqrt(2), 1 / np.sqrt(2)],
                       [1 / np.sqrt(2), -1 / np.sqrt(2)]])
        assert op.is_unitary()

    def test_qiskit_evolve(self):
        sv = Statevector([1, 0])
        op_X = Operator([[0, 1], [1, 0]])
        evolved = sv.evolve(op_X)
        np.testing.assert_array_almost_equal(evolved.data, [0, 1])

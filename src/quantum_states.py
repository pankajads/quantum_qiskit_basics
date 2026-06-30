"""Quantum state vector definitions and utilities."""

import numpy as np


def create_ket0():
    """Create basis state |0⟩.
    
    Returns:
        np.ndarray: Column vector representing |0⟩ = [[1.0], [0.0]]
    """
    return np.array([[1.0], [0.0]])


def create_ket1():
    """Create basis state |1⟩.
    
    Returns:
        np.ndarray: Column vector representing |1⟩ = [[0.0], [1.0]]
    """
    return np.array([[0.0], [1.0]])


def create_superposition(ket0, ket1):
    """Create equal superposition of two states.
    
    Args:
        ket0 (np.ndarray): First quantum state
        ket1 (np.ndarray): Second quantum state
        
    Returns:
        np.ndarray: Superposition (ket0 + ket1) / 2
    """
    return ket0 / 2 + ket1 / 2


def format_output():
    """Set NumPy print options to display floats with decimal point."""
    np.set_printoptions(formatter={'float_kind': lambda x: f'{x:.1f}'})

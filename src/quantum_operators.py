"""Quantum operators and gate definitions."""

import numpy as np


def create_identity_matrix():
    """Create 2x2 identity matrix (I gate).
    
    Returns:
        np.ndarray: Identity matrix [[1.0, 0.0], [0.0, 1.0]]
    """
    return np.array([[1.0, 0.0], [0.0, 1.0]])


def create_custom_operator():
    """Create a custom 2x2 operator.
    
    Returns:
        np.ndarray: Custom operator [[1.0, 1.0], [0.0, 0.0]]
    """
    return np.array([[1.0, 1.0], [0.0, 0.0]])


def compose_operators(op1, op2):
    """Compose two operators using matrix multiplication.
    
    Args:
        op1 (np.ndarray): First operator
        op2 (np.ndarray): Second operator
        
    Returns:
        np.ndarray: Composed operator (op1 @ op2)
    """
    return op1 @ op2


def apply_operator(operator, state):
    """Apply a quantum operator to a quantum state.
    
    Args:
        operator (np.ndarray): Quantum operator (matrix)
        state (np.ndarray): Quantum state (vector)
        
    Returns:
        np.ndarray: Resulting quantum state
    """
    return operator @ state


def combine_operators(op1, op2, weight1=0.5, weight2=0.5):
    """Create a weighted combination of two operators.
    
    Args:
        op1 (np.ndarray): First operator
        op2 (np.ndarray): Second operator
        weight1 (float): Weight for first operator (default 0.5)
        weight2 (float): Weight for second operator (default 0.5)
        
    Returns:
        np.ndarray: Combined operator
    """
    return weight1 * op1 + weight2 * op2

"""
constants.py - This module defines constants.
"""

import jax
import jax.numpy as jnp

### CONSTANTS ###

SIGMA_X = jnp.array(((0, 1), (1, 0)),dtype=jnp.complex64)
SIGMA_Y = jnp.array(((0, -1j), (1j, 0)),dtype=jnp.complex64)
SIGMA_Z = jnp.array(((1, 0), (0, -1)),dtype=jnp.complex64)
SIGMA_PLUS = jnp.array(((0, 2), (0, 0)),dtype=jnp.complex64) # SIGMA_X + i * SIGMA_Y
SIGMA_MINUS = jnp.array(((0, 0), (2, 0)),dtype=jnp.complex64) # SIGMA_X - i * SIGMA_Y


### GENERATIVE CONSTANTS ###

def get_creation_operator(size):
    """
    Construct the creation operator with the given matrix size.

    Arguments:
    size :: int - This is the size to truncate the operator at. This
        value should be g.t.e. 1.

    Returns:
    creation_operator :: ndarray (size, size)
        - The creation operator at level `size`.
    """
    return jnp.diag(jnp.sqrt(jnp.arange(1, size)), k=-1)


def get_annihilation_operator(size):
    """
    Construct the annihilation operator with the given matrix size.

    Arguments:
    size :: int - This is hte size to truncate the operator at. This value
        should be g.t.e. 1.

    Returns:
    annihilation_operator :: ndarray (size, size)
        - The annihilation operator at level `size`.
    """
    return jnp.diag(jnp.sqrt(jnp.arange(1, size)), k=1)


def get_eij(i, j, size):
    """
    Construct the square matrix of `size`
    where all entries are zero
    except for the element at row i column j which is one.

    Arguments:
    i :: int - the row of the unit element
    j :: int - the column of the unit element
    size :: int - the size of the matrix

    Returns:
    eij :: ndarray (size, size)
        - The requested Eij matrix.
    """
    eij = jnp.zeros((size, size),dtype=jnp.complex64)
    eij[i, j] = 1
    return eij

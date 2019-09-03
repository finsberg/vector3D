"""
This module contains the Vector3D class to be used
for illustrating how to document and test a project.

A good example of the NumPy style can be found here:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

"""
import numpy as np


class Vector3D:
    """
    A class for creating 3D vectors.

    Arguments
    ---------
    x : float
        x - coordinate
    y : float
        y - coordinate
    z : float
        z - coordinate

    Example
    -------
    .. code::

        >>> u = Vector3D(1, 1, 1)
        >>> v = Vector3D(1, 2, 3)
        >>> w = u + v
        >>> print(w)
        (2, 3, 4)

    """

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x:g}, {self.y:g}, {self.z:g})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        msg = f"Cannot add Vector3D with {type(other)}"
        # assert isinstance(other, Vector3D), msg
        if not isinstance(other, Vector3D):
            raise TypeError(msg)
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Vector3D(x, y, z)

    def __eq__(self, other):
        msg = f"Cannot compare Vector3D with {type(other)}"
        if not isinstance(other, Vector3D):
            raise TypeError(msg)

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __sub__(self, other):
        msg = f"Cannot subtract Vector3D with {type(other)}"
        # assert isinstance(other, Vector3D), msg
        if not isinstance(other, Vector3D):
            raise TypeError(msg)
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vector3D(x, y, z)

    def dot(self, other):
        r"""Compute the dot product.

        .. math::

            u \cdot v = u_1v_1 + u_2v_2 + u_3v_3

        Arguments
        ---------
        other : Vector3D
            Vector that you want to dot.

        Returns
        -------
        float
            The dot product
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        r"""Compute the cross product.

        .. math::

            w = u \times v

        with

        .. math::

            w_1 &= u_2 v_3 -  u_3 v_2 \\
            w_2 &= u_1 v_3 -  u_3 v_1 \\
            w_3 &= u_1 v_2 -  u_2 v_1


        Arguments
        ---------
        other : Vector3D
            Vector that you want to dot

        Returns
        -------
        float
            The dot product
        """
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)

    def __mul__(self, other):
        """Interpret u*v to be the dot product"""
        if isinstance(other, Vector3D):
            return self.dot(other)
        elif isinstance(other, (int, float)):
            # Alternative use `np.isscalar`
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError(f"cannot multiply vector and {type(other)}")

    def __matmul__(self, other):
        """Interpret u@v as cross product"""
        return self.cross(other)

    def perpendicular(self, other):
        """
        Check if a vector is perpendicular

        Arguments
        ---------
        other : Vector3D
            The vector that you want to check is perpendicular.

        Returns
        -------
        bool
            True if they are perpendicular, and False otherwise.
        """
        return abs(self * other) < 1e-9

    def __rmul__(self, other):
        return self * other

    @property
    def length(self):
        """
        Get length of vector (2-norm)
        """
        return np.sqrt(self * self)

    @length.setter
    def length(self, new_length):
        """
        Set length of the vector.

        Raises
        ------
        ValueError
            If you try to set length equal a non-positive value.
        """
        if new_length < 1e-12:
            msg = "Cannot set length equal to zero or a negative value"
            raise ValueError(msg)
        scale = new_length / self.length
        self.x *= scale
        self.y *= scale
        self.z *= scale

    def unit(self):
        """
        Return a vector in pointing in the same direction
        of unit length.
        """
        new_vector = Vector3D(self.x, self.y, self.z)
        new_vector.length = 1
        return new_vector

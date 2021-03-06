class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d


    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):         # relies on __len__  method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        """Return difference of two vectors."""
        if len(self) != len(other):         # relies on __len__  method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>' # adapt list representation

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    # # Standard __mul__ function
    # def __mul__(self, multiplier):
    #     result = Vector(len(self))
    #     for j in range(len(self)):
    #         result[j] = self[j] * multiplier
    #     return result

    # dot product __mul__ function
    def __mul__(self, other):
        dot_product = [self[j] * other[j] for j in range(len(self))]
        return sum(dot_product)

    def __rmul__(self, multiplier):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = multiplier * self[j]
        return result


if __name__  == '__main__':
    v1 = Vector(5)
    v2 = Vector(5)

    v1[0] = 1
    v1[1] = 2
    v1[2] = 3
    v1[3] = 4
    v1[4] = 5
    v2[0] = 6
    v2[1] = 7
    v2[2] = 8
    v2[3] = 9
    v2[4] = 10

    print('v1 =',v1)
    print('v2 =',v2)

    print('Dot Product of v1 and v2 = ', v1 * v2)

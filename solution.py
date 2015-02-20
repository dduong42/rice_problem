RICE = [
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [3, 0, 0, 0],
]


class Matrix:
    def __init__(self, nb_rows, nb_columns):
        self.nb_rows = nb_rows
        self.nb_columns = nb_columns
        self._matrix = [[0 for j in range(nb_columns)] for i in range(nb_rows)]

    @classmethod
    def from_list(cls, matrix_list):
        """
        Return a Matrix for a list of lists.

        """
        nb_rows = len(matrix_list)

        try:
            nb_columns = len(matrix_list[0])
        except IndexError:
            raise ValueError('The list given should not be empty')

        matrix = cls(nb_rows, nb_columns)
        for i in range(nb_rows):
            for j in range(nb_columns):
                matrix[i, j] = matrix_list[i][j]
        return matrix

    def get(self, i, j, default=None):
        """
        Return self[i, j] or `default` if the coordinates are not valid.

        """
        try:
            return self[i, j]
        except IndexError:
            return default

    def __getitem__(self, coordinates):
        i, j = coordinates

        if i < 0 or j < 0:
            raise IndexError

        return self._matrix[i][j]

    def __setitem__(self, coordinates, value):
        i, j = coordinates
        self._matrix[i][j] = value

    def __repr__(self):
        rows = (' '.join(str(self[i, j]) for j in range(self.nb_columns))
                for i in range(self.nb_rows))
        return '\n'.join(rows)


def coordinates_iterator(nb_rows, nb_columns):
    """
    Yield coordinates to partially iterate over a matrix.
    The (0, n) and (n, 0) coordinates are not yield

    """
    for i in range(1, nb_rows):
        for j in range(1, nb_columns):
            yield (i, j)


def generate_helper_matrix(rice_matrix):
    """
    Generate a matrix `matrix` that has this feature:
    M[i, j] is equal to the quantity of rice obtained when visiting the
    (i, j) square when using the most optimal path.

    """
    nb_rows = rice_matrix.nb_rows
    nb_columns = rice_matrix.nb_columns

    matrix = Matrix(nb_rows, nb_columns)

    matrix[0, 0] = rice_matrix[0, 0]

    # There is only one way to go to the squares that are on the edges.
    # Only go down, or only go to the right.
    for i in range(1, nb_rows):
        matrix[i, 0] = rice_matrix[i, 0] + matrix[i - 1, 0]

    for j in range(1, nb_columns):
        matrix[0, j] = rice_matrix[0, j] + matrix[0, j - 1]

    for i, j in coordinates_iterator(nb_rows, nb_columns):
        # Take the quantity of rice that is maximal between the two paths
        max_rice = max(matrix[i - 1, j], matrix[i, j - 1])
        matrix[i, j] = rice_matrix[i, j] + max_rice

    return matrix


def get_path(helper_matrix):
    """
    Return one path that gives you the most quantity of rice.

    The idea is to start from the destination and to go to the start

    """
    nb_rows = helper_matrix.nb_rows
    nb_columns = helper_matrix.nb_columns

    i, j = nb_rows - 1, nb_columns -1
    path = []
    while (i, j) != (0, 0):
        path.append((i, j))
        if (helper_matrix.get(i - 1, j, default=-1)
                >= helper_matrix.get(i, j - 1, default=-1)):
            i -= 1
        else:
            j -= 1

    return list(reversed(path))


def solve(rice_matrix):
    """
    Print the path that gives you the most quantity of rice and the quantity
    of rice received.

    """
    helper_matrix = generate_helper_matrix(rice_matrix)
    nb_rows = helper_matrix.nb_rows
    nb_columns = helper_matrix.nb_columns

    print('Path:', get_path(helper_matrix))
    print('Quantity:', helper_matrix[nb_rows - 1, nb_columns - 1])

if __name__ == '__main__':
    _rice_matrix = Matrix.from_list(RICE)
    solve(_rice_matrix)

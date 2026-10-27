"""Program 39: Transpose a matrix."""

def transpose_matrix(matrix):
    if not matrix:
        return []

    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Transposed matrix:")
    for row in transpose_matrix(matrix):
        print(row)
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    res = []

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * scalar)
        res.append(new_row)

    return res
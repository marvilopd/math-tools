import re
import numpy as np


def main():
    greeting()
    a = read_matrix("A")
    b = read_matrix("B")
    if a.shape[1] != b.shape[0]:
        print(f"Cannot multiply A({a.shape[0]}x{a.shape[1]}) by B({b.shape[0]}x{b.shape[1]}).")
        return
    result = a @ b
    print("\nMatrix A:")
    print(a)
    print("\nMatrix B:")
    print(b)
    print("\nA x B =")
    print(result)


def greeting():
    print("Hello! This program calculates matrix multiplication.")


def read_matrix(name: str) -> np.ndarray:
    """Read a matrix from the user.

    Prompts the user for the number of rows and columns, then reads each
    row as a line of values separated by spaces or commas. Returns a NumPy
    array of floats.
    """
    while True:
        try:
            print(f"\nEnter matrix {name}:")
            rows = int(input(f"Number of rows for {name}: ").strip())
            cols = int(input(f"Number of columns for {name}: ").strip())
            if rows <= 0 or cols <= 0:
                raise ValueError("Rows and columns must be positive integers.")

            print(
                "Enter each row on a separate line, using spaces or commas between values.\n"
                "You can also paste the whole matrix row-by-row."
            )
            matrix = []
            for i in range(rows):
                row = input(f"Row {i + 1}: ").strip()
                values = parse_row(row)
                if len(values) != cols:
                    raise ValueError(
                        f"Row {i + 1} should contain exactly {cols} values, "
                        f"but {len(values)} were entered."
                    )
                matrix.append(values)
            return np.array(matrix, dtype=float)
        except ValueError as exc:
            print(f"Invalid input: {exc}")
            print("Please try again.")


def parse_row(row: str) -> list[float]:
    """Parse a single row of matrix input into a list of floats.

    Accepts values separated by spaces or commas. Raises a ValueError when a
    token cannot be converted to a float.
    """
    if not row:
        return []
    tokens = re.split(r"[\s,]+", row.strip())
    values = []
    for token in tokens:
        if token == "":
            continue
        try:
            values.append(float(token))
        except ValueError:
            raise ValueError(f"Could not parse '{token}' as a number.")
    return values


if __name__ == "__main__":
    main()

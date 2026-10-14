class Matrix:
    def __init__(self, data):
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0
        self.data = data

    def show(self):
        for row in self.data:
            line = ""
            for val in row:
                line += f"{val:8.2f}" if isinstance(val, float) else f"{val:8}"
            print(line)
        print()

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Error: matrices must have the same dimensions to add.")
            return None
        result = [[0] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Error: matrices must have the same dimensions to subtract.")
            return None
        result = [[0] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] - other.data[i][j]
        return Matrix(result)

    def multiply(self, other):
        if self.cols != other.rows:
            print("Error: columns of first matrix must equal rows of second matrix.")
            return None
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                result[i][j] = total
        return Matrix(result)


if __name__ == "__main__":
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])

    print("Matrix A:")
    a.show()
    print("Matrix B:")
    b.show()

    print("A + B:")
    result = a.add(b)
    if result:
        result.show()

    print("A - B:")
    result = a.subtract(b)
    if result:
        result.show()

    print("A x B:")
    result = a.multiply(b)
    if result:
        result.show()
#6901012610137
#lab7-5
class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def solve(self):
        self._solve_util(0)
        return self.solutions

    def _solve_util(self, col):
        if col == self.n:
            # Found a valid solution
            solution = []
            for i in range(self.n):
                row = ""
                for j in range(self.n):
                    if self.board[i][j] == 1:
                        row += "Q "
                    else:
                        row += ". "
                solution.append(row)
            self.solutions.append(solution)
            return True

        for row in range(self.n):
            if self._is_safe(row, col):
                self.board[row][col] = 1
                self._solve_util(col + 1)
                self.board[row][col] = 0

    def _is_safe(self, row, col):
        # Check if the current position is under attack

        # Check the row on the left side
        for j in range(col):
            if self.board[row][j] == 1:
                return False

        # Check the upper diagonal on the left side
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check the lower diagonal on the left side
        i, j = row, col
        while i < self.n and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

n = 4
queens = NQueens(n)
solutions = queens.solve()

print(f"Total solutions for {n}-Queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()

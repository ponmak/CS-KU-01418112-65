# 07 Minesweeper

def board(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print()

m, n = input().split("x")
m, n = int(m), int(n)

# setup board
matrix = [[0 for j in range(n)] for i in range(m)]

# planting
bomb_count = int(input())
for i in range(bomb_count):
    x, y = input().split(',')
    x, y = int(x), int(y)
    # change bomb to *
    matrix[x][y] = "*" # shutup Pyright

# check 8 directions
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '*':
            # Top-left
            if i > 0 and j > 0:
                if matrix[i-1][j-1] != '*':
                    matrix[i-1][j-1] += 1

            # Top
            if i > 0:
                if matrix[i-1][j] != '*':
                    matrix[i-1][j] += 1

            # Top-right
            if i > 0 and j < n - 1:
                if matrix[i-1][j+1] != '*':
                    matrix[i-1][j+1] += 1

            # Left
            if j > 0:
                if matrix[i][j-1] != '*':
                    matrix[i][j-1] += 1

            # Right
            if j < n - 1:
                if matrix[i][j+1] != '*':
                    matrix[i][j+1] += 1

            # Bottom-left
            if i < m - 1 and j > 0:
                if matrix[i+1][j-1] != '*':
                    matrix[i+1][j-1] += 1

            # Bottom
            if i < m - 1:
                if matrix[i+1][j] != '*':
                    matrix[i+1][j] += 1

            # Bottom-right
            if i < m - 1 and j < n - 1:
                if matrix[i+1][j+1] != '*':
                    matrix[i+1][j+1] += 1

board(matrix)

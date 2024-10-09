# 07 Minesweeper

def board(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print()

m, n = input().split("x")
m, n = int(m), int(n)

# setup board
matrix = [[0 for j in range(m)] for i in range(n)]

# planting
bomb_count = int(input())
for i in range(bomb_count):
    x, y = input().split(',')
    x, y = int(x), int(y)
    # change bomb to *
    matrix[y][x] = "*" # shutup Pyrigh

    # check 8 directions
    for i in range(m):
        for j in range(n):
            # top left
            if i == 0 and j == 0 and matrix[i][j] == '*':
                matrix[i][j+1] += 1
                matrix[i+1][j] += 1
                matrix[i+1][j+1] += 1
            # 


board(matrix)

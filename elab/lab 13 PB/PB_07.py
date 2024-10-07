# 07 Minesweeper 

m, n = input().split("x")
m, n = int(m), int(n)

# setup board
matrix = [[0 for j in range(m)] for i in range(n)]

# planting
bomb_count = int(input())
for i in range(bomb_count):
    x, y = input().split(',')
    x, y = int(x), int(y)
    matrix[x][y] = '*'

print(matrix)



# 2d lists:

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])

# nested for loop

for row in number_grid:
    print(row)
    for column in row:
        print(column)
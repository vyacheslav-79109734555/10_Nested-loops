rowCount = 9
for row in range(10):
    for col in range(10):
        if col == row:
            print('^', end='')
        elif col == rowCount:
            print('^', end='')
        else:
            print(' ', end='')
    rowCount -= 1
    print()

# input will be num of rows
rows = int(input("Enter a the number of rows: "))

func_calls = 0
elapsed_time = 0

def weight_on(row, col):
    if row == 0:
        result = 0
        return(result)
    # outer left
    elif col == 0:
        # result = 200 + (weight_on(row - 1, 0) / 2)
        result = (200 + weight_on(row - 1, 0)) / 2
        return(result)
    # outer right
    elif col == row:
        # result = 200 + (weight_on(row - 1, row) / 2)
        result = (200 + weight_on(row - 1, 0)) / 2
        return(result)
    # middle columns
    else:
        result = 200 + ((weight_on(row - 1, col -1) + weight_on(row - 1, col)) / 2)
        # result = (200 + weight_on(row - 1, col -1) + weight_on(row - 1, col)) / 2
        return(result)


for row in range(0, rows):
    # print(f'row: {row}')
    for col in range (0, row + 1):
        # print(f'row: {int(row)} col: {int(col)}', end=" ")
        print(weight_on(int(row), int(col)), end=" ")
    print("\r")

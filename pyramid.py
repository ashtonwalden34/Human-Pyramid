# input will be num of rows
rows = int(input("Enter a the number of rows: "))

def weight_on(row, col):
    col = int(col)
    row = int(row)
    if row == 0:
        result = 0
    # outer left
    elif col == 0:
        #  what the video showed
        # result = (200 + weight_on(row - 1, 0)) / 2
        #  what I think may be correct
        result = 200 + (weight_on(row - 1, 0) / 2)
    # outer right
    elif col == row:
         #  what the video showed
        # result = (200 + weight_on(row - 1, row)) / 2
        #  what I think may be correct
        result = 200 + (weight_on(row - 1, row) / 2)
    # middle columns
    else:
         #  what the video showed
        # result = (200 + (weight_on(row - 1, col -1) + weight_on(row - 1, col)) / 2)
        #  what I think may be correct
        result = 200 + (weight_on(row - 1, col -1) + weight_on(row - 1, col) / 2)
        pass


for row in range(rows):
    # num of cols = num of row + 1
    for col in range(rows + 1):
        print(weight_on(row, col))
    # print new line
    print()
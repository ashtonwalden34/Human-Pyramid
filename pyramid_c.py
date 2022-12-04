import sys
import argparse
from time import perf_counter

arg_parser = argparse.ArgumentParser()

function_calls = 0
elapsed_time = 0
weights = {}

def weight_on(row, col):
    global function_calls
    function_calls += 1
    if row == 0:
        result = 0
        weights[row, col] = result
        return(result)
    # outer left
    elif col == 0:
        # result = 200 + (weight_on(row - 1, 0) / 2)
        result = (200 + weight_on(row - 1, 0)) / 2
        weights[row, col] = result
        return(result)
    # outer right
    elif col == row:
        # result = 200 + (weight_on(row - 1, row) / 2)
        result = (200 + weight_on(row - 1, 0)) / 2
        weights[row, col] = result
        return(result)
    # middle columns
    else:
        result = 200 + ((weight_on(row - 1, col -1) + weight_on(row - 1, col)) / 2)
        weights[row, col] = result
        # result = (200 + weight_on(row - 1, col -1) + weight_on(row - 1, col)) / 2
        return(result)


def main():
    time_start = perf_counter()
    rows = int(input("Enter a the number of rows: "))
    f = open('part3.out', 'w')
    for row in range(0, rows):
        for col in range (0, row + 1):
            f.write(f'{weight_on(int(row), int(col)):.2f}')
            f.write(" ")
            # print(f'{weight_on(int(row), int(col)):.2f}', end=" ")
        # print("\r")
        f.write("\r")
    
    # print(f'\nFunction Calls: {function_calls}')
    f.write(f'\nFunction Calls: {function_calls}')
    time_stop = perf_counter()
    time_elapsed = time_stop - time_start
    f.write(f'\nTime Elapsed: {time_elapsed} seconds')

    print(weights)

    # arg_parser.add_argument(rows, type=input, default=0)

if __name__ == "__main__":
    main()


#  argeparse input

# check key in dictionary first
    # if yes then pull value
    # if no then calculate
# add to dictionary after calculating

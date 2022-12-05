import sys
import argparse
from time import perf_counter
arg_parser = argparse.ArgumentParser()

function_calls = 0
elapsed_time = 0
cache_hits = 0
weights = {}


class Person():
    def __init__(self, row, col, weight = 200, shoulder = "0.00"):
        self.row = row
        self.col = col
        self.weight = weight
        self.shoulder = shoulder

    def weight_on(self):
        global cache_hits
        if (self.row, self.col) in weights:
            return(self.shoulder)
        else: 
            if self.row == 0:
                if (self.row, self.col) in weights.keys():
                    cache_hits += 1
                    return(weights.get(self.shoulder))
                else:
                    self.shoulder = 0
                    weights[self.row, self.col] = Person(self.row, self.col, self.weight, self.shoulder)
                    return(self.shoulder)

            # outer left
            elif self.col == 0:
                if (self.row, self.col) in weights.keys():
                    cache_hits += 1
                    return(weights.get(self.row, self.col))
                else:
                    result = (200 + self.weight_on()) / 2
                    weights[self.row, self.col] = Person(elf.row, self.col, self.weight, self.shoulder)
                    return(result)

            # outer right
            elif self.col == self.row:
                if (self.row, self.col) in weights.keys():
                    cache_hits += 1
                    return(weights.get(self.row, self.col))
                else:
                    result = (200 + self.weight_on(self.row - 1, 0)) / 2
                    weights[self.row, self.col] = Person(self.row, self.col, self.weight, self.shoulder)
                    return(result)

            # middle columns
            else:
                if (self.row, self.col) in weights.keys():
                    cache_hits += 1
                    return(weights.get(self.row, self.col))
                else:
                    result = 200 + ((self.weight_on(self.row - 1, self.col -1) + self.weight_on(self.row - 1, self.col)) / 2)
                    weights[self.row, self.col] = Person(self.row, self.col, self.weight, self.shoulder)
                    return(result)

    # method weight_on
        # no parameters
        # if self.should has val, return
        # else recursivley compute how much weight carrying and return

    # dictionary
        # location person pairs


def main():
    time_start = perf_counter()
    rows = int(input("Enter a the number of rows: "))
    f = open('part4.out', 'w')
    for row in range(0, rows):
        for col in range (0, row + 1):
            f.write(f'{Person(row, col).weight_on()}')
            f.write(" ")
        # print("\r")
        f.write("\r")
    
    # print(f'\nFunction Calls: {function_calls}')
    time_stop = perf_counter()
    time_elapsed = time_stop - time_start
    f.write(f'\nTime Elapsed: {time_elapsed} seconds')
    f.write(f'\nFunction Calls: {function_calls}')
    f.write(f'\nCache Hits: {cache_hits}')
    
    print(weights)

    # arg_parser.add_argument(rows, type=input, default=0)

if __name__ == "__main__":
    main()


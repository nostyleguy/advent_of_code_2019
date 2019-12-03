#!/usr/bin/python2.7

# Advent of Code 2019
# Day 01 - The Tyranny of the Rocket Equation
#

import sys
from functools import reduce

def calculate_fuel(mass):
    return (int(mass) / 3) - 2


def main():
    filepath = sys.argv[1]

    with open(filepath) as input_file:
        inputs = input_file.readlines()

    # Calculate the fuel requirement of each mass in the inputs
    calculated_fuels = list(map(calculate_fuel, inputs))

    # Sum the calculated fuel costs
    total = reduce((lambda x,y: x + y), calculated_fuels)
    
    print("Total: {}".format(total))            

if __name__ == "__main__":
    main()
import argparse

# initialize argparse
parser = argparse.ArgumentParser(description="A program that does something")

# add positional argument
parser.add_argument('filename')

# parse arguments
arguments = parser.parse_args()
print(arguments)
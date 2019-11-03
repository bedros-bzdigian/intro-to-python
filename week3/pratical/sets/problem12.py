import argparse

parser = argparse.ArgumentParser()

set3 = {1,2,3,4,5,6,7,8}

parser.add_argument("--number", help="display a cube of a given number", type=int)

args = parser.parse_args()

if args.number:
    x =args.number in set3
print (x)    



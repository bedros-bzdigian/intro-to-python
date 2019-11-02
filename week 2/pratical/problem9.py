import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="some text", type=str)

parser.add_argument("--cube", help="display a cube of a given number", type=int)

parser.add_argument("--cube1", help="display a cube of a given number", type=int)

args = parser.parse_args()

if args.cube:
    y = (args.cube)
if args.cube1:
    x = (args.cube1)
print (args.text [args.cube:args.cube1])     
import argparse

set1 = {1,2,3,'hi'}

print ("set1 before changes: " , set1)

parser = argparse.ArgumentParser()

parser.add_argument("--text", help="some text", type=str)

parser.add_argument("--number", help="display a cube of a given number", type=int)

args = parser.parse_args()

if args.text:
 set1.update({args.text})

if args.number:
 set1.update({args.number})

print ("set1 after changes: " , set1)      
    





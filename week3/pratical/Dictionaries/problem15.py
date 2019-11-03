import argparse

dict1 = {'key':1 , 'value':2}

print ("dict1 before changes: " , dict1)

parser = argparse.ArgumentParser()

parser.add_argument("key", help="key", type=str)

parser.add_argument("value", help="value", type=int)

args = parser.parse_args()

dict1[args.key] = args.value

print ("dict1 after changes: " , dict1)
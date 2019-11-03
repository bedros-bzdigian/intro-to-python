import argparse

list4 = ['hi' , 1 , 'hello' , 2]

parser = argparse.ArgumentParser()

parser.add_argument("text", help="some text", type=str)

parser.add_argument("number", help="display a cube of a given number", type=int)

args = parser.parse_args()

print ("list4 before changes: " , list4)

list4.remove(args.text)

list4.remove(args.number)
print ("list4 after changes: " , list4)





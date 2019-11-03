import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number", help="display a cube of a given number", type=int)

args = parser.parse_args()

list2 = [0 , 'hi' , 2 , 100 ,300 , 2]

x = list2.count(args.number)
print ("list2: " , list2)
print ("the number of using this number is: " , x)

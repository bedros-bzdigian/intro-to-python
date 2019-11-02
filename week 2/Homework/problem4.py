import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="some text", type=str)


args = parser.parse_args()

print("The given text: " , args.text)

print ( "The syria count is: " , args.text.count('syria') )

print ("The new string: " , args.text.replace('syria' , 'Armenia'))

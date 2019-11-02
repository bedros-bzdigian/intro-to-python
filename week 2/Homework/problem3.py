import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="some text", type=str)

parser.add_argument("first_word", help="some text1", type=str)

parser.add_argument("second_word", help="some text2", type=str)

args = parser.parse_args()

print("The given text: " , args.text)

print ("the first word: " ,args.first_word)

print ("the second word :" , args.second_word )

print ("output string : " , args.text.replace(args.first_word, args.second_word) )

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type= str)

args = parser.parse_args()

f = args.text.replace('usa', 'Armenia').replace('USA', 'Armenia')

print("The given string :", args.text)

print("The USA/usa count is :", args.text.upper().count('USA'))

print("The new string: ", f)
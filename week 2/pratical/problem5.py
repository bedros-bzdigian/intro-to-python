import argparse 

parser = argparse.ArgumentParser()
parser.add_argument ("text" , help = "some text" , type = str)
args = parser.parse_args()

print ( args.text )
print (args.text.lower())
print (args.text.upper())
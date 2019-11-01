import argparse 

parser = argparse.ArgumentParser()
parser.add_argument ("text" , help = "your inputted name will printed" , type = str)
args = parser.parse_args()

print ("welcome !" , args.text)
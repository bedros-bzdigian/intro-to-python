import argparse 

parser = argparse.ArgumentParser()
parser.add_argument ("square" , help = "your inputted name will printed" , type = int)
args = parser.parse_args()

print ("Happy birthday, you are already " , args.square , "years old")

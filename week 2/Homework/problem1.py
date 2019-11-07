import time
import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("--cube", help="display a cube of a given number", type=int)

parser.add_argument("--cube1", help="display a cube of a given number", type=int)

args = parser.parse_args()

today = datetime.date.today()

print ("current date: " , today)
if args.cube:
    tdelta = datetime.timedelta(years = args.cube)
    
if args.cube1:
    tdelta = datetime.timedelta(days = args.cube1)
    
    
print ("current date: " , today + tdelta)
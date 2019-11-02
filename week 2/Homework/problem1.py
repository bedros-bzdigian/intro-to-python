import time
import argprase
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("--cube", help="display a cube of a given number", type=int)

parser.add_argument("--cube1", help="display a cube of a given number", type=int)

args = parser.parse_args()

local_time = time.asctime()

print ("current date: " , local_time)
if args.cube:
    print(args.cube)
if args.cube1:
    print(args.cube1)

print ("final date is: " , local_time.timedelta(years = args.cube) )
    

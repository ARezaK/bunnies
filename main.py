from subbrute import subbrute
import argparse
import sys
from bruteforceftp import check_anonymous_login, brute_force


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")

args = parser.parse_args()

if not args.target: 
    print("Need a target")
    sys.exit(0)

target = args.target

for d in subbrute.run(target):
    print d 
    if 'ftp' in d[0]:
        print(d[0])
        print 'found ftp'
        check_anonymous_login(d[0])
        brute_force(d[0])


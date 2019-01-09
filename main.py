from subbrute import subbrute
import os
import argparse
import sys
from bruteforceftp import check_anonymous_login, brute_force


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-e", "--dnsenum")
parser.add_argument('-d', '--domlink')
parser.add_argument('-s', '--sqlmap')
parser.add_argument('-n', '--snallygaster')

args = parser.parse_args()

target = args.target
dnsenum = args.dnsenum
domlink = args.domlink
snallygaster = args.snallygaster

if dnsenum:
    for d in subbrute.run(target):
        print d 
        if 'ftp' in d[0]:
            print(d[0])
            print 'found ftp'
            result = check_anonymous_login(d[0])
            if result == 1: # means correct addr was not provided
                continue
            brute_force(d[0])

if domlink:
    # need api key
    pass

if snallygaster:
    try:
        os.system('snallygaster %s -d' % target)
    except:
        print("u dont have snallygaster installed; do pip3 install snallygaster")


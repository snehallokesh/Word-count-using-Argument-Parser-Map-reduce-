'''Using argument parser to input string'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here", nargs='+')
args = parser.parse_args()
w = args.echo

for line in w:
    line = line.strip()
    word = line.split()
    print(word)
    mydict = {}
    for item in word:
        mydict[item] = word.count(item)
    print(mydict)

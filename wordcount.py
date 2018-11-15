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





    '''word = line.split()
    count = 1
    
    for words in word:
        if words == word:
            current_count += count
    else:
        # print(w, current_count)
        current_count = count'''

    '''words = line.split()
    print(words)
    for word in words:'''


'''
for line in sys.stdin:
    for word in line.strip().split():
        print(word, 1)'''


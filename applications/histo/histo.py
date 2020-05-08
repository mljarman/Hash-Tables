import re
counts = {}
def histo(filename):
    # open and read the file:
    file = open(filename, 'r')
    file = file.read()
    file = re.sub("[\"\:;,\.\-\+=/\\\|\[\]\{\}\(\)\*\'^&?!]", "", file)
    file = file.lower()
    # count words in txt file:
    for w in file.split():
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1
    # sort dictionary by highest word count and then alphabetically:
    words = list(counts.items())
    ordered = sorted(words, key = lambda counts: (-counts[1], counts[0]))
    print(ordered)
    # display:
    for word, count in ordered:
        print(f'{word}\t\t\t{"".join(["#"]*count)}')

filename = 'robin.txt'
histo(filename)

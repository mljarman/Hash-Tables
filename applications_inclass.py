'''
benefits: look up things quickly O(1) linear lookups

if you have 5 elements
    linear search O(n)
if you have 5 trillion elements
    linear search takes a long time
    BST binary search tree O(log n) less memory
    Hashtable O(1) more memory

Speed of search
---------------------
Linear search through an array

Network caching (web browsers)

Memoization--expensive calculation, want to do it once and store the result.

Indexing
--------
Alice: 30
Bob: 40
Charlie: 20
Dave: 20

'show me all the ppl who are 30'
what do i want to look up by? --> thats the key

20: [Charlie, Dave]
30: [Alice]
40: [Bob]

given a list of records, need to convert into a hashtable first O(n)
THEN we can do quick lookups O(1)

Removing Duplicates
----------------------
h = {}
for i in data:
    # have we seen this data before?
    if h[i]: # same as checking for existence in set
        continue
    # we've seen it now:
    h[i] = True # same as adding to a set

    print(i)

for i in data
    for j in data
        for k in data <-- linear search? replace with hashtable O(1)
    **whole thing becomes O(n^2)**

Counting elements
-------------------
How many times an item occurs in dataset
 1
 5
 5
 7
 9
 2
 3
 9
 5

 go through and count how many of each item in the list O(n^2)
 h = {}
 for i in data:
     # is this data already a key in the hashtable? O(1)
     if i not in h:
         # if not, add it
         h[i] = 0
    # now we can increment
     h[i] += 1
OR

for i in data:
    if i not in h:
        h[i] = 1
    else:
        h[i] += 1

Aside
------
the key in the dict can be any immutable type, including tuples.
h = {
(1,2): 'value1',
(3,4): 'value2',
}



'''
# slow calculation caching
cache = {}
def fib(n):
    if n <=1:
        return n
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

#for i in range(100):
    #print(fib(i))
# slow because of lots of repeated computations
# need to make cache
cache = {}
def build_lookup_table():
    for i in range(1, 6):
        inv_sqrt(i)

import math
def inv_sqrt(n):
    if n not in cahce:
        cache[n] = 1 / math.sqrt(n)
    return cache[n]

#for i in range(1, 6):
    #print(inv_sqrt(i))


# can't sort a dictionary
# can turn dictionary into list and sort from there
d = {
    'foo': 12,
    'bar': 17,
    'qux': 2
}

# sort by key
items = list(d.items())
print(items)

items.sort()
print(items)

for i in items:
    print(f'{i[0]}: {i[1]}')
# sort by value
def get_key(e):
    return e[1]

items = list(d.items())
items.sort(key=lambda e: e[1], reverse=True) # to reverse list
# OR:
items.sort(key=get_key)

for i in items:
    print(f'{i[0]}: {i[1]}')


'''
Your Hash Table vs Dict
------------------------

put(k,v)   ==  d[k] = v
x = get()  ==  v = d[k]
delete(k)  ==  del d[k]

'''

# every letter maps to another letter
def encode(s):
    r = ""
    for c in s:
        r += encode_table[c]
    return r

def decode(s):
    r = ""
    for c in s:
        r += decode_table[c]
# construct decode table from encode table:
decode_table = {}
# get k, v pair from table
for k, v in encode_table.items()
    # every value becomes a key
    decode_table[v] = k
# OR
decode_table = encode_table(map(reversed, encode_tables.items()))

# sprint challenge solve 3 out of 5 problems
# come up with slow naive version then how to use hashtable to solve

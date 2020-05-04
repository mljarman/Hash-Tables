['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
#The Time complexity is depending on the size of the key, not the hash table size
#list must iterate through the entire list to search for something O(n)
hash_table_size = 8
hash_table = [None] * hash_table_size
def myhash(s):
    str_bytes = str(s).encode() # incase s was a number or not a string, will make it a string
    total = 0
    # add the bytes in the string
    for b in str_bytes:
        total += b

        total &= 0xfffffff # djb2 8 f's
        total &= 0xffffffffffffffff # fnv-1 16 f's

    return total

def hash_index(s):
    h = myhash(s)
    return h % hash_table_size # no matter how big h is, the % says it has to fit in the size of the
    # hash_table_size. remainder will always be less than the diviser.

def put(key, value):
    # get the index into the hash table list (based on key)
    index = hash_index(key)
    hash_table[index] = value

def get(key):
    index = hash_index(key)
    return hash_table[index]

def delete(key):
    index = hash_index(key)
    hash_table[index] = None

if __name__ == "__main__":
    # if running from command line, do all these things:
    print(myhash('hello'))
    print(hash_index('hello'))
    print(hash_index('foobar'))
    print(hash_index('cats'))
    print(hash_index('beej'))
    print(hash_table)
    put('hello', 37)# prints 37 at index 4 #hello will always hash to 4 so we
   # only need hello to find an index position for 37.
    put('foobar', 126)
    put('cats', 'dogs')

    print(hash_table)

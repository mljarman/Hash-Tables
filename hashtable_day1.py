'''
Using an array:
'''
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity




    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        # for each byte, multiply hash by the fnv prime
        # xor hash with the byte from the input

        Implement this, and/or DJB2.
        """



    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)
            hash &= 0xffffffff
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity
        # return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        self.storage[index] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            print('Key not found')
        self.storage[index] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            return None
        else:
            return self.storage[index]

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # double the capacity
        # self.capacity = capacity * 2
        pass
        # reset-indices:

if __name__ == "__main__":
    ht = HashTable(2)
    ht.put("line_1", "Tiny hash table")
    ht.put("line_1", "test")
    print(ht.storage)
    print(ht.hash_index("line_1"))
    ht.put("b", "Filled beyond capacity")
    print(ht.storage)
    ht.put("line_3", "Linked list saves the day!")
    print(ht.storage)

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)
    #
    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    #
    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))
    #
    # print("")

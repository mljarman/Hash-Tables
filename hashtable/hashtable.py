
'''
Using a linked list:
'''
class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return (f"('{self.key}','{self.value}')")

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.counter = 0




    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        # for each byte, multiply hash by the fnv prime
        # xor hash with the byte from the input

        Implement this, and/or DJB2.
        """



    def djb2_ll(self, key):
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
        return self.djb2_ll(key) % self.capacity
        # return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # find hash index:
        index = self.hash_index(key)
        # variable to create new node:
        new_node = HashTableEntry(key, value)
        # current node will be the index location:
        current = self.storage[index]
        # check if something is at index, if there isn't, add the node:
        if current is None:
            self.storage[index] = new_node
            self.counter += 1
        else:
            # as long as the next node is not None and not matching key:
            while current.next is not None and current.key != key:
                # keep moving
                current = current.next
                # if key is already there, override its value:
            if current.key == key:
                current.value = value
                # otherwise, create a new node at the end:
            else:
                current.next = new_node
                self.counter += 1

        if (self.counter/self.capacity) >= .7:
            self.resize(new_capacity=self.capacity*2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # find hash index:
        index = self.hash_index(key)
        # if current is None, print key not found:
        if self.storage[index] is None:
            return
        else:
            # set previous and current variables:
            previous = None
            current = self.storage[index]
            # while there's more than 1 node in the linked list:
            while current.next is not None:
                # if keys match:
                if current.key == key:
                    # if key is first node:
                    if previous is None:
                        # change pointer from first node to next:
                        self.storage[index] = current.next
                    else:
                        # skip over node so previous points to next:
                        previous.next = current.next
                        # decrease count
                        self.counter -= 1
                    break
                else:
                    # keep moving down the list looking for matching key
                    previous = current
                    current = current.next
            # if only 1 item in the list and keys match, replace with None
            if previous is None and current.key == key:
                self.storage[index] = None
                self.counter -= 1
        if (self.counter/self.capacity) >= .7:
            self.resize(new_capacity=self.capacity*2)
        return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # find hash index:
        index = self.hash_index(key)
        # index will be current node:
        current = self.storage[index]
        # while something at that index, if keys match, return that value:
        while current is not None:
            if current.key == key:
                return current.value
            else:
                # move through chain to see if key is there:
                current = current.next
        # if key not in hash table, return None:
        else:
            return None

    def resize(self, new_capacity=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # load factor:
        load_factor = self.counter / self.capacity
        # original hashtable
        orig_storage = self.storage
        # orig_count = self.counter
        if new_capacity is None:
            new_capacity = self.capacity
        temp_hash_table = HashTable(capacity=new_capacity)

        if new_capacity is not None:
            # if new_capacity given, update self.storage
            for index in orig_storage:
                while index is not None:
                    temp_hash_table.put(index.key, index.value)
                    index = index.next
            self.storage = temp_hash_table.storage
            self.capacity = temp_hash_table.capacity


if __name__ == "__main__":
    ht = HashTable(2)
    ht.put("line_1", "Tiny hash table")
    print((len(ht.storage),ht.counter, ht.capacity, '1'))
    ht.put("line_2", "test")
    print((len(ht.storage),ht.counter, ht.capacity, '2'))
    ht.put("b", "Filled beyond capacity")
    print((len(ht.storage),ht.counter, ht.capacity, '3'))
    ht.put("abc", "Linked list saves the day!")
    print((len(ht.storage),ht.counter, ht.capacity, '4'))
    ht.delete("line_3")
    print((len(ht.storage),ht.counter, ht.capacity, '5'))

    print("")

    # Test storing beyond capacity
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    print(ht.storage)
    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

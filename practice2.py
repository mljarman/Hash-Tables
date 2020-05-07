'''
Open Addressing: Linear Probing
--------------------------------

'foo' hashes to index 1
'bar' hashes to index 2
'baz' hashes to index 2

put('foo', 12)
put('bar', 30)
put ('baz', 99)

put('qux', 11) --- has to be index 0

0       1   2   3    <-- index
[None, 12, 30, None]

[None, 12, 99, None]

[None, ('foo',12), ('bar'30), ('baz',99)] (with probing, moves to next empty spot)

delete('bar')
[None, ('foo',12), None, ('baz',99)]

get('baz') will try to go to where bar was, but it won't be there. can't have deleted
entries as None.

[None, ('foo',12), DELETED, ('baz',99)]






'''

'''
Collision Resolution by Chaining
----------------------------------
Each slot of the hash table holds a linked List
collisions are handled by adding multiple items to the same linked List


slot index (linked list)
----------------------------
0       -> None
1       -> ('foo', 12)
2       -> ('bar', 30) -> ('baz', 999)
3       -> NOne

put('foo', 12) index 1
put('bar', 30) index 2
put('baz', 999) index 2

get('beej') hashes to index 1, not there return none
get('baz') searches index 2, finds baz returns 999

delete('bar') indexes to 2, search the list for key, if found delete
Put:
find hash index
search the list for the key
if it's there, replace the value
if it's not, append a new record to the list

Get:
find the hash index
search the list for the key
if found, return the value
else return none

Delete:
find the hash index
search the list for the key
if found, delete the node from the list
else return none

'''

'''
linked list refresher
put 1
(1) -> (2)(current) -> (3) -> None
head


None --> list is empty
head
'''

class Node:
    def__init__(self, value)
        self.value = value
        self.next = None


head = None # empty linked list

# insert (at head)
def_insert_at_head(value):
# (99) -> (1) -> (2) -> (3) -> None
    n = Node(value)
    n.next = head
# (99) -> (1) head -> (2) -> (3)
    head = n
# (99) head -> (1) -> (2) -> (3)
    return n
# append (at tail)
def append_at_tail(value):
    # (1) head -> (2) -> (3) -> none
    #( 1) head -> (2) -> (3) -> (99) ->none
    n = Node(value)
    if head is None:
        head = n
        return
    cur = head

    while cur.next is not None:
        # (1) head -> (2) -> (3)(cur) -> (99)(n) ->none
        cur = cur.next
    cur.next = n


# find
def find(value):
    cur = head
    while cur is not None:
        if cur.value == value:
            return cur
        cur = cur.next
    return None

# delete
def delete(value):
    # (1) head -> (2)(want to delete) -> (3) -> none
    # (1) head -> (3) -> none
    # find the node
    cur = head
    # delete the head special case
    if cur.value == value
        head = head.next
        cur.next = None
        return cur
    prev = None
    while cur is not None:
        if cur.value == value:
            # found it, delete it
            prev.next = cur.next
            cur.next = None
            return cur
        prev = cur # can do prev = prev.next
        cur = cur.next
    return None

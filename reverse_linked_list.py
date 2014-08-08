class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next
    def __str__(self):
        return repr(self.item)

def generate_linked_list(size):
    """Expects positive integer greater than 1 for size"""
    root = Node(0)
    curr = root
    for i in xrange(1,size):
        node = Node(i)
        curr.next = node
        curr = curr.next
    return root

def reverse_linked_list(root):
    reverse = []
    curr = root
    while curr != None:
        reverse.insert(0,curr.item)
        curr = curr.next

    new_root = Node(reverse[0])
    curr = new_root
    for i in reverse[1:]:
        node = Node(i)
        curr.next = node
        curr = curr.next
    return new_root

root = generate_linked_list(10)

curr = reverse_linked_list(root)
while curr != None:
    print curr
    curr = curr.next

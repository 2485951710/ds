class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

def is_circle(head):
    prev = head
    curr = head
    while curr and curr.next:
        prev = prev.next
        curr = curr.next
        if prev == curr:
            return True
    return False


if __name__ == '__main__':

    a = Node(2)
    b = Node(3)
    c = Node(4)
    d = Node(5)
    e = Node(6)
    a.next = b
    b.next = c
    c.next = d
    d.node = e
    e.node =c
    print(is_circle(a))
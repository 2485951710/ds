from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def insert(self,index,data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prve = self.get(index-1)
            new_node.next = prve.next
            prve.next = new_node
        self.size += 1

    def __repr__(self):
        curr = self.head
        string = ""
        while curr:
            string += f"{curr}-->"
            curr = curr.next
        return string + "END"

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("索引越界")
        elif index == 0:
            self.head = self.head.next
        elif index == self.size-1:
            remove_node = self.get(index-1)
            remove_node.next = None
        else:
            prev = self.get(index-1)
            prev.next = prev.next.next
        self.size -= 1

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            temp = curr.next
            if prev is None:
                curr.next = prev
            else:
                curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

if __name__ == '__main__':
    l = LinkList()
    l.insert(0, 1)
    l.insert(1, 2)
    l.insert(2, 4)
    l.insert(2, 3)
    l.insert(0, -1)
    l.insert(1, 0.5)
    l.remove(5)
    print(l)
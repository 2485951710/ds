
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class LinkList:
    def __init__(self):
        self.head=None

    def insert_head(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current}-->"
            current = current.next
        return string_repr + "END"

    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            step = self.head
            while step.next:
                step = step.next
            step.next = Node(data)

    def insert(self, i, data):
        if self.head is None or i==1:
            self.head = self.insert_head(data)
        else:
            curr = self.head
            j = 1
            while j<i:
                prev = curr
                curr = curr.next
                j += 1
            new_node = Node(data)
            prev.next = new_node
            new_node.next = curr

    def linklist(self,obj):
        self.head = Node(obj[0])
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

    def delect_head(self):
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next

    def pop(self):
        if self.head is None:
            print("空链表")
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None

if __name__ == '__main__':
    li = LinkList()
    # li.insert_head(100)
    # li.insert_head(99)
    # li.insert_head(98)
    # li.append(101)
    # li.print_list()
    # print(li)
    # li.insert(4,100.5)

    li.linklist([1,2,['a','b'],4,5,6])
    li.pop()

    print(li)
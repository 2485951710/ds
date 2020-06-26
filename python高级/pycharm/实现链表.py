class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class LikeList:
    def __init__(self):
        self.head=None

    def insert_head(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
        self.head=new_node

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            print(current)
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
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            curr = self.head
            prev = self.head
            j = 1
            while j<i:
                prev = curr
                curr = curr.next
                j += 1
            new_node = Node(data)
            prev.next = new_node
            new_node.next = curr

    def liknlist(self,obj):
        self.head = Node(obj[0])
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next


if __name__ == '__main__':
    l=LikeList()
    # l.insert_head(100)
    # l.insert_head(99)
    # l.insert_head(98)
    # print(l)
    # l.append(101)
    # print(l)
    # l.insert(4,100.5)
    l.liknlist([1,2,3,4,])
    print(l)
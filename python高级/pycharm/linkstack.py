class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"

class LinkStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        else:
            temp =self.top
            self.top = self.top.next
            self.size -= 1
        return temp.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size

    def __repr__(self):
        curr = self.top
        string_repr = ""
        while curr:
            string_repr += f"{curr}-->"
            curr = curr.next
        return string_repr + "END"

if __name__ == '__main__':
    stack = LinkStack()
    stack.push(5)
    stack.push(9)
    stack.push('python')
    print(stack)
    print(stack.size)
    print(stack.is_empty())
    stack.pop()
    print(stack)
    print(stack.size)
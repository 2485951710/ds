class Stack:
    def __init__(self,limit=10):
        self.stack = []
        self.size = 0

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        if len(self.stack) < self.size:
            raise Exception("stackoverflow")
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.size -= 1

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return self.size

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(1)
    s.push(2)
    print(s)
    print(s.pop())
    print(s.peek())
    print(s.is_empty())
    print(s)


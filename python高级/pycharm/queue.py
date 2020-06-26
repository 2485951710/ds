class Queue:
    def __init__(self):
        self.entires = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = "<" + str(self.entires)[1:-1] + ">"
        return printed

    def put(self, items):
        self.entires.append(items)
        self.length += 1

    def get(self):
        self.length -= 1
        dequened = self.entires[self.front]
        self.entires = self.entires[1:]
        return dequened

    def front(self):
        return self.entires[0]

    def length(self):
        return self.length


if __name__ == '__main__':
    que = Queue()
    que.put(10)
    que.put(5)
    print(que)
    print(que.get())
    print(que)
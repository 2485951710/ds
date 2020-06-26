class Array:
    def __init__(self, capacity):
        self.array = [None]*capacity
        self.size = 0

    def insert(self, index, element):

        if index < 0 or index > self.size:
            raise Exception('数据越界')
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size-1, index-1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def output(self):
        for i in range(self.size):
            print(self.array[i], end='->')

    def addcapacity(self):
        new_array=[None]*self.size*2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('数据越界')
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]
        self.array[self.size-1]=[None]
        self.size -= 1

if __name__ == '__main__':
    arr=Array(4)
    arr.insert(0, 0)
    arr.insert(1, 1)
    arr.insert(2, 2)
    arr.insert(3, 3)

    arr.remove(3)
    arr.output()
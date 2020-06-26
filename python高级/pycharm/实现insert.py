class Array:
    def __init__(self, capacity):
        self.array = [None]*capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception('数据越界')
        if self.size >= len(self.array):
            # pass
            self.addcapacity()
        for i in range(self.size-1, index-1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def addcapacity(self):
        new_array = [None]*self.size*2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i], end='->')

    def pop(self, index=-1):
        if index < 0 or index > self.size:
            raise Exception('数据越界')


    def remove(self,element):
        if element not in self.array:
            raise Exception('{}不在列表内'.format(element))
        else:
            for i in range(self.size):
                if element == self.array[i]:
                    index = i
                    break
        for i in range(index, self.size):
            self.array[i] = self.array[i+1]
        self.array[self.size-1] = [None]
        self.size -= 1

    def mod(self):
        new_array = [None]*self.size
        for i in range(self.size):
            new_array[i] = self.array[i]/self.array[0]
        return new_array






if __name__ == '__main__':
    arr = Array(4)
    arr.insert(0, 0)
    arr.insert(1, 1)
    arr.insert(2, 2)
    arr.insert(3, 3)
    arr.insert(3, 4)
    arr.remove(0)
    arr.output()
    print()
    print(arr.mod())
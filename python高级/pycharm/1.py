class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print('{}学习很努力'.format(self.name))
stu = Student('张三',20)
print(stu.name)
print(stu.age)
stu.study()
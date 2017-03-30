class Test(object):
    count = 0

    def __init__(self,x,y):

        self.__x = x
        self.y = y

    def add(self):
        return self.__x+self.y

    @staticmethod
    def method_static():
        print("I'm static")

    @classmethod
    def method_class(cls):
        print("I'm class method")

    def msg(self):
        return 'original msg'

class Test2(Test):
    def msg(self):
        return (super().msg()+' child')

test = Test(5,9)
test2 = Test2(5,9)

print(test.add())
# test.__x=77
print(test.add())
Test.method_static()
test.method_static()

Test.method_class()
test.method_class()

print(test.msg())
print(test2.msg())


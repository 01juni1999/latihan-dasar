class Person :
    def __init__(self,name):
        self.name=name

    def say_hi(self):
            print ('hello,my name is' ,self.name)

p = Person ('Swaroop')
p.say_hi()
# the previous 2 lines can also be written as
# person('swaroop').say_hi()
 
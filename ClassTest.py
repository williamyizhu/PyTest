
class MyClass(object):
    def __init__(self):
        self.x = 1

    def func(self):
        print('dummy')
    
    def add(self):
        self.y = self.x + 10
        
    def run(self):
        eval('self.%s()' % ('add'))
        
class FramerClass(MyClass):
    def __init__(self):
        MyClass.__init__(self)
        
    def func(self):
        print('cme')

My = MyClass()
My.func()
My.run()
My.y

Framer = FramerClass()
Framer.func()


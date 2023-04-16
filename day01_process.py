import os
from multiprocessing import Process

def foo():
    print('This is foo')

def bar():
    print('This is bar')

def baz():
    print('This is baz')

if __name__ == '__main__':
    park_child1 = Process(target=foo).start()
    park_child2 = Process(target=bar).start()
    park_child3 = Process(target=baz).start()
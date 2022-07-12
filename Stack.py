# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 00:16:35 2022
@author: Eriny
"""
    
class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0 ## if len(self.items) == 0: return True
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    # Try To Comment This Function And Run The Program To See The Result
    def __str__(self):
        return str(self.items)

    
if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.isEmpty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s)
    print(s.size())

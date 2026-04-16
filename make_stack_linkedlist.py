class Node:

  def __init__(self,value):
    self.data = value
    self.next = None

class Stack:

  def __init__(self):
    self.top = None

  def push(self, value):

    new_node = Node(value)

    new_node.next = self.top

    self.top = new_node

  def pop(self):

    if self.top is None:
      return "Stack Empty"
    else:
      data = self.top.data
      self.top = self.top.next
      return data

  def is_empty(self):
    return self.top == None

  def peek(self):

    if self.top is None:
      return "Stack Empty"
    else:
      return self.top.data

  def traverse(self):

    temp = self.top

    while temp is not None:
      print(temp.data,end=' ')
      temp = temp.next

  def size(self):

    temp = self.top
    counter = 0

    while temp is not None:
      temp = temp.next
      counter+=1

    return counter

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.traverse()
print(s.pop())
# s.traverse()
print(s.peek())
# s.traverse()
print(s.is_empty())
# s.traverse()
print(s.size())
s.traverse()

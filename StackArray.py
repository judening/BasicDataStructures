class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return not self.items

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         # can do: return self.items[-1]
         # also, will throw if empty
         return self.items[len(self.items)-1]

     def __len__(self):
         return len(self.items)

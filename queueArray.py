class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

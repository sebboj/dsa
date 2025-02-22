from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError('Queue is empty -- e m p t y -- e  m  p  t  y')

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError('Queue is empty -- e m p t y -- e  m  p  t  y')

    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    cool_queue = Queue()
    print(cool_queue)
    cool_queue.enqueue('S')
    cool_queue.enqueue('E')
    cool_queue.enqueue('B')
    print(cool_queue)
    print(cool_queue.dequeue())
    print(cool_queue.peek())
    print(cool_queue)

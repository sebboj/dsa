class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError('Stack is empty -- e m p t y -- e  m  p  t  y')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError('Stack is empty -- e m p t y -- e  m  p  t  y')

    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    cool_stack = Stack()
    print(cool_stack)
    cool_stack.push(1)
    cool_stack.push(2)
    cool_stack.push(3)
    print(cool_stack)
    print(cool_stack.pop())
    print(cool_stack.peek())
    print(cool_stack)
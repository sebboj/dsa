class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_to_end(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def __str__(self):
        out = ''
        curr_node = self.head
        while curr_node:
            out += str(curr_node.value) + ' '
            curr_node = curr_node.next
        return out

if __name__ == '__main__':
    cool_list = LinkedList()
    cool_list.insert_to_end(6)
    cool_list.insert_to_end(6)
    cool_list.insert_to_end(6)
    print(cool_list)

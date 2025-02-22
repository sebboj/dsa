# min binary heap implementation
# with index hash table to improve remove from O(n) to O(logn)

from sortedcontainers import SortedSet

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.length = 0
        self.indx_table = {} # for O(logn) removal

    def swap(self, indx1, indx2):
        '''
        SWAP FUNCTION IS WORKING FINE THE PROBLEM HAPPENS SOMEWHERE IN REMOVE FUNCTION
        THE SET SHOULD NOT BE EMPTY
        '''
        # print(self.indx_table[self.heap[indx1]], self.indx_table[self.heap[indx2]])

        val1 = self.heap[indx1]
        val2 = self.heap[indx2]
        print(val1, val2)
        print(indx1, indx2)

        print(self.indx_table[val1], self.indx_table[val2])
        print(self.heap)

        self.indx_table[val1].remove(indx1)
        self.indx_table[val2].remove(indx2)

        self.indx_table[val1].add(indx2)
        self.indx_table[val2].add(indx1)

        temp = self.heap[indx1]
        self.heap[indx1] = self.heap[indx2]
        self.heap[indx2] = temp

        print(self.indx_table[val1], self.indx_table[val2])
        print(self.heap)


    def bubble_up(self, indx):
        curr_indx = indx
        curr_parent_indx = (curr_indx - 1) // 2

        while curr_indx > 0 and self.heap[curr_parent_indx] > self.heap[curr_indx]:
            self.swap(curr_parent_indx, curr_indx)
            curr_indx = curr_parent_indx
            curr_parent_indx = (curr_indx - 1) // 2

        return curr_indx

    def sink(self, indx):
        curr_indx = indx
        curr_left_child_indx = curr_indx * 2 + 1
        curr_right_child_indx = curr_indx * 2 + 2

        while (curr_left_child_indx < self.length and self.heap[curr_indx] > self.heap[curr_left_child_indx]) or \
                (curr_right_child_indx < self.length and self.heap[curr_indx] > self.heap[curr_right_child_indx]):

            if curr_right_child_indx < self.length and \
                    self.heap[curr_left_child_indx] > self.heap[curr_right_child_indx]:
                # swap curr with right child
                self.swap(curr_indx, curr_right_child_indx)
                curr_indx = curr_right_child_indx
            else:
                # swap curr with left child
                self.swap(curr_indx, curr_left_child_indx)
                curr_indx = curr_left_child_indx

            curr_left_child_indx = curr_indx * 2 + 1
            curr_right_child_indx = curr_indx * 2 + 2

    def insert(self, n):
        self.heap.append(n)
        self.length += 1
        curr_indx = self.length - 1

        if n not in self.indx_table:
            self.indx_table[n] = SortedSet()
        self.indx_table[n].add(curr_indx)
        self.bubble_up(curr_indx)

    # remove by value, currently O(n)
    # use hash table for O(logn) removal
    # returns True if successful
    def remove(self, n):
        if not self.indx_table[n]:
            print(f'remove error: cannot find {n} in heap')
            return None

        indx = self.indx_table[n][0]

        # print(self.indx_table[self.heap[indx]])
        self.swap(indx, self.length - 1)
        self.indx_table[self.heap[indx]].remove(indx)
        # print(self.indx_table[self.heap[indx]])
        if len(self.indx_table[self.heap[indx]]) == 0:
            self.indx_table.pop(self.heap[self.length - 1])
        self.heap.pop()
        self.length -= 1
        if indx > 0 and self.heap[indx] < self.heap[(indx - 1) // 2]:
            self.bubble_up(indx)
        else:
            self.sink(indx)
        return n

    # remove root
    def poll(self):
        if self.length > 0:
            return self.remove(self.heap[0])
        return None

    # get min
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def __str__(self):
        return str(self.heap)

if __name__ == "__main__":
    cool_pq = PriorityQueue()
    cool_pq.insert(10)
    cool_pq.insert(19)
    cool_pq.insert(13)
    cool_pq.insert(14)
    cool_pq.insert(7)
    cool_pq.insert(11)
    cool_pq.insert(12)
    cool_pq.insert(13)
    cool_pq.insert(4)
    cool_pq.insert(12)
    cool_pq.insert(6)
    cool_pq.insert(8)
    cool_pq.insert(1)
    cool_pq.insert(5)
    cool_pq.insert(0)
    print(cool_pq)
    cool_pq.remove(12)
    print(cool_pq)
    print(cool_pq.poll())

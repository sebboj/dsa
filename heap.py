import heapq

'''
heapq creates a minheap by default
to have a maxheap negate d element when adding and negate when removing
'''

if __name__ == '__main__':
    cool_heap = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    heapq.heapify(cool_heap)

    print(cool_heap)

    heapq.heappush(cool_heap, 0)
    print(cool_heap)

    min_element = heapq.heappop(cool_heap)
    print(min_element)
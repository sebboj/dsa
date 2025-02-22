class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    # returns parent
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # basically parent(find(x)) = find(y)
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        # determine old and new parents
        old_p = y_root
        new_p = x_root
        if self.rank[x_root] < self.rank[y_root]:
            old_p = x_root
            new_p = y_root
        elif self.rank[y_root] == self.rank[x_root]:
            self.rank[x_root] += 1

        # update parents of applicable nodes from old to new
        for p in range(len(self.parent)):
            if self.parent[p] == old_p:
                self.parent[p] = new_p

def countComponents(n, edges):
    cool_disjoint_set = DisjointSet(n)
    for x, y in edges:
        cool_disjoint_set.union(x, y)
    unique_parents = set()
    for p in cool_disjoint_set.parent:
        unique_parents.add(p)

    return len(unique_parents)

if __name__ == '__main__':
    print(countComponents(6, [[0,1],[2,3],[4,5],[1,2],[3,4]])) # expected: 1
    print(countComponents(6, [[0,1],[1,2],[2,3],[4,5]])) # expected: 2
    print(countComponents(3, [[0,1],[0,2]])) # expected: 1

    cool_set = DisjointSet(7)

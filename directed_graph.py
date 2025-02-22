'''
AKA: Directed Adjacency List
'''

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append(end)
        if end not in self.graph:
            self.graph[end] = []

    def display(self):
        for vertex in self.graph:
            if self.graph[vertex]:
                print(vertex,'->',' -> '.join(str(x) for x in self.graph[vertex]))
            else:
                print(vertex)

if __name__ == '__main__':
    cool_graph = DirectedGraph()
    cool_graph.add_edge(0,1)
    cool_graph.add_edge(0,2)
    cool_graph.add_edge(1,2)
    cool_graph.add_edge(2,0)
    cool_graph.add_edge(2,3)
    cool_graph.display()
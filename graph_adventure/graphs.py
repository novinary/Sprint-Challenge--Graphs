class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

newQueue = Queue()
newQueue.enqueue(1)

print(newQueue.queue)

newStack = Stack()
newStack.push(1)
newStack.pop()

print(newStack.stack)

class Graph():
    def __init__(self):
        self.vertices = {}
    def add_vertices(self, vertex):
        self.vertices[vertex] = set()
    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def dft_r(self, start_vert, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vert)
        print(start_vert)
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                self.dft_r(child_vert, visited)
    def dft(self, starting_vertex_id):
        stack = Stack()
        stack.push(starting_vertex_id)
        visited = set()
        while stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.vertices[v]:
                    stack.push(next_vert)
    
    

newGraph = Graph()
newGraph.add_vertices(1)
newGraph.add_vertices(2)
newGraph.add_edges(1,2)
newGraph.add_directed_edge(1,2)

print(newGraph.vertices)

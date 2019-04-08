"""
Simple graph implementation
"""
import queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
	    self.vertices = {}
    def add_vertex(self, vertex_id):
	    self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
	    if v1 in self.vertices and v2 in self.vertices:
		    self.vertices[v1].add(v2)
		    self.vertices[v2].add(v1)
	    else:
		    raise IndexError("That vertex does not exist")
    def add_directed_edge(self, v1, v2):
	    if v1 in self.vertices and v2 in self.vertices:
		    self.vertices[v1].add(v2)
	    else:
		    raise IndexError("That vertex does not exist")

# Implement the queue, and enque the starting Vertex ID
    def bft(self, starting_vertex_id):
    # Create and empty queue
        q = queue.Queue()
        q.put(starting_vertex_id)
    # Create a set to store vertices
        visited = set()
    # While the queue is not empty"
        while q.qsize() > 0:
    # Dequeue the first vertex
            v = q.get()
    # If that vertex has not been visited:
        # Mark it as visited
            print(v)
            visited.add(v)
        # Add all of its neighbors to the back of the queue
            for next_vert in self.vertices[v]:
                q.put(next_vert)

    def dft(self, starting_vertex_id):
    # Create an empty stack
        s = queue.LifoQueue()
        s.put(starting_vertex_id)
    # Create a set to store vertices
        visited = set()
    # While the stack is not empty"
        while s.qsize() > 0:
    # Pop the first vertex
            v = s.get()
    # If that vertex has not been visited:
        # Mark it as visited
            print(v)
            visited.add(v)
        # Add all of its neighbors to the top of the stack
            for next_vert in self.vertices[v]:
                s.put(next_vert)

#BFS returning shortest path:
	# Instead of storing each vertex in the queue, store the PATH to that vertex
	# When you dequeue, look at the last node
	# When you enqueue, copy the path and append the neighbor node and enqueue the new path
class Queue:
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


class Stack:
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


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2.
        """
        # Check if they exist first
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print("Error adding edge: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while queue.size() > 0:
            # dequeue/pop first vertex
            path = queue.dequeue()
            node = path[-1]
            # if not visited
            if node not in visited:
                # DO THE THING
                print(node)
                # Mark as visited
                visited.add(node)
                # Enqueue all neighbors
                for next_vert in self.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack and push starting_vertex onto stack
        stack = Stack()
        stack.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # while stack is not empty:
        while stack.size() > 0:
            # Pop last vertex
            path = stack.pop()
            topNode = path[-1]

            if topNode not in visited:
                # DO THE THING
                print(topNode)
                # Mark as visited
                visited.add(topNode)
                # Enqueue all neighbors
                for next_vert in self.get_neighbors(topNode):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initial case
        if visited is None:
            visited = set()
        # Base case: How do we know we're done?
        # We're done when we have no more neighbors

        # Track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)

        # Call the function recursively - on neighbors Not Visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)
                # If a node has no unvisited neighbors <- This is our base case!

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create a queue and enqueue starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while queue.size() > 0:
            # dequeue/pop first vertex
            path = queue.dequeue()
            node = path[-1]
            # if not visited
            if node not in visited:
                # DO THE THING
                if node == destination_vertex:
                    return path
                # Mark as visited
                visited.add(node)
                # Enqueue all neighbors
                for next_vert in self.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack and push starting_vertex onto stack
        stack = Stack()
        stack.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # while stack is not empty:
        while stack.size() > 0:
            # Pop last vertex
            path = stack.pop()
            topNode = path[-1]

            if topNode not in visited:
                # DO THE THING
                if topNode == destination_vertex:
                    return path
                # Mark as visited
                visited.add(topNode)
                # Enqueue all neighbors
                for next_vert in self.get_neighbors(topNode):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initial case
        if visited is None:
            visited = set()

        if path is None:
            path = []
        # Base case: How do we know we're done?
        # We're done when we have no more neighbors

        # Track visited nodes
        visited.add(starting_vertex)
        newPath = path + [starting_vertex]

        # DO THE THING
        if starting_vertex == destination_vertex:
            return newPath

        # Call the function recursively - on neighbors Not Visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                neighborPath = self.dfs_recursive(neighbor, destination_vertex, visited, newPath)
                if neighborPath:
                    return neighborPath
                # If a node has no unvisited neighbors <- This is our base case!

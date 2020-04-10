import json
from collections import namedtuple

class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to

def floyd_warshall(g):
    """Return dictionaries distance and next_v.
 
    distance[u][v] is the shortest distance from vertex u to v.
    next_v[u][v] is the next vertex after vertex v in the shortest path from u
    to v. It is None if there is no path between them. next_v[u][u] should be
    None for all u.
 
    g is a Graph object which can have negative edge weights.
    """
    distance = {v:dict.fromkeys(g, float('inf')) for v in g}
    next_v = {v:dict.fromkeys(g, None) for v in g}
 
    for v in g:
        for n in v.get_neighbours():
            distance[v][n] = v.get_weight(n)
            next_v[v][n] = n
 
    for v in g:
         distance[v][v] = 0
         next_v[v][v] = None
 
    for p in g: 
        for v in g:
            for w in g:
                if distance[v][w] > distance[v][p] + distance[p][w]:
                    distance[v][w] = distance[v][p] + distance[p][w]
                    next_v[v][w] = next_v[v][p]
 
    return distance, next_v

matrix = """
[
  {
    "inicio": "1",
    "fim": "2",
    "weight": "3"
  },
  {
    "inicio": "1",
    "fim": "4",
    "weight": "5"
  },
  {
    "inicio": "2",
    "fim": "1",
    "weight": "2"
  },
  {
    "inicio": "2",
    "fim": "4",
    "weight": "4"
  },
  {
    "inicio": "3",
    "fim": "2",
    "weight": "1"
  },
  {
    "inicio": "4",
    "fim": "3",
    "weight": "2"
  }
]"""

g = Graph()
x = json.loads(matrix, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
for i in x:
    key1 = int(i.inicio)
    key2 = int(i.fim)
    key3 = int(i.weight)
    if key1 not in g:
        g.add_vertex(key1)
    if key2 not in g:
        g.add_vertex(key2)
    if not g.does_edge_exist(key1, key2):
        g.add_edge(key1, key2, key3)
 
distance, next_v = floyd_warshall(g)

print("Distance between 1 and 4: ")
for start in g:
    if start.get_key() == 1:
        for end in g:
            if end.get_key() == 4:
                if next_v[start][end]:
                    print(distance[start][end])
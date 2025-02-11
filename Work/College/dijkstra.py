from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        # Using defaultdict to store the graph as an adjacency list
        self.graph = defaultdict(list)
        
    def add_edge(self, src, dest, weight):
        # Add edges with weights to the graph
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))  # For undirected graph
        
    def dijkstra(self, src, dest):
        # Initialize distances dictionary with infinity for all vertices
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[src] = 0
        
        # Dictionary to store the previous vertex in the shortest path
        previous = {vertex: None for vertex in self.graph}
        
        # Priority queue to store vertices and their distances
        pq = [(0, src)]
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            # If we've found destination, we can stop
            if current_vertex == dest:
                break
                
            # If we've found a longer path, skip
            if current_distance > distances[current_vertex]:
                continue
                
            # Check all neighbors of current vertex
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                # If we've found a shorter path, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
                    
        return distances[dest], self._get_path(previous, src, dest)
        
    def _get_path(self, previous, src, dest):
        path = []
        current = dest
        
        while current is not None:
            path.append(current)
            current = previous[current]
            
        return path[::-1]  # Reverse path to get source to destination

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    
    # Add edges (source, destination, weight)
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    
    # Find shortest path from 'A' to 'E'
    shortest_distance, path = g.dijkstra('A', 'E')
    
    print(f"Shortest distance from A to E: {shortest_distance}")
    print(f"Shortest path: {' -> '.join(path)}")


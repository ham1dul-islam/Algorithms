import networkx as nx
import matplotlib.pyplot as plt

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Recursive DFS
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Iterative DFS
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))  # Reverse to maintain order

# Visualizing the graph
def draw_graph(graph):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    plt.figure(figsize=(5, 5))
    pos = nx.spring_layout(G)  # Layout for better visualization
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=14)
    plt.show()

def main():
    # Run DFS
    print("Recursive DFS Traversal:")
    dfs_recursive(graph, 'A')

    print("\nIterative DFS Traversal:")
    dfs_iterative(graph, 'A')

    # Draw the graph
    draw_graph(graph)

if __name__ == "__main__":
    main()

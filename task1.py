import networkx as nx 
import matplotlib.pyplot as plt 


G = nx.Graph()

G.add_edge('Tree', 'Bat', weight=5)
G.add_edge('Tree', 'Bird', weight=10)
G.add_edge('Tree', 'Beetle', weight=3)
G.add_edge('Beetle', 'Grass', weight=2)
G.add_edge('Beetle', 'Bird', weight=4)
G.add_edge('Bird', 'Grass', weight=7)

pos = nx.spring_layout(G)

options = {
    "node_color": "teal",
    "edge_color": "lightgray",
    "node_size": 2100,
    "font_size": 14,
    "width": 2,
    "with_labels": True
}
nx.draw(G,pos,  **options)

labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Взаємодія  між різними видами в екосистемі')

num_of_nodes = G.number_of_nodes()
num_of_edges = G.number_of_edges()
is_connected = nx.is_connected(G)
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
path = nx.shortest_path(G, source='Tree', target='Grass')
avg_path_lentgh = nx.average_shortest_path_length(G)

if __name__ == '__main__':
    plt.show()
    
    print('\nВзаємодія  між різними видами в екосистемі:\n')
    print(f"Number of Nodes: {num_of_nodes}")
    print(f"Number of Edges: {num_of_edges}\n")
    print("Degree centrality:")
    print(degree_centrality)
    print("\nCloseness centrality:")
    print(closeness_centrality)
    print("\n Betweenness centrality:")
    print(betweenness_centrality)
    print("\n Shortest path from Tree to Grass:")
    print(path)
    print(f"\n Average shortest path length: {avg_path_lentgh}")
    
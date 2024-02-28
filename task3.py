import networkx as nx 
from task1 import G

all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

print(f"| {'Shortest path from->to':<30} | {'Path':<30} | {'Distance':<30} |")
print(f"| {'-'*30} | {'-'*30} | {'-'*30} |")

for source in G.nodes:

    for target, path in all_shortest_paths[source].items():
        if source != target:
            distance = nx.dijkstra_path_length(G, source=source, target=target)
            
            print(f"| {f'{source} ->  {target}':<30} | {', '.join(path):<30} | {distance:<30} |")

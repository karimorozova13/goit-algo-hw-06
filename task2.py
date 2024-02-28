import networkx as nx 
from task1 import G

bfs_tree  = nx.bfs_tree(G, source='Tree')
print(bfs_tree.edges())

dfs_tree  = nx.dfs_tree(G, source='Tree')
print(dfs_tree.edges())

# find explanation in the conclusions.md file

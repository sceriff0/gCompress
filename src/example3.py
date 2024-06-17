import networkx as nx
import matplotlib.pyplot as plt
import compression

seed = 0
G = nx.powerlaw_cluster_graph(1000,4,0.25,seed=seed)

G = compression.redundantVertexElimination(G,commonNeighbors=5)
nodesToKeep = compression.betaWeight(G,10,10)
compressedG = compression.keepAll(G,nodesToKeep)

pos = nx.spring_layout(G,seed=seed)
options = {
    'node_color': 'r',
    'node_size': 500,
}

subax1 = plt.subplot(121)
nx.draw(G,pos=pos)
nx.draw_networkx_nodes(G,pos=pos,nodelist=nodesToKeep,**options)

subax2 = plt.subplot(122)
nx.draw(compressedG,pos=pos)
nx.draw_networkx_nodes(compressedG,pos=pos,nodelist=nodesToKeep,**options)

plt.show()
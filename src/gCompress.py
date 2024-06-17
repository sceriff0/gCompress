try:
    import networkx as nx
except ModuleNotFoundError:
    print("module 'networkX' is not installed")
    quit()

import compression
import utils

args = utils.parseArgs()

G = nx.read_edgelist(args.graph)
nodes = args.nodes
beta = args.beta
merge = args.merge
gCompressFile = args.out

if merge:
  G = compression.redundantVertexElimination(G,commonNeighbors=merge)

nodesToKeep = compression.betaWeight(G,nodes,beta)
compressedG = compression.keepAll(G,nodesToKeep)

nx.write_edgelist(compressedG,gCompressFile)

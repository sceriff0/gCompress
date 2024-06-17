import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import compression
import utils

seed = 0
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

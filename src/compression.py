import networkx as nx
import numpy as np
import itertools

def redundantVertexElimination(G, commonNeighbors = 10) -> nx.Graph:
  
  """
  This function merges nodes that have a minimum number of common neighbors

  Args:
      G (nx.Graph): the graph we want to merge the nodes of.
      commonNeighbors (int, optional):  the minimum number of neighbors that two nodes need to share to be merged. Defaults to 10.
      outputFile (str, optional): the file where to write the nodes that have been merged.

  Returns:
      nx.Graph: the graph created from the merge of nodes of G.
  """

  
  reducedG = G
  out = open("merge.txt", "w")

  adjMat = nx.to_pandas_adjacency(G)
  twoHopMat = np.linalg.matrix_power(adjMat,n=2) ## This matrix gives me all nodes two nodes apart
  upperIndices = np.triu_indices_from(twoHopMat,k=1) ## I only need upper diagonal

  vertexToMerge = []

  for i in range(twoHopMat.shape[0]):
    for j in range(i+1, twoHopMat.shape[0]):

      u = list(G)[i]
      v = list(G)[j]

      if len(list(nx.common_neighbors(G,u,v))) >= commonNeighbors: ## I find all nodes with at least common neighbors
        if(u not in vertexToMerge and v not in vertexToMerge):

          vertexToMerge.append(u)
          vertexToMerge.append(v)

  for (u,v) in zip(vertexToMerge[0::2], vertexToMerge[1::2]):

    reducedG = nx.contracted_nodes(reducedG,u,v) ## I merge the found nodes
    out.write("Merged nodes: " + str(u) + " and " + str(v) + "\n")

  out.close()

  return reducedG

def betaWeight(G: nx.Graph, importantNumber: int = 20, beta: float = 1.) -> list:

  """
  This function returns a list of nodes to keep in the final graph based on weights computed  based on their local neighborhood

  Args:
      G (nx.Graph): the graph containing the nodes to keep.
      importantNumber (int, optional):  the number of nodes to keep. Defaults to 20.
      beta (int, optional):  the weight that considers more the neighborhood. Defaults to 1.

  Returns:
      list: the list of nodes that will be kept in the final graph.
  """
  
  numberOfNodes = len(list(G))
  importantNodes = np.zeros((numberOfNodes,), dtype='f,object')
  index = 0

  for nodeV in list(G): # In this cycle I compute the score of each node as in the paper.

    neighborhood = list(G.neighbors(nodeV))
    numberOfNeighbors = len(list(neighborhood))
    
    degreeV = G.degree(nodeV)
    weight = 0

    for nodeU in neighborhood:

      degreeU = G.degree(nodeU)
      if (degreeU <= beta * degreeV):

        weight += 1

    weight /= numberOfNeighbors
    importantNodes[index] = (weight,nodeV)
    index += 1
  
  importantNodes.sort()
  importantNodes = [nodeWeight[1] for nodeWeight in importantNodes] # Here I take only the specified number of nodes with highest score

  return set(importantNodes[-importantNumber:])

def keepAll(G: nx.Graph, importantNodes: set) -> nx.Graph:

  """
  This function computes the nodes on the shortest paths between chosen nodes, so to have a compressed representation of a graph

  Args:
      G (nx.Graph): the graph we want to compress.
     importantNodes (set):  the set of nodes used to compute the compression of the graph.

  Returns:
      nx.Graph: the graph created from the compression of G.
  """
  
  connectingNodes = set()
  nodePairs = itertools.combinations(importantNodes,2)
  
  for nodePair in nodePairs:

    try:
      connectingNodes = connectingNodes.union(nx.shortest_path(G,nodePair[0],nodePair[1])[1:-1]) # Here I connect all important nodes to build a connected graph if possible
    except:
      continue
    
  nodesToKeep = importantNodes.union(connectingNodes)

  possibleEdges = set(itertools.combinations(nodesToKeep,2))
  actualEdges = set(G.edges())

  compressedG = nx.Graph(possibleEdges & actualEdges)

  return compressedG


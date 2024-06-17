# gCompress
## Scientific Programming Project (Python)

### This script may be used to compress a graph provided in _edgelist_ format.

### It is based on: Gilbert and Levchenko: “Compressing Network Graphs”. 

### Graphs from StringDB may be compressed but the header has to be manually removed.

### Two example files: example1.py and example2.py are provided which just need to be run. They display the same graph compressed with different parameters. In particula the second one has a higher parameter n of nodes that will be kept for sure and a higher beta which will increase the importance of the local neighborhood.

### To run the script just do:
```
python gCompress.py <graphFile.txt> -n <nodeToKeep> -b <betaParameter> -m <mergeParameter> -o <outFile>
```

### Where

__n__ is the number of nodes that will be kept and connected if possible.

__b__ is the parameter that influences the chosen n nodes.

__m__ is the paramenter that control wether to perform node merging of nodes with at least m neighbors. This is pretty slow.

__o__ is the file where the compressed graph will be written in output format.

### If m is specified a file merge.txt will be generated that contains info on the merged nodes.

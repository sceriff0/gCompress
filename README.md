# gCompress
## Scientific Programming Project (Python)

### This script may be used to compress a graph provided in _edgelist_ format.

### It is based on: Gilbert and Levchenko: “Compressing Network Graphs”. 

### Graphs from StringDB may be compressed but the header has to be manually removed.

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

### Three example files: example1.py, example2.py and example3.py are provided which just need to be run. 

### They will apply the same functions as the gCompress script but with fixed parameters and graph.

### At the end they will display the full and the compressed graph near each other with "important" nodes highlighted in red.

### The examples show how different values of beta impact the chosen nodes.
### Examples 1 to 3 have increasingly higher values of beta and show that the "important" nodes are chosen further away from the center.

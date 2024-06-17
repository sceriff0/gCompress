# gCompress
## Scientific Programming Project (Python)

### This script may be used to compress a graph provided in _edgelist_ format.

### Two example files: example1.py and example2.py are provided which just need to be run. They display the same graph compressed with different parameters. In particula the second one has a higher parameter n of nodes that will be kept for sure and a higher beta which will increase the importance of the local neighborhood.

### To run the script just do:
```
python main.py <graphFile.txt> -n <nodeToKeep> -b <betaParameter> -m <mergeParameter> -o <outFile>
```

### Where

n is the number of nodes that will be kept and connected if possible.


b is the parameter that influences the chosen n nodes.

m is the paramenter that control wether to perform node merging of nodes with at least m neighbors. This is pretty slow.

o is the file where the compressed graph will be written in output format.

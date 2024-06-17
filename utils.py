import argparse

def parseArgs() -> argparse.Namespace:

  """
  This function is used the read the arguments from command line.

  Returns:
      argparse.Namespace: the object cointaining the arguments.
  """
  parser = argparse.ArgumentParser( 
                    prog='gCompress',
                    description='A program to compress your graph :)')
  
  parser.add_argument('graph', type=str)           
  parser.add_argument('-n', '--nodes', type=int, help= "The number of core nodes that will be kept")     
  parser.add_argument('-b', '--beta',  type=int, help= "Higher beta gives more important to the local structure of the graph")
  parser.add_argument('-m', '--merge', type=int, default=0, help= "Vertexes with more common neighbors than the value will be merged if specified")
  parser.add_argument('-o', '--out', type=str, default="gCompress.txt", help= "The file with the compressed graph")

  args = parser.parse_args()

  return args
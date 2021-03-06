import pydotplus
import sys

#graph = pydotplus.graph_from_dot_file('file.dot')
graph = pydotplus.graph_from_dot_file(sys.argv[1])
#print(graph.to_string(),"\n")
f = open(sys.argv[2]) #list of node requirements in CSV format
for line in f:
    print(line.split(","))
for node in graph.get_nodes():
    print(node.get_name())
    print(node.to_string(),"\n")   


for edge in graph.get_edges():
    print(edge.get_source() , " Is the source")
    print(edge.get_destination() ," Is the destination", "\n")
    
import pydotplus
import sys
class ParallelNode(pydotplus.Node):
    def __init__(self,node,time,nodesNecessary,sources):
        pydotplus.Node.__init__(self,node.get_name(),node.obj_dict)
        self.timeNeeded = time
        self.isFinished = False
        self.nodesNecessary = nodesNecessary
        self.sources = sources
        #self.destinations = destinations


def initializeNodes(graph,requirements):
    nodes = []
    for node in graph.get_nodes():
        for line in requirements:
            splitLine = line.split(",")
            if (splitLine[0] == node.get_name()):
                sources = getSources(graph,node)
                #destinations = get_destinations(node,graph)
                newNode = ParallelNode(node,splitLine[1],splitLine[2],sources)
                nodes.append(newNode)
                break
    return nodes
def getSources(graph,node):
    sources = []
    edges = graph.get_edges()
    for edge in edges:
        if (edge.get_destination() == node.get_name()):
            sources.append(edge.get_source())
    return sources   

graph = pydotplus.graph_from_dot_file(sys.argv[1])
requirements = open(sys.argv[2],"r")

nodes = initializeNodes(graph,requirements)
    
for node in nodes:
    print(node.get_name())
    print(node.timeNeeded)
    print(node.nodesNecessary)
    if node.sources:
        print (node.get_name(),"'s sources are",node.sources)
    else:
        print (node.get_name()," has no sources")
requirements.close()
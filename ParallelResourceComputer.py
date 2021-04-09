import pydotplus
import sys
from itertools import combinations
class ParallelNode(pydotplus.Node):
    def __init__(self,node,nodesNecessary,time):
        pydotplus.Node.__init__(self,node.get_name(),node.obj_dict)
        self.timeNeeded = int(time)
        self.isFinished = False
        self.nodesNecessary = int(nodesNecessary)
        self.sources = []
        #self.destinations = destinations
    def setSources(self,sources):
        self.sources = sources


def initializeNodes(graph,requirements):
    nodes = []
    for node in graph.get_nodes():
        for line in requirements:
            splitLine = line.split(",")
            if (splitLine[0] == node.get_name()):
                #sources = getSources(graph,node)
                #destinations = get_destinations(node,graph)
                newNode = ParallelNode(node,splitLine[1],splitLine[2])
                nodes.append(newNode)
                break
    return nodes
def getSources(nodeList,node):
    sources = []
    edges = graph.get_edges()
    for edge in edges:
        if (edge.get_destination() == node.get_name()):
            for single in nodeList:
                if single.get_name() == edge.get_source():
                    sources.append(single)
    return sources   
def knapSack(waiting,nodesReady):
    timeMax = 0
    tempReady = []
    nodes = 0
    n = 0
    while(n != len(waiting)+1):
        comb = list(combinations(waiting,n))
        for nodeList in comb:
            nodesCount = 0
            timeCount = 0
            temp = []
            for node in nodeList:
                nodesCount += node.nodesNecessary
                timeCount += node.timeNeeded
                temp.append(node)
        if nodesCount <= nodesMax:
            if timeCount > timeMax:
                timeMax = timeCount
                tempReady = temp
                nodes = nodesCount
        n = n + 1
    return tempReady,nodes;
graph = pydotplus.graph_from_dot_file(sys.argv[1])
requirements = open(sys.argv[2],"r")

nodes = initializeNodes(graph,requirements)
for node in nodes:
    sources = getSources(nodes,node)
    node.setSources(sources)
requirements.close()    

running,ready,waiting,finished = [],[],[],[]
runtime = 0
for node in nodes:
    if not node.sources:
        waiting.append(node)

for node in nodes:
    for source in node.sources:
        print ("hello i am:",node.get_name(),"and my source is",source.get_name())
nodesMax = 8
nodesReady = nodesMax
tempReady,tempNodes = knapSack(waiting,nodesReady)
running.append(tempReady)
nodesReady -=tempNodes
while(running):
    runtime++
    for node in running:
        node.timeNeeded--
        if thing.timeNeeded == 0:
            running.remove(node)
            finished.append(node)
            node.isFinished = True
            nodesReady+=node.nodesNecessary
    for node in waiting:
        for source in node.sources:
            if not source.isFinished:
                #then its not done

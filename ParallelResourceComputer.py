import pydotplus
import sys
from itertools import combinations
class ParallelNode(pydotplus.Node):
    def __init__(self,node,nodesNecessary,time):
        pydotplus.Node.__init__(self,node.get_name(),node.obj_dict)
        self.timeNeeded = int(time)
        self.isFinished = False
        self.isReady = False
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

def knapSack(waitingList,nodesReady):
    timeMax = 0
    tempR = []
    nodes = 0
    n = 0
    while(n != len(waitingList)+1):
        comb = list(combinations(waitingList,n))
        for nodeList in comb:
            nodesCount = 0
            timeCount = 0
            temp = []
            for node in nodeList:
                nodesCount += node.nodesNecessary
                timeCount += node.timeNeeded
                temp.append(node)
        if nodesCount <= nodesReady:
            if timeCount > timeMax:
                timeMax = timeCount
                tempR = temp
                nodes = nodesCount
        n = n + 1
    return tempR,nodes;
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
        node.isReady = True
        ready.append(node)
    else:
        waiting.append(node)

nodesMax = 8
nodesReady = nodesMax
tempReady,tempNodes = knapSack(ready,nodesReady)
for node in tempReady:
    ready.remove(node)
running.extend(tempReady)
nodesReady -=tempNodes
while(running):
    tempReady = []
    tempNodes = 0
    runtime+=1
    for node in running:
        node.timeNeeded-=1
        if node.timeNeeded == 0:
            print("Node:",node.get_name(),"Finished Current time: ",runtime)
            finished.append(node)
            node.isFinished = True
            nodesReady+=node.nodesNecessary
            #sys.exit()
    running = [node for node in running if node not in finished]
    for node in waiting:
        node.isReady = True
        for source in node.sources:
            if not source.isFinished:
                node.isReady = False
                break
        if node.isReady:
            ready.append(node)
    waiting = [node for node in waiting if node not in ready]
    if ready:
        tempReady,tempNodes = knapSack(ready,nodesReady)
        for node in tempReady:
            ready.remove(node)
        running.extend(tempReady)
        nodesReady-=tempNodes
    #for node in running:
    #    print ("Currently running:",node.get_name(),"with time",node.timeNeeded,"left")
print("Total uptime: ",runtime)
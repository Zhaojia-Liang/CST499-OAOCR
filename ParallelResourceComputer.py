import pydotplus
import sys
import datetime
from itertools import combinations


class ParallelNode(pydotplus.Node):
    def __init__(self,node,nodesNecessary,time):
        pydotplus.Node.__init__(self,node.get_name(),node.obj_dict)
        self.timeNeeded = int(time)
        self.isFinished = False
        self.isReady = False
        self.nodesNecessary = int(nodesNecessary)
        self.sources = []
        self.originalTime = int(time)
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
                ISOtime = parse_isoduration(splitLine[2])
                newNode = ParallelNode(node,splitLine[1],ISOtime)
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
def get_isosplit(s,split):
    if split in s:
        n, s = s.split(split)
    else:
        n = 0
    return n, s
def parse_isoduration(s):
    s = s.split('P')[-1]
    days, s = get_isosplit(s, 'D')
    _, s = get_isosplit(s, 'T')
    hours, s = get_isosplit(s, 'H')
    minutes, s = get_isosplit(s, 'M')
    seconds, s = get_isosplit(s, 'S')
    
    dt = datetime.timedelta(days = int(days), hours = int(hours), minutes = int(minutes), seconds = int(seconds))
    return int(dt.total_seconds())
def knapSack(waitingList,nodesReady):
    timeMax = 0
    tempR = []
    nodess = 0
    n = 0
    while(n != len(waitingList)+1):
        #print("in loop")
        comb = list(combinations(waitingList,n))
        for nodeL in comb:
            nodesCount = 0
            timeCount = 0
            temp = []
            for node in nodeL:
                nodesCount += node.nodesNecessary
                timeCount += node.timeNeeded
                temp.append(node)
        #print(nodesCount)
        #print(timeCount)
        if nodesCount <= nodesReady:
            if timeCount > timeMax:
                timeMax = timeCount
                tempR = temp
                nodess = nodesCount
        n = n + 1
    return tempR,nodess;
def workFlowSimulator(nodeList,nodeAmount):
    #print (nodeAmount)
    #print(len(nodeList))
    running,ready,waiting,finished = [],[],[],[]
    efficiency = []
    runtime = 0
    for node in nodeList:
        if not node.sources:
            node.isReady = True
            ready.append(node)
        else:
            waiting.append(node)
    #for node in nodeList:
        #print(node.get_name(),node.nodesNecessary)
        #print(node.get_name(),node.timeNeeded)
    #for node in ready:
    #    print(node.get_name(),node.nodesNecessary)
    nodesReady = nodeAmount
    tempReady,tempNodes = knapSack(ready,nodesReady)
    for node in tempReady:
        ready.remove(node)
    running.extend(tempReady)
    nodesReady -=tempNodes
    #for node in ready:
    #    print(node.get_name(),node.nodesNecessary)
    #for node in nodeList:
    #    print(node.get_name(),node.nodesNecessary)
    #for node in waiting:
    #    print(node.get_name(),node.nodesNecessary)
    #if(running):
    #    print("Running list is True")
    #print(len(running))
    #print(str(any(running)))
        
    while(running):
        tempReady = []
        tempNodes = 0
        #print((nodeAmount-nodesReady)/nodeAmount)
        efficiency.append((nodeAmount-nodesReady)/nodeAmount)
        runtime+=1
        for node in running:
            node.timeNeeded-=1
            if node.timeNeeded == 0:
                #print("Node:",node.get_name(),"Finished Current time: ",runtime)
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
        #print(nodesReady)
        #print(nodeAmount)
    #print("Total uptime: ",runtime)
    #print("Average Efficency: ",round((sum(efficiency)/runtime)*100,2),"%")
    for node in finished:
        node.isFinished = False
        node.isReady = False
        node.timeNeeded = node.originalTime
    return round((sum(efficiency)/runtime)*100,2),runtime,nodeAmount

graph = pydotplus.graph_from_dot_file(sys.argv[1])
requirements = open(sys.argv[2],"r")

nodes = initializeNodes(graph,requirements)
nodesMax = 0
nodeMin = nodes[0].nodesNecessary
GraphPoints = []
for node in nodes:
    if node.nodesNecessary > nodeMin:
        nodeMin = node.nodesNecessary
    nodesMax += node.nodesNecessary
    sources = getSources(nodes,node)
    node.setSources(sources)
requirements.close()
#workFlowSimulator(nodes,10) ' 
for x in range(nodeMin,nodesMax+1):
    tup = ()
    tup = tuple(workFlowSimulator(nodes,x))
    GraphPoints.append(tup)
for point in GraphPoints:
    print("Amount of Nodes",point[2])
    print("Runtime",point[1])
    print("Average efficiency: ", point[0])
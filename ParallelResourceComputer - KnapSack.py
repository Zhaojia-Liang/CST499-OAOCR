# import pydotplus
# import sys
# class ParallelNode(pydotplus.Node):
#     def __init__(self,node,time,nodesNecessary):
#         pydotplus.Node.__init__(self,node.get_name(),node.obj_dict)
#         self.timeNeeded = time
#         self.isFinished = False
#         self.nodesNecessary = nodesNecessary
# graph = pydotplus.graph_from_dot_file(sys.argv[1])
# nodes = []
# for node in graph.get_nodes():
    
# node1 = ParallelNode(graph.get_nodes()[3],4,8)

# print (node1.get_name())
# print (node1.timeNeeded)
# print (node1.isFinished)
# print (node1.nodesNecessary)


# DO the knapsack thing for now
# imagine A  B  C  D  E -> arrry arr[]
# Nodes:  5  3  2  3  2
# Time:   30 20 20 10 40
from itertools import combinations

class Node:
	def __init__(self, label, nodes, time):
		self.label = label
		self.nodes = nodes
		self.time = time

A = Node("A", 5, 30)
B = Node("B", 3, 20)
C = Node("C", 2, 20)
D = Node("D", 3, 10)
E = Node("E", 2, 40)

# A = Node(10, 60)
# B = Node(20, 100)
# C = Node(30, 120)

arr = [A, B, C, D, E]

# We have max 8 nodes, to complie the most finishing time that we can have

nodesMax = 8
timeMax = 0
str = ""

n = 0

# counter for selected nodes and 
while(n != len(arr)+1):
	comb = combinations(arr, n)

	for i in list(comb):
		nodesCount = 0
		timeCount = 0
		temp = ""
		for j in i:
			nodesCount += j.nodes
			timeCount += j.time
			temp += j.label
		if nodesCount <= nodesMax:
			if timeCount > timeMax:
				timeMax = timeCount
				str = temp

	n = n + 1

print(str, timeMax)
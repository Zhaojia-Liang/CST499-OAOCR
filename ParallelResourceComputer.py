import pydotplus
import sys
class ParallelNode(pydotplus.Node):
    def __init__(self,node,time,nodesNecessary):
        pydotplus.Node.__init__(self,node.get_name(),node.obj_dict)
        self.timeNeeded = time
        self.isFinished = False
        self.nodesNecessary = nodesNecessary
graph = pydotplus.graph_from_dot_file(sys.argv[1])

node1 = ParallelNode(graph.get_nodes()[0],4,8)

print (node1.get_name())
print (node1.timeNeeded)
print (node1.isFinished)
print (node1.nodesNecessary)
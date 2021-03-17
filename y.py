import pydot

graph = pydot.Dot('my_graph', graph_type='digraph')

A_node = pydot.Node('A')
B_node = pydot.Node('B')
C_node = pydot.Node('C')
D_node = pydot.Node('D')
E_node = pydot.Node('E')

graph.add_node(A_node)
graph.add_node(B_node)
graph.add_node(C_node)
graph.add_node(D_node)
graph.add_node(E_node)

First_edge = pydot.Edge('A', 'B')
Second_edge = pydot.Edge('A', 'C')
Third_edge = pydot.Edge('B', 'D')
Forth_edge = pydot.Edge('B', 'E')

graph.add_edge(First_edge)
graph.add_edge(Second_edge)
graph.add_edge(Third_edge)
graph.add_edge(Forth_edge)

graph.write_raw('Sample.dot')
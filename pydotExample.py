import pydot


graph = pydot.Dot('my_graph', graph_type = 'graph', bgcolor = 'yellow')

my_node = pydot.Node('a', label = 'foo')
graph.add_node(my_node)
graph.add_node(pydot.Node('b', shape='circle'))

my_edge = pydot.Edge('a','b',color = 'blue')
graph.add_edge(my_edge)
graph.write_raw('output.dot')
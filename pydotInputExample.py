import pydot

graphs = pydot.graph_from_dot_file('output.dot')
graph = graphs[0]

print(graph.get_graph_type)
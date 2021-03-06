import pydotplus as ptp

graph = ptp.Dot(graph_type='graph')
edges = [("A","B"), ("A","C"), ("B","D"), ("B","E"), ("C","E")]
nodes = [("A", "red"), ("B", "green"), ("C", "green"), ("D", "red"), ("E", "green")]
for e in edges:
    graph.add_edge(ptp.Edge(e[0], e[1]))
for n in nodes:
    node = ptp.Node(name=n[0], label= n[0], fillcolor=n[1], style="filled" )
    graph.add_node(node)
graph.write_dot("file.dot")
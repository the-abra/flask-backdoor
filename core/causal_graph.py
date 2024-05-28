import networkx as nx

def create_causal_graph(nodes, edges):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def check_backdoor_criterion(G, treatment, outcome):
    # Find all paths from treatment to outcome
    all_paths = list(nx.all_simple_paths(G, source=treatment, target=outcome))
    
    # Check each path to see if it is a backdoor path
    for path in all_paths:
        if len(path) > 2 and path[1] != outcome:
            return "No"  # There is a backdoor path
    
    return "Yes"  # No backdoor path found

import networkx as nx
import matplotlib.pyplot as plt
import random

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 

    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos


    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


G = nx.DiGraph()

nodos =['(5/6, 1, 0, 1)\nZ = 16.5',
        '(1, 4/5, 0, 4/5)\nZ = 16.5',
        '(0, 1, 0, 1)\nZ = 9',
        '(1, 1, 0, 1/2)\nZ = 16',
        '(1, 0, 4/5, 0)\nZ = 13.8',
        '(1, 1, _, 1/2)\nno factible',
        '(1, 1, 1/5, 0)\nZ = 15.2',
        '(1, 1, 1, 0)\nno factible',
        '(1, 1, 0, 0)\nZ = 14']

G.add_nodes_from(nodos)

G.add_edge(nodos[0], nodos[1])
G.add_edge(nodos[0], nodos[2])
G.add_edge(nodos[1], nodos[3])
G.add_edge(nodos[1], nodos[4])
G.add_edge(nodos[3], nodos[5])
G.add_edge(nodos[3], nodos[6])
G.add_edge(nodos[6], nodos[7])
G.add_edge(nodos[6], nodos[8])

pos = hierarchy_pos(G, root=nodos[0], width=100.)

nx.draw(G, pos=pos, with_labels=True, arrows=False)
# plt.show()

def get_random_node():
    return random.sample(nodos, 1)[0]
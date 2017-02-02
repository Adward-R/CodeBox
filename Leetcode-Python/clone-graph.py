__author__ = 'Adward'
"""
OJ's undirected graph serialization:

Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = [] #List[UndirectedGraphNode]

class Solution(object):
    def buildGraph(self, graphStr, startLabel):
        """
        :type graphStr: str
        :type startLabel: int
        :rtype: UndirectedGraphNode
        """
        nodesLink = {}
        vertices = {}
        for nodeStr in graphStr[1:-1].split('#'):
            node = nodeStr.split(',')
            ky = int(node[0])
            nodesLink[ky] = [int(nbr) for nbr in node[1:]]
            vertices[ky] = UndirectedGraphNode(ky)
        print(nodesLink)
        for ky in nodesLink:
            for nbr in nodesLink[ky]:
                if nbr == ky:
                    vertices[ky].neighbors.append(vertices[ky])
                else:
                    vertices[ky].neighbors.append(vertices[nbr])
                    #vertices[nbr].neighbors.append(vertices[ky])
        #for v in vertices:
        #    vertices[v].neighbors.sort(key=lambda x: x.label)
        return vertices[startLabel]

    def serializeGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: str
        """
        nodesLink = {node.label: []}
        vq = [node]
        while len(vq):
            lbl = vq[0].label
            for nbr in vq[0].neighbors:
                if nbr.label not in nodesLink:
                    nodesLink[nbr.label] = [lbl]
                    #nodesLink[lbl].append(nbr.label)
                    vq.append(nbr)
                elif nbr.label == lbl:
                    nodesLink[lbl].append(lbl)
                elif nbr.label not in nodesLink[lbl]:
                    nodesLink[nbr.label].append(lbl)

            vq = vq[1:]
        #print(nodesLink)
        nlink = [[n] + nodesLink[n] for n in nodesLink]
        return '{' + '#'.join([','.join([str(i) for i in ilst]) for ilst in nlink]) + '}'


    def cloneGraph0(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        serial = self.serializeGraph(node)
        print(serial)
        return self.buildGraph(serial, node.label)

    def cloneGraph(self, node):  # final BFS solution
        if not node:
            return None
        lmap = {node.label: UndirectedGraphNode(node.label)}  # label->node
        Q = [node]
        while len(Q):
            newQ = []
            for V in Q:
                for nbr in V.neighbors:
                    if nbr.label not in lmap:
                        lmap[nbr.label] = UndirectedGraphNode(nbr.label)
                        newQ.append(nbr)
                    lmap[V.label].neighbors.append(lmap[nbr.label])
            Q = newQ
        return lmap[node.label]

sol = Solution()
#graphNode = sol.buildGraph('{0,1,2#1,2#2,2}', 2)
#graphNode = sol.buildGraph('{-1,1#1}', 1)
#graphNode = sol.buildGraph('{0,0,0}', 0)
graphNode = sol.buildGraph('{-3,-1,3,5#-1,2,3,3#2,3#3,5#5}', -3)
serial = sol.serializeGraph(sol.cloneGraph(graphNode))
print(serial)
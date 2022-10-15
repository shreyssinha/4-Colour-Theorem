class Node:

    def __init__(self, idx, data = 0): #Constructor
        """
        id : Z+
        """
        self.id = idx
        self.data = data
        self.neighbors = dict()

    def addNeighbor(self, neighbor, weight = 0):
        """
        neighbor: Node Object
        weight: 
        """
        if neighbor.id not in self.neighbors.keys():
            self.neighbors[neighbor.id] = weight
    
    def setData(self, data):
        self.data = data
    
    def getNeighbors(self):
        return self.neighbors.keys()

    def getId(self):
        return self.id
    
    def getData(self):
        return self.data
    
    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

    def __str__(self):
        return str(self.data) + "Connected to : "+ \
            str([x.data for x in self.neighbors])

########################################################

class Graph:
    
    vertexCardinality = 0

    def __init__(self):
        self.allNodes = dict()
    
    def addNode(self, idx):

        if idx in self.allNodes:
            return None
        
        Graph.vertexCardinality += 1
        node = Node(idx = idx)
        self.allNodes[idx] = node
        return node
    
    def addNodeData(self, idx, data):
        if idx in self.allNodes:
            node = self.allNodes[idx]
            node.setData(data)
        else:
            print("Node at id does not exist.")

    def addEdge(self, src, dst, weight = 0):
        self.allNodes[src].addNeighbor(self.allNodes[dst], weight)
        self.allNodes[dst].addNeighbor(self.allNodes[src], weight)

    def isNeighbor(self, v1, v2):
        if v1 in self.allNodes[v2].getNeighbors():
            if v1 != v2:
                return True
        else :
            return False

    def printEdges(self):
        for idx in self.allNodes:
            node = self.allNodes[idx]
            #print(node.getId())
            for con in node.getNeighbors():
                if node.getId() < self.allNodes[con].getId():
                    print(node.getId(), " -- ",
                    self.allNodes[con].getId())

    def getNode(self,idx):
        if idx in self.allNodes:
            return self.allNodes[idx]
        else:
            return None

    def getAllNodesIds(self):
        return self.allNodes.keys()
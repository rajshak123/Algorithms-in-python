class Graph:
	def __init__(self):
		self.edges={}
	def addVertex(self,v):
		if v not in self.edges:
			self.edges[v]=[]
	def addEdge(self,from_v,to_v):
		if from_v not in self.edges:
			self.edges[from_v]
		if to_v not in self.edges:
			self.edges[to_v]
		if to_v not in self.edges[from_v]:
			self.edges[from_v].append(to_v)
		if from_v not in self.edges[to_v]:
			self.edges[to_v].append(from_v)
	def isEdge(self,from_v,to_v):
		if from_v not in self.edges:
			return False
		if to_v not in self.edges:
			return False
		return to_v in self.edges[from_v]
def loadGrapg(edges):
	g=Graph()
	for v in edges:
		g.addVertex(v)
		for neighbors in edges[v]:
			g.addEdge(v, neighbors)
	return g

class DFS:
	def __init__(self,graph,s):
		self.graph=graph
		self.start=s
		self.color={}
		self.pred={}
		for v in self.graph.edges:
			self.color[v]=White
			self.pred[v]=None
		self.dfs_visit(s)
		
	def dfs_visit(self,u):
		
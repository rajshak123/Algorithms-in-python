# Remove a node from BST has to be implemented

from node import Node
class BST(object):
	def __init__(self):
		self.root=None
	def add(self,data):
		if self.root is None:
			self.root=Node(data)
		else:
			self.root.insert(data)
	def contains(self,data):
		node=self.root
		while node:
			if data==node.data:
				return True
			elif data<node.data:
				node=node.leftChild 
			else:
				node=node.rightChild
		return False
	def insert(self,data):
		if not self.root:
			self.root=Node(data)
		else:
			self.insertNode(self,data,self.root)
	
	def insertNode(self,data,node):
		if data<node.data:
			if node.leftChild:
				self.insertNode(data, node.leftChild)
			else:
				self.leftChild=Node(data)
		else:
			if node.rightChild:
				self.insertNode(data, node.rightChild)
			else:
				self.rightChild=Node(data)

	def getMin(self):
		if self.root:
			return self.getMinVal(self.root)
	def getMinVal(self,node):
		if node.leftChild:
			self.getMinVal(node.leftChild)
		return node.data
	
	def getMax(self):
		if self.root:
			return self.getMaxVal(self.root)
	def getMaxVal(self,node):
		if node.rightChild:
			return self.getMaxVal(node.rightChild)
		return node.data
	def inorderTraversal(self,node):
		if self.leftChild:
			inorderTraversal(self.leftChild)
		print(node.data)

		if self.rightChild:
			inorderTraversal(self.rightChild)

	def remove(self,data):
		
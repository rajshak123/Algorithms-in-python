class Node(object):
	def __init__(self,data):
		self.data=data
		self.leftChild=None
		self.rightChild=None
	def insert(self,data):
		if data<self.data:
			if not self.leftChild:
				self.leftChild=Node(data)
			else:
				self.leftChild.insert(data)
		else:
			if not self.rightChild:
				self.rightChild=Node(data)
			else:
				self.rightChild.insert(data)
	def getmin(self):
		if self.leftChild is None:
			return self.data
		else:
			return self.getmin()
	def getmax(self):
		if self.rightChild is None:
			return self.data
		else:
			return self.rightChild.getmax()
	def traverseInOrder(self):
		if self.leftChild is not None:
			self.leftChild.traverseInOrder()
		print(self.data)
		if self.rightChild is not None:
			self.rightChild.traverseInOrder()
		

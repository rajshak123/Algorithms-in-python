from node import Node
class LinkedList(object):
	def __init__(self):
		self.head=None
		self.counter=0
	
	def insertStart(self,data):
		self.counter+=1
		newNode=Node(data)
		if self.head is None:
			self.head=newNode
		else:

			newNode.nextNode=self.head
			self.head=newNode

	def traverse(self):
		actualNode=self.head
		while actualNode is not None:
			print(actualNode.data)
			actualNode=actualNode.nextNode
	
	def insertEnd(self,data):
		actualNode=self.head
		while actualNode.nextNode is not None:
			actualNode=actualNode.nextNode
		newNode=Node(data)
		actualNode.nextNode=newNode
	
	def removeStart(self):
		self.counter-=1
		self.head=self.head.nextNode
	
	def removeEnd(self):
		self.counter-=1
		actualNode=self.head
		if self.head.nextNode==None:
			self.removeStart()
		else:
			# import pdb
			# pdb.set_trace()
			while actualNode.nextNode is not None:
				rem=actualNode
				actualNode=actualNode.nextNode
			rem.nextNode=None
			

	def removeAny(self,data):
		self.counter-=1
		if self.head is None:
			return
		actualNode=self.head
		previousNode=None
		while actualNode.data!=data:
			previousNode=actualNode
			actualNode=actualNode.nextNode
		if previousNode is None:
			self.head=actualNode.nextNode
		else:
			previousNode.nextNode=actualNode.nextNode
		
		
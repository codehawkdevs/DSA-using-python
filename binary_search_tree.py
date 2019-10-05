class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			self.insertNode(data, self.root)
		else:
			self.root = Node(data)
			
	def insertNode(self, data, node):
		if data<node.data:
			if node.left:
				self.insertNode(data, node.left)
			else:
				node.left = Node(data)
		else:
			if node.right:
				self.insertNode(data, node.right)
			else:
				node.right = Node(data)

	def getMinValue(self):
		if self.root:
			return self.getMin(self.root)

	def getMin(self, node):
		if node.left:
			return self.getMin(node.left)
		return node.data

	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root)

	def getMax(self, node):
		if node.right:
			return self.getMax(node.right)
		return node.data

	def traverseInorder(self):
		if self.root:
			return self.inorder(self.root)
		else:
			print("Tree is empty")

	def inorder(self, node):
		if node.left:
			self.inorder(node.left)

		print(node.data)

		if node.right:
			self.inorder(node.right)

	def remove(self,data):
		if self.root:
			self.root = self.removeNode(data, self.root)

	def removeNode(self, data, node):
		if not node:
			return node

		if node.data>data:
			node.left = self.removeNode(data, node.left)

		elif node.data<data:
			node.right = self.removeNode(data, node.right)

		else:
			if not node.left and not node.right:
				del node
				return None

			if not node.left:
				temp = node.right
				del node
				return temp

			elif not node.right:
				temp = node.left
				del node
				return temp

			temp = self.getPredecessor(node.left)
			node.data = temp.data
			node.left = self.removeNode(temp.data, node.left)
		return node

	def getPredecessor(self, node):
		if node.right:
			return getPredecessor(node.right)
		return node


if __name__ == '__main__':
	bt = BinaryTree()
	bt.insert(2)
	bt.insert(1)
	bt.insert(4)
	bt.insert(5)
	bt.insert(3)
	bt.traverseInorder()
	print()
	bt.remove(1)
	bt.traverseInorder()
	print()
	print(ord('c'))
























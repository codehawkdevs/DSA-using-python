class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insertafter(self, prev, new_data):
		if prev == None:
			return " Error 404"
		new_node = Node(new_data)
		new_node.next = prev.next
		prev.next = new_node 

	def append(self, new_data):

		new_node = Node(new_data)
		if self.head == None:
			self.head = new_node
			return
		last = self.head
		while(last.next):
			last = last.next
		last.next =new_node

	
	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

if __name__ == "__main__":
	ll = LinkedList()
	ll.head = Node(1)
	second = Node(2)
	third = Node(3)
	ll.head.next = second
	second.next = third
	ll.push(9)
	ll.insertafter(ll.head, 5)
	ll.append(6)
	ll.printlist()

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

	def append(self, new_data):
		new_node = Node(new_data)

		if self.head == None:
			self.head = new_node
			return

		last = self.head
		while(last.next):
			last = last.next

		last.next = new_node

	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data, end='')
			temp = temp.next
		print()
# here's the function
	def remove_duplicates_unordered(self):
		temp1 = self.head
		while(temp1 and temp1.next):
			temp2 = temp1
			while(temp2.next):
				if(temp1.data == temp2.next.data):
					dup = temp2.next
					temp1.next = temp2.next.next
					temp2.next = None
				else:
					temp2 = temp2.next
			temp1 = temp1.next


if __name__ == '__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(4)
	llist.push(5)
	llist.append(7)
	llist.append(6)
	llist.append(8)
	llist.append(9)
	llist.push(1)
	llist.push(5)
	llist.append(7)
	llist.append(8)
	llist.append(9)
	llist.printlist()
	llist.remove_duplicates_unordered()
	llist.printlist()

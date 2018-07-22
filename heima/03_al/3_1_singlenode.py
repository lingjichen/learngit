#-*- coding:utf-8 -*-
#!/usr/bin/env python3

class SingleNode(object):
	""" single node  """
	def __init__(self, item):
		self.item = item
		# next is next node
		self.next = None

class SingleLinkList(object):
	"""  single link list"""
	def __init__(self):
		self._head = None
	
	def is_empty(self):
		return self._head == None

	def length(self):
		cur = self._head
		count = 0
		while cur != None:
			count +=1
			cur = cur.next
		return count

	def travel(self):
		cur = self._head
		while cur != None:
			print(cur.item, '',end="")			
			cur = cur.next
		print()

	def add(self, item):
		node = SingleNode(item)
		node.next = self._head
		self._head = node

	def append(self, item):
		node = SingleNode(item)
		if self.is_empty():
			self._head = node
		else:
			cur = self._head
			while cur.next != None:
				cur = cur.next
			cur.next = node


	def insert(self, pos, item):
		if pos < 0:
			self.add(item)
		elif pos > (self.length() - 1):
			self.append(item)
		else:
			node = SingleNode(item)
			count = 0
			pre = self._head
			while count < (pos - 1):
				count += 1
				pre = pre.next
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		cur = self._head
		pre = None
		while cur != None:
			if cur.item == item:
				if not pre:
					self._head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next

	def search(self, item):
		cur = self._head
		while cur != None:
			if cur.item == item:
				return True
			cur = cur.next
		return False

if __name__ == '__main__':
	ll = SingleLinkList()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2, 4)
	print("length", ll.length())
	ll.travel()
	print(ll.search(3))
	print(ll.search(5))
	ll.remove(1)
	print("length", ll.length())
	ll.travel()
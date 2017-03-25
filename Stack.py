class StackNode:
	def __init__(self, nxt,value):
		self.next = nxt
		self.value = value
class Stack:
	def __init__(self):
		self.top = None
		self.size = 0
	def push(self,value):
		self.top = StackNode(self.top,value)
		self.size += 1
	def pop(self):
		if self.top is None:
			return None
		val = self.top.value
		self.top = self.top.next
		self.size -= 1
		return val
	def peek(self):
		if self.top is None:
			return None
		return self.top.value
	def isEmpty(self):
		return self.top is None
	def getSize(self):
		return self.size
	def display(self):
		cur=self.top
		l = []
		while not self.isEmpty():
			l.append(self.pop())
		for i in range(len(l)-1):
			print(str(l[i]),end="<--")
			self.push(l[i])
		print(str(l[len(l)-1]))
		self.push(l[len(l)-1])
	

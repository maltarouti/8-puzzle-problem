
class node:
	def __init__(self, data, cost, parent=None):
		self.data = data 
		self.cost = cost
		self.adj = []
		self.parent = parent

	def getPriority(self):
		return self.cost

class normal_node:
	def __init__(self, data, parent=None):
		self.data = data 
		self.adj = []
		self.parent = parent

class tree:
	def __init__(self, initial_state, isCost=True):
		if(isCost):
			self.root = node(initial_state, 0)
		else:
			self.root = normal_node(initial_state)



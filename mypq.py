from pq import PriorityQueue

'''
The MyPQ class extends a PriorityQueue class.
The PriorityQueue class uses a heap as the underlying data structure. 

Running time of methods in the MyPQ class:
	findtopk - O(k*log n^2)
	removetopk - O(k*log n)
	changepriority - O(log n)
	remove - O(log n)
	insert - O(log n)
'''

class MyPQ(PriorityQueue):
	
	def findtopk(self,k):
		"""
		Returns a list of the k items with the highest priority. 
		If there are fewer than k items in the Priority Queue, 
		then this returns a list of all that are left.
		"""
		hp_items = []	
		if len(self) <= k: 						
			for i in self._entries:
				hp_items.append(i.item)
			return hp_items
		for i in range(0,k):					
			hp_items.append(self.removemin())	
		for i in hp_items:
			self.insert(i, int(i[3]))
		return hp_items						

	def removetopk(self, k):
		'''
		Removes and returns the k items with the highest priority. 
		The output is a list. If there are fewer than k items 
		in the Priority Queue, then this removes and returns all 
		items that are left.
		'''
		hp_items = []
		if len(self) < k: 						
			for i in self._entries:
				hp_items.append(self.removemin())
			return hp_items	
		for i in range(0,k):					
			hp_items.append(self.removemin())
		return hp_items								

	def changepriority(self, item, newpriority):
		'''
		Updates the priority of 'item' to be 'newpriority'.
		'''
		i = self._itemmap[item]
		entry = self._entries[i]
		if newpriority >= entry.priority:
			entry.priority = newpriority
			self._downheap(i) 					
		elif newpriority <= entry.priority:
			entry.priority = newpriority
			self._upheap(i) 					
												
	def remove(self, item):
		'''
		Removes the given item from the priority queue. 
		Raises a KeyError if item is not actually in the Priority Queue.
		'''
		if item in self._itemmap:
			for i in self._entries: 
				if self._itemmap[item] == len(self._entries) - 1: 
					break
				self._swap(self._itemmap[item], self._itemmap[item] + 1)
			self._entries.pop()
		else:
			raise KeyError

	def insert(self, item, priority):
		'''
		Overrides the insert method in the 'PriorityQueue' class
		so that if a duplicate item is added, it changes the priority 
		rather than inserting a copy. 
		This will solve the problem that the given implementation can 
		lose track of an item in the itemmap if it is inserted twice.
		'''
		if item in self._itemmap:
			self.changepriority(item, priority)
		else:
			PriorityQueue.insert(self, item, priority)
												

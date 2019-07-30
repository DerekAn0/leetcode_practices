class BinarySearch:
	"""docstring for BinarySearch"""
	def __init__(self, arg,target):
		self.list = arg
		self.target = target


	def search(self, new_list):
		n = len(new_list)
		if n == 0:
			return -1
		else:
			n =(int) (n / 2) 
			if self.target > new_list[n]:
				return self.search(new_list[n+1:])+n+1

			elif self.target < new_list[n]:
				return self.search(new_list[:n])
			else:
				return n


	def search_without_recursif(self):
		low = 0
		high = len(self.list) -1

		while low<=high:
			mid = (int)((low + high) /2)
			if self.list[mid] < self.target:
				low = mid + 1
			elif self.list[mid] > self.target:
				high = mid -1
			else:
				return mid 
		return -1 


sort_list = [3,11,21,29,41,54,61,78,110,127]

searcher = BinarySearch(sort_list,127)
print(searcher.search(sort_list))



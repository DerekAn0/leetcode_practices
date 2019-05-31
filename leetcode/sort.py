class Sort:
	def __init__(self):
		self.test_list =[ 2,3,4,5,2]

	def Quick(self):
		print(self.test_list)

a = [1,3,4]
def use_lambda(num:list)->int:
	return lambda num:max(num)
print(use_lambda.__annotations__)
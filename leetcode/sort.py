class Sort:
	test_list = [49,38,65,97,76,13,27,49]
	after_list = test_list.copy()

	@classmethod
	def __str__(cls):
		return '{0.after_list}'.format(cls)

	def Quick(self):
		pass

	@classmethod
	def erase_after_list(cls):
		cls.after_list = cls.test_list


	@classmethod
	def Direct_Insert(cls):
		pass


	@classmethod
	def Bubble(cls):
		print(cls.test_list)
		n = len(cls.after_list)
		for i in range(n-1):
			for j in range(n-i-1):
				if cls.after_list[j] > cls.after_list[j+1]:
					cls.after_list[j],cls.after_list[j+1] = cls.after_list[j+1],cls.after_list[j]



Sort.Bubble()
print(Sort())

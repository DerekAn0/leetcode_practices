class Sort:
	test_list = [49,38,65,97,76,13,27,49]
	after_list = test_list.copy()

	@classmethod
	def __str__(cls):
		return '原数组：{0.test_list}\n排序之后：{1.after_list}'.format(cls,cls)

	def Quick(self):
		pass

	@classmethod
	def erase_after_list(cls):
		cls.after_list = cls.test_list


	@classmethod
	def Direct_Insert(cls):
		# 以第一个为pivot 之后一个个插入已知有序序列
		n = len(cls.after_list)
		for i in range(1,n):
			# from 2 index
			j=i
			while j>0 and cls.after_list[j] < cls.after_list[j-1]:
				cls.after_list[j],cls.after_list[j-1] = cls.after_list[j-1],cls.after_list[j] 
				j-=1


	@classmethod
	def Insert(cls):
		n = len(cls.after_list)
		for i in range(1,n):
			target = cls.after_list[i]
			j = i 
			# forward
			while target<cls.after_list[j-1] and j>0:
				# print(cls.after_list[j])
				cls.after_list[j] = cls.after_list[j-1]
				j -= 1
			cls.after_list[j] = target

	@classmethod
	def Bubble(cls):
		print(cls.after_list)
		n = len(cls.after_list)
		for i in range(n-1):
			for j in range(n-i-1):
				if cls.after_list[j] > cls.after_list[j+1]:
					cls.after_list[j],cls.after_list[j+1] = cls.after_list[j+1],cls.after_list[j]



Sort.Insert()
print(Sort())


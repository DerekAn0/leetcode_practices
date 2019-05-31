import string

from itertools import zip_longest

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
        
#     	mapper = {
#     	"2":["a","b","c"],
#     	"3":["d","e","f"],
#     	"4":["g","h","i"],
#     	"5":[]

#     	}
#     	for i in range(2,9):
#     		# for c in range('a','z'):
#     		for num in range(0,3):
#     			mapper[i].append()


#         for s in str:
#         	if 

list1 = [2,3,4]
list2 = ['a','b','','c']

for a in zip_longest(list2,list1,fillvalue=None):
	print(a)

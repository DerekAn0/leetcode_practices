class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		return self.is_symmetric_list(self.discovery(root))


	def discovery(self,root:TreeNode)->list:
		open = [root]
		value = []
		while len(open) != 0 :
			# entry FI 
			generated = open.pop(0)
			value.append(generated.val)
			if generated.left is not None:
				left = generated.left 
				open.append(left)
			else:
				left = None
			if generated.right is not None:
				right = generated.right 
				open.append(right)
			else:
				right = None
			# exit LO
		return value

	def is_symmetric_list(self,l:list) -> bool:
		is_symmetric = True
		while(len(l)!=0 and len(l)!=1):
			first = l.pop(0)
			last = l.pop(-1)
			is_symmetric = first == last
			if is_symmetric is False:
				return False 
		return is_symmetric



root = TreeNode(1)


l = TreeNode(2) 
r = TreeNode(3)
ll = TreeNode(4)
lr = TreeNode(5)
rl = TreeNode(6)
rr = TreeNode(7)

root.left = l
root.right = r

l.left=ll
l.right = lr
r.left = rl
r.right = rr




s = Solution()
print(s.is_symmetric_list(s.discovery(root)))

print()
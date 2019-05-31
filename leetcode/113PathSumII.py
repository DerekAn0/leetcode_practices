# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # left + right = root 
        if root.left is not None and root.right is not None:
            whole = []
            for i in self.pathSum(root.left,sum-root.val):
                whole.append(i)
            for j in self.pathSum(root.right,sum-root.val):
                whole.append(j)
            for i in range(len(whole)):
                whole[i].insert(0,root.val)
            return whole
        # right = whole
        elif root.left is None and root.right is not None:
            whole = []
            print(root.val)
            for j in self.pathSum(root.right,sum-root.val):
                whole.append(j)
            for i in range(len(whole)):
                whole[i].insert(0,root.val)
            return whole
        # left = whole
        elif root.left is not None and root.right is None:
            whole = []
            for j in self.pathSum(root.left,sum-root.val):
                whole.append(j)
            for i in range(len(whole)):
                whole[i].insert(0,root.val)
            return whole
        else:
            if root.val is sum:
                return [[sum]]
            else:
                return []

root = TreeNode(7)
right1 = TreeNode(2)
left2 = TreeNode(3)
right2 = TreeNode(-7)

root.right = right1
right1.left = left2
right1.right = right2


solution = Solution()
print(solution.pathSum(root,2))


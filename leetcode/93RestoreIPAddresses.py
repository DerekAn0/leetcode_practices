class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)>12 or len(s)<4:
            return []
        else:
            

s= "12345"
n = len(s)
print(len(s))

for i in range(n):
    for j in range(n):
        if j>i:
            for l in range(n) :
                if l>j:
                    print("{0} + {1} + {2}".format(i,j,l)) 
class Solution:
    def defangIPaddr(self, address: str) -> str:
    	return address.replace(".","[.]")


s=Solution()
s.defangIPaddr("255.100.50.0") 
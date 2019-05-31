class Solution:
    def divisorGame(self, N: int) -> bool:

    	if N == 2:
    		return True
    	elif N == 1 or N == 3:
    		return False
    	else:
    		alice_choice = self.find_all_choices(N)
	    	for i in alice_choice :
	    		bob_choice = self.find_all_choices(N-i)
	    		for index,j in enumerate(bob_choice):
	    			# if divisorGame(n-i-j) 对于所有j全是true证明alice 有一招绝杀无论bob怎么选择bob都输则return true
	    			# 否则 在所有j中 bob可以有翻盘机会 故此break alice重新选择一个 因为bob非常聪明能赢就肯定赢了
	    			if self.divisorGame(N-i-j) == False:
	    				break
	    			else:
	    				if index == len(bob_choice)-1:
	    					return True
	    				else:
	    					continue
	    	return False

    def find_all_choices(self, N:int) ->list:
    	all_possible = []
    	for i in range(1,N):
    		if N % i ==0 :
    			all_possible.append(i)
    	return all_possible

s = Solution()
for i in range(30):

	print(s.divisorGame(i))


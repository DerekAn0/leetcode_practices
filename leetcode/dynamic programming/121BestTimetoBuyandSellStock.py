class Solution:
	def maxProfit(self, prices, mode="Normal") :
		if mode == "Normal":
			info = {}
			for buy_day in range(len(prices)):
				for sell_day in range(len(prices)):
					if sell_day > buy_day:
						info[str(buy_day)+"->"+str(sell_day)] = prices[sell_day] - prices[buy_day]	
			print(info)
		else:
			info = {}
			for day in range(len(prices)-1):
				tomorrow = day + 1 
				info[str(day)+"-"+str(tomorrow)] = prices[tomorrow] - prices[day]

			for buy_day in range(len(prices)):
				for sell_day in range(len(prices)):
					pass
			# print(info)

		return 0


					

s = Solution()
s.maxProfit([7,1,5,3,6,4],"innormal")


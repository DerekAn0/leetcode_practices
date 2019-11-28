class Solution:
    def minTimeToVisitAllPoints(self, points):
        sum = 0
        for i in range(0, len(points)-1):
            j = i+1
            sum += self.caculate_distance(points[i], points[j])
        return sum



    def caculate_distance(self, point1, point2):
        num1 = point1[0] - point1[0]
        num2 = point1[1] -point1[1]
        if num1 == num2:
        	return num1
        elif num1 > num2:
        	return num1
        else:
        	return num2


sol = Solution()
sum = sol.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]])
print(sum)
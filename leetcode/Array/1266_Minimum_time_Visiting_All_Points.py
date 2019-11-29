import math
class Solution:
    def minTimeToVisitAllPoints(self, points):
        sum = 0
        for i in range(0, len(points)-1):
            j = i+1
            sum += (self.caculate_distance(points[i], points[j]))
        return sum

    def caculate_distance(self, point1, point2):
        num1 = math.fabs(point1[0] - point2[0])
        num2 = math.fabs(point1[1] - point2[1])
        if num1 == num2:
        	return math.fabs(num1)
        elif num1 > num2:
        	return math.fabs(num1)
        else:
            return math.fabs(num2)


sol = Solution()
sum = sol.minTimeToVisitAllPoints([[3,2],[-2,2]])
print(sum)
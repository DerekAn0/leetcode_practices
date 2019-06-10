from random import randint

# 1.1 almost random octet
def randomOctet(n):
	return [randint(0,1) for i in range(n)]

# 1.2 number of bits equals to one 
def countOne(myList):
	return myList.count(1)

def countOnev2(myList):
	count = 0
	for i in myList:
		if i == 1:
			count += 1
	return count

# 1.3 even number of bits
def isEvenOne(myList):
	return countOne(myList) % 2 == 0

# 1.4 Addtion of a bit of partiy
if __name__ == '__main__':
	n = 2
	my_list = randomOctet(n)
	if isEvenOne(my_list):
		my_list.append(1)
	else:
		my_list.append(0)
	print(my_list)
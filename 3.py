number = int(input())
summ = 0

def factorial(num):
	result = 1

	for current_num in range(1,num+1):
		result*= current_num

	return result

for iteration in range(1, number + 1):
	
	current_factorial = factorial(iteration)
	summ+= 1 / factorial(iteration)

print(round(summ,5))



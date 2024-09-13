number = int(input())
zero_amount = 0

while number != 0:
	current_digit = number % 10

	if current_digit == 0:
		zero_amount+= 1

	number//= 10

print(zero_amount)
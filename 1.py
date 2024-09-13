number = int(input())
summ_of_array = 0
prev_digit = ''

while number != 0:
	current_digit = number % 10

	if current_digit == 0 and prev_digit == 0:
		summ_of_array = 0

	summ_of_array+= current_digit	
	number//= 10
	prev_digit = current_digit

print(summ_of_array)
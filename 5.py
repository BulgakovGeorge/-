original_number = int(input())

for number in range(1,original_number+1):
	square_number = number * number

	if square_number > original_number:
		break
	else:
		print(square_number)

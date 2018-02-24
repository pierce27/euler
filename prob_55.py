

# if len(num_total)%2 = 0:


# print int_num + int_num_rev


def sum_rev(num):
	
	# reverse number
	num_rev = reverse(num)

	

	print num
	print num_rev

	# convert to integers
	int_num = int(num)
	int_num_rev = int(num_rev)

	num_total_int = int_num + int_num_rev

	num_total = str(num_total_int)

	# check if odd length
	if len(num_total)%2 != 0:
		# check plaindromoe
		checkpal(num_total)
	else:
		# recursively check num total
		sum_rev(num_total)

# reverse number
def reverse(num):
	num_rev = ''

	i = len(num)

	while i != 0:
		num_rev += num[i-1]
		i = i - 1

	return num_rev

# check if number is pallindrome
def checkpal(total):




def main():
	sum_rev('349')

main()
# https://projecteuler.net/problem=55

# if len(num_total)%2 = 0:


# print int_num + int_num_rev


def sum_rev(num, count):
	# reverse number
	num_rev = reverse(num)

	# convert to integers
	int_num = int(num)
	int_num_rev = int(num_rev)

	num_total_int = int_num + int_num_rev

	num_total = str(num_total_int)

	if count > 49:
		return False

	# check plaindromoe
	if check_pal(num_total):
		return count
	else:
		count = count + 1

	count = sum_rev(num_total, count)
	return count



# check if number is pallindrome
def check_pal(total_str):
	
	print total_str
	# check if odd
		# get middle number
	middle = len(total_str)/2
	i = 0
	first = ''
	second = ''

	# get first part of number
	while i < middle:
		first  += total_str[i]
		i = i+1

	# get second part of number
	if len(total_str)%2 != 0:
		i = middle + 1
	else:
		i = middle

	while i < len(total_str):
		second  += total_str[i]
		i = i+1

	if first == reverse(second):
		return True


# reverse number
def reverse(num):
	num_rev = ''

	i = len(num)

	while i != 0:
		num_rev += num[i-1]
		i = i - 1

	return num_rev		






def main():
	
	n = 0
	lyc_count = 0

	while n < 10000:
		print n
		count = sum_rev(str(n), 1)

		if count:
			print count
			print 'It took ' + str(count) + ' times'
			print '\n'
		else:
			print 'No Pall'
			print '\n'
			lyc_count = lyc_count + 1
		n = n + 1

	print 'There are ' + str(lyc_count) + ' lycrhell numbers'

main()






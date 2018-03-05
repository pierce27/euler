# https://projecteuler.net/problem=38


def is_srt_harshad(num):
	if is_s_harshad(num):
		if is_rt_harshad(num):
			return True
		else: 
			return False
	else:
		return False

	
def is_s_harshad(num):
	
	if is_harshad(num):
		if is_prime(num / sum_num(num)):
			return True
		else:
			return False
	else:
		return False


def is_rt_harshad(num):
	str_num = str(num)

	i = len(str_num) - 1

	while i > 0:
		trunc = int(str_num[0:i])
		if not is_harshad(trunc):
			return False
		i = i -1

	return True

def is_harshad(num):

	if num%sum_num(num) == 0:
		return True
	else:
		return False


def is_prime(num):

	for i in xrange(2,num):
		if num%i == 0:
			return False

	return True

def sum_num(num):
	num_sum = 0

	for n in str(num):
		num_sum = num_sum + int(n)	

	return num_sum

def main():

	psrth_nums = []
	psrth_sum = 0

	for i in xrange(100,100000000000000):
		if is_prime(i):
			print i
			str_i = str(i)
			end_char = len(str_i) - 1
			trunc = int(str_i[0:end_char])
			if is_srt_harshad(trunc):
				print 'IS SRT!!!!!!!!!'
				psrth_nums.append(i)

	for x in psrth_nums:
		psrth_sum = x + psrth_sum

	print psrth_sum


		
	
main()
password = 'a123456'
c = 3
while True:
	pas = input('enter your password:')
	c = c - 1
	if pas == password:
		print('sucess!')
		break
	elif c > 0:
		print('the password is wrong!')
		print('you got', c, 'chance!')
	else:
		print('you got blocked!')
		break
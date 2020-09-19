def check_slovo(slovo):
	checkk = True
	i = 0
	while i < len(slovo):
		if (slovo[i]> 192 or (slovo[i]>65 and slovo[i]<90) or (slovo[i]>97 and slovo[i]<122) or slovo[i] ==32) != True:
			checkk = False
		i +=1
	return checkk

def worlds127(name, fam):
	name = list(name)
	fam = list(fam)
	name, fam = unicod(name, fam)
	checkk_name = check_slovo(name)
	checkk_fam = check_slovo(fam)
	return checkk_name, checkk_fam

def unicod(name, fam):
	i = 0
	name  = list(name)
	fam = list(fam)
	while i < len(name):
		name[i] = ord(name[i])
		i +=1
	i = 0
	while i < len(fam):
		fam[i] = ord(fam[i])
		i +=1
	return name, fam

def getting_tail(mass, n):
	i = 0
	k = len(list(mass)) - n
	mass = mass[k:]
	tail = '' 
	while i < len(list(mass)):
		tail = tail + str(chr(mass[i]))
		i +=1
	return tail

def add00(mass, n):
	i = 0
	while i < n:
		mass.append(0)
		i +=1
	return mass

def work_ris1(name, fam, tail_str, result_sum, result_sum_ascii):
	if len(name) != len(fam):
		n = abs(len(name) - len(fam))
		if len(name) < len(fam):
			tail_str = getting_tail(fam, n)
			name = add00(name, n)
		else:
			tail_str = getting_tail(name, n)
			fam = add00(fam, n)
	else:
		tail_str = ''
	i = 0
	result_sum_ascii = []
	while i < len(name):
		cakesumm = int(name[i])^int(fam[i])
		result_sum_ascii.append(cakesumm)
		cakesumm = chr(cakesumm)
		result_sum = result_sum + cakesumm
		i +=1
	return name, fam, tail_str, result_sum, result_sum_ascii
def res(resl):
	tem = sum(resl)
	if int(tem/10) ==0:
		return tem
	else:
		red = [int(x) for x in str(tem)]
		return res(red)
tot = 444
resl = [int(x) for x in str(tot)]
print(res(resl))
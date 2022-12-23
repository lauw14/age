driving = input('請問你有沒有開過車? 有/沒有')
if driving != '有' and driving != '沒有': #不等於有，又，不等於沒有
	print('只能輸入有或沒有')
	raise SystemExit   #跳出此程式
age = input('請問你的年紀？ 輸入數字')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你成年而合法開過車')
	else:
		print('你未成年而不合法開過車')
elif driving == '沒有':
	if age >= 18:
		print('可以去備考駕照，再去開車')
	else:
		print('再等幾年就可以考駕照')

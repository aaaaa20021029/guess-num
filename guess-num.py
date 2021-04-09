# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "恭喜答對了!"
# 猜錯的話 要告訴他 比答案小

import random

r = random.randint(1, 100)
count = 0

while True:
	count += 1 # count = count + 1
	num = input('請猜一個數字: ')
	num = int(num)
	if num == r:
		print('恭喜答對了!')
		print('已嘗試', count, '次')
		break
	elif num > r:
		print('比答案大。')
	elif num < r:
		print('比答案小。')
	print('已嘗試', count, '次')
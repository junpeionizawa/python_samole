#入力されたものを数値型で保存する
#オートチャージ的なコード
x = int(input('Enter number:'))

if x <= 10000:
   x += 10000
   print(x)
else:
	print(x)


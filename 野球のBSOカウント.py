s1 = ""
sk = 0
bl = 0
import random
for N in range(1,7):
 if  N  <= 7:
 	print(N)
 	mylist = ["strike!", "ball!"]
 	s1 = random.choice(mylist)
 	print(s1)
 if s1 == "strike!":
 	sk += 1
 else:
 	bl += 1
 if sk > 2:
 	print("三振!!アウト!!")
 	break
 if bl > 3:
 	print("フォアボール!!")
 	break

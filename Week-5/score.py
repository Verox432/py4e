score = input("Enter Score: ")
try :
	scorefloat = float(score)
except :
	scorefloat = -255
if scorefloat == -255 :
	print('Invalid Input')
	quit()
if scorefloat > 1.0 :
	print('Cannot enter score higher than 1.0')
elif scorefloat >= 0.9 :
	print('A')
elif scorefloat >= 0.8 :
	print('B')
elif scorefloat >= 0.7 :
	print('C')
elif scorefloat >= 0.6 :
	print('D')
elif scorefloat < 0.6 :
	print('F')

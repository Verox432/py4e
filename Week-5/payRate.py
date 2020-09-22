hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = int(hrs)
r = float(rate)
if h < 40 :
	pay = h * r
else :
	overtime = (h - 40) * (r * 1.5)
	pay = overtime + 40 * r
print(pay)

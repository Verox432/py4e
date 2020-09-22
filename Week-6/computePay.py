def computepay(h,r):
	if h > 40 :
		overtime = (h - 40) * (r * 1.5)
		return overtime + 40 * r
	else :
		return h * r

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)

p = computepay(h,r)
print("Pay",p)

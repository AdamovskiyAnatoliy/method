import math

x = int(input("Enter x: "))

if x > -4:
	f = math.cos(2*x) + 9
else:
	f = -(math.cos(x)/(x-9))

print(f)
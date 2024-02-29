def y1(n):
    return (n * (n + 1)) / 2
def y2(n):
    return (n * (n + 1) * (2 * n + 1)) / 6
def y3(n):
    return ((n * (n + 1)) / 2) ** 2
c=0
for i in range(0,10,1):
	if 9*y2(i)**2==y3(i)*(1+8*y1(i)):
		c+=1
if c==10:
	print("Verified by code")
else:
	print("the equation doesnt hold")

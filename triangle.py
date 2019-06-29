side1=input("enter side")
side2=input("enter side")
side3=input("enter side")
if side1==side2 and side2==side3:
	print "it is equilateral triangle"
elif side1==side2 or side1==side3 or side2==side3:
	print"it is isosceles triangle"
else:
	print "it is scalene triangle"
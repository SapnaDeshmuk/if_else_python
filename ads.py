character=int(input("enter ur character"))
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
lalpha="abcdefghijklmnopqrstuvwxyz" 
if character in alpha:
	print "character is alphabet"
elif character>=0 or character <=9:
	print"character is digit"
else:
	print "character  is special character" 
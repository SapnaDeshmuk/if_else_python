pages=input("enter pages")
needed_pages=input("which page u want")
turn=raw_input("enter right or left")
total_pages=pages/2
if  turn=="left":
	print needed_pages/2
else:
	print total_pages-needed_pages/2
	# if pages/2:
	# 	print pages/2 -needed_pages
	# else:
	# 	print"big"
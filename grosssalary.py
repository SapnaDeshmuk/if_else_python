basic_salary=input("enter value")
if basic_salary<=10000:
	hra=basic_salary*20/100
	da=basic_salary*80/100
	gross_salary = basic_salary + da + hra
	print gross_salary
elif basic_salary>10000 and basic_salary<=20000:
	hra=basic_salary*25/100
	da=basic_salary*90/100
	gross_salary = basic_salary + da + hra
	print gross_sala
else:
	hra=basic_salary*30/100
	da=basic_salary*95/100
	gross_salary = basic_salary + da + hra
	print gross_salary
	
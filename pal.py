actual_cost = input(" Please Enter the Actual Product Price: ")
sale_amount = input(" Please Enter the Sales Amount: ")
if actual_cost.isnumeric()==True and sale.isnumeric()==True:
    actual_cost=int(actual_cost)
    sale_amount=int(sale_amount)
    if(actual_cost >sale_amount):
        amount = actual_cost - sale_amount
        print("Total Loss Amount "+str(amount))
    elif(sale_amount > actual_cost ):
        amount = sale_amount - actual_cost
        print("Total Profit"+str(amount))
    else:
        print("No Profit No Loss!!!")
else:
    print("Value not correct")

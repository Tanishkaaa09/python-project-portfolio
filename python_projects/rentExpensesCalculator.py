#inputs->
#total rent,food ordered,electricity,charge per unit
#persons living in flat
#output->
#total amount you have to pay
rent= int(input("Enter total rent: "))
food= int(input("Enter the amount of food ordered = "))
electricity_spend=int(input("Enter the total of electricity spent "))
charge_per_unit=int(input("enter the charge per unit of electricity = "))
persons=int(input("enter the number of persons living in rooms/flat="))
total_bill=electricity_spend*charge_per_unit
output=(food+rent+total_bill)/persons
print("Rent each person will pay",output)

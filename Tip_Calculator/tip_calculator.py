#Printing the Welcome line 
print("Welcome to the tip calculator")
#Getting the total bill amount 
total_bill = float(input("What is the total bill? $"))
#Getting tip percenatage 
tip = int(input("What percentage tip would you like to give? 10, 12 or 15"))
#Getting number of people for split 
num_ppl = int(input("How many people to split the bill? "))
#Calculating bill with tip 
total_bill_with_tip = tip/100 * total_bill + total_bill
# print(total_bill_with_tip) 
##calculating bill per person
bill_per_person = round(total_bill_with_tip/num_ppl,2)
print(f"Each person should pay ${bill_per_person}")

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
guests = int(input("How many people eating? "))
tip = int(input("Choose tip: 10, 12, 15 or 20? "))
tip_percent = tip/100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
per_person = (total_bill / guests)
print("%.2f" % per_person)
#print(type(per_person))

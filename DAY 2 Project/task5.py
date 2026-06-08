#               We're going to build a tip calculator.

print("Welcome to the Tip Calculator! ")
bill=float(input("What was the total bill? $ "))
tip=int(input("What percentage tip would you like to give? 10 20 15 "))
people=int(input("How many people to split the bill? "))
tip_percent=(bill*tip)/100
total_bill=bill+tip_percent
bill_split=total_bill/people
final_amount=round(bill_split,2)
print(f"each person should pay: ${final_amount}")

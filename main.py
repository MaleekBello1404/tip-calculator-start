#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

total_bill = float(input("What was the total bill? $"))
tip = float(
    input("How many percentage tip would you like to give? 10, 12 or 15? %"))
num_of_ppl = int(input("How many people to split the bill? "))

tip = (tip / 100) * total_bill
processed_bill = tip + total_bill
bill_per_person = processed_bill / num_of_ppl
final_bill = round(bill_per_person, 2)
final_bill = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${final_bill}")
final_bill = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${final_bill}")

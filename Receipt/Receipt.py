taxable_total= float(input("Taxable Total: "))
untaxable_total= float(input("Untaxable Total: "))
#inputs from user
tax = float(0.07)
taxed_amount = taxable_total * tax
taxed_total = taxed_amount + taxable_total
#tax calculations
total_purchase = taxed_total + untaxable_total
#total purchase price
print("Tax: ", f'{taxed_amount:.1f}')
print("Total purchase: ", total_purchase)
#print statements with results

#Problem Analysis
'''
    Ask the user to input 3 of their purchases
    Find the sum of those 3 purchases and display it as it's total.
    If total is greater than 100.00, the user is qualified to have a discount. If not, then display that the total of the user did not fulfill the qualified amount.
    Calculate for the new total that has been subtracted by the discount(if any). And display
    Calculate the Loyalty points by dividing the user's intiial total into 0.10. And display.
    Ask the user to enter it's payment, and accept the payment ONLY if it is greater than the new total amount. Otherwise, display an error that says "Payment Failed"
    Calculate for the change by subtracting the payment to the new total amount. And display.
'''

first= input("Enter the amount of your first purchase:")
second= input("Enter the amount of your second purchase:")
third= input("Enter the amount of your third purchase:")
total = float(first) + float(second)+ float(third)
print("Total Purchased:", total)
discount = total*0.10
loyalty = total/10
new_total = float(total-discount)

if total > 100.00:
    print("You qualified for a discount!: ", discount)
else:
    print("Your total did not qualify for a Discount...")
    
print("New Total Purchased:", new_total)
print("Loyalty Points Earned:", loyalty)


payment = int(input("Enter your Payment:"))
if payment > new_total:
    print("Change:", payment - new_total)
else:
    print("Payment Failed...")
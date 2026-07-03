amount = float(input("Enter bill amount: "))
people = int(input("No. of people splitting :"))
Tip = int(input("Tip percentage: "))

Tip_amount = amount * (Tip / 100)
Total_bill = amount + Tip_amount
Per_Person = Total_bill / people

print(f"=======BILL SUMMARY=======")
print(f"Bill amount         : Rs. {amount:.2f}")
print(f"Tip ({(Tip)}%)      : Rs. {Tip_amount:.2f}")
print(f"Total bill          : Rs. {Total_bill:.2f}") 
print(f"Per person          : Rs. {Per_Person:.1f}")

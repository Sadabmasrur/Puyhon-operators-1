amount=int(input("Enter the withdraw amount: "))

note100=amount//100
note50=(amount%100)//50
note10=((amount%100)%50)//10

print(f"100 Taka note needed: {note100}")
print(f"50 Taka note needed: {note50}")
print(f"10 Taka note needed: {note10}")
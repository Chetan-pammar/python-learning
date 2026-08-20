item = input("Enter your item here:")
price= int(input(" Enter the price of your item:"))
quantity = int(input("Enter the quantities brought:"))
Total =price*quantity
print("Total:\t",Total)
if Total >= 5000:
   discount = Total*0.1
   print(f"Discount:\t{discount}\nFinal Bill:\t{Total-discount}")
else:
   print(f"Discount:\t0\nFinal Bill:\t{Total}")

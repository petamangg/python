#input product name , quantity , rate to display product name , ammount . discount , taxable ammount , vat ,
#and net ammount
productName=input("Enter the Product Name : ")
quantity = float(input("Enter the Quantity : "))
rate = int(input("Enter the Rate : "))
ammount = quantity * rate
discount = ammount * 5 / 100
taxableammount= ammount-discount
vat = taxableammount*13/100
netammount = taxableammount + vat

print(f"{productName} , Discount : {discount} , Taxable Ammount : {taxableammount} , VAT : {vat} , Net Ammount : {netammount}")
print("--------------------------------------------------------------------------------------")


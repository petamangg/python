# WAP to input previous unit and current unit
# to find consumed unit, payable amount, VAT and net amount

PU = float(input("Enter the Previous Unit : "))
CU = float(input("Enter the Current Unit : "))

consumedUnit = CU - PU

rate = 10
payableAmount = consumedUnit * rate

vat = payableAmount * 13 / 100
netAmount = payableAmount + vat

print(f"Consumed Unit : {consumedUnit} , Previous Unit : {PU} , Current Unit : {CU} , Payable Ammount : {payableAmount} ,VAT : {vat} , Net Ammount : {netAmount}")
from decimal import Decimal

amount = Decimal(input("Please, enter amount of money.\nIn HRN: "))
print(f"In USD: {(amount / Decimal('36.93')).quantize(Decimal('1.00'))}")

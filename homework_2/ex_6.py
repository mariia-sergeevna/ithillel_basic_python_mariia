from math import cos, sqrt


number = float(input("Enter number: "))
cos_number = cos(number)
sin_number = sqrt(1 - (cos_number**2))
tg_number = sin_number / cos_number
print(f"tan(x): {tg_number}")

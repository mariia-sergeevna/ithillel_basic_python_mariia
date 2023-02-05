def calculate_digits_from_string(number: str) -> int:
    sum_digits = 0
    for index in range(len(number)):
        sum_digits += int(number[index])
    return sum_digits


def calculate_digits_from_int(number: int) -> int:
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits


number = input("Enter number: ")

print(calculate_digits_from_string(number))
print(calculate_digits_from_int(int(number)))

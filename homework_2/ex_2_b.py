# without math.sqrt
def find_roots(a, b, c):
    discriminant = ((b**2) - (4 * a * c)) ** 0.5
    root_1 = (-b + discriminant) / (2 * a)
    root_2 = (-b - discriminant) / (2 * a)
    return f"x_1 = {root_1},\nx_2 = {root_2}"


print(find_roots(2, 5, 2))

def calculate_fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    prev, cur = 0, 1
    cur_idx = 2
    while cur_idx <= n:
        cur += prev
        prev = cur - prev
        cur_idx += 1
    return prev


def main() -> None:
    user_input = int(input("Enter desired value: "))
    result = calculate_fibonacci(user_input)
    print(f"{user_input} element in fibonacci" f" is {result}")


if __name__ == "__main__":
    main()

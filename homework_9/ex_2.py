from random import randint


def diff_odd_even(num_limit: int, lower_bound: int, upper_bound: int) -> int:
    random_nums = [randint(lower_bound, upper_bound) for _ in range(num_limit)]
    sum_even = sum([num for num in random_nums if not num % 2])
    sum_odd = sum([num for num in random_nums if num % 2])
    return sum_even - sum_odd


def main() -> None:
    low_bound, up_bound = map(
        int, input("Enter lower and upper bound of random nums: ").split()
    )
    n_limit = int(input("Enter count of numbers: "))
    result = diff_odd_even(n_limit, low_bound, up_bound)
    print(f"Difference between sum even and sum odd random numbers:\n{result}")


if __name__ == "__main__":
    main()

from random import randint


def diff_min_max(num_limit: int, lower_bound: int, upper_bound: int) -> int:
    random_nums = [randint(lower_bound, upper_bound) for _ in range(num_limit)]
    return max(random_nums) - min(random_nums)


def diff_min_max_sorted(num_limit: int, lower_bound: int, upper_bound: int) -> int:
    random_nums = sorted([randint(lower_bound, upper_bound) for _ in range(num_limit)])
    return random_nums[-1] - random_nums[0]


def main() -> None:
    low_bound, up_bound = map(
        int, input("Enter lower and upper bound of random nums: ").split()
    )
    n_limit = int(input("Enter count of numbers: "))
    result_built_in = diff_min_max(n_limit, low_bound, up_bound)
    res_sorted = diff_min_max_sorted(n_limit, low_bound, up_bound)
    print(f"Difference between max and min elements:\n{result_built_in}\n{res_sorted}")


if __name__ == "__main__":
    main()

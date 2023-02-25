def gen_primes() -> list:
    prime_numbers = []
    for num in range(3, 101, 2):
        for item in prime_numbers:
            if not num % item:
                break
        else:
            prime_numbers.append(num)
    return prime_numbers


def main() -> None:
    result = gen_primes()
    print(f"List of prime numbers from 1 to 100:\n{result}")


if __name__ == "__main__":
    main()

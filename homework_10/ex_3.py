from random import shuffle


def pemrtuate(text: str) -> str:
    """
    Get a keyboard text input and permute each word in this text.
    """
    words = text.split()
    result = ""

    for word in words:
        if len(word) <= 3:
            result += word + " "
            continue

        result += word[0]
        for idx in range(1, len(word) - 1, 3):
            if len(word) - 1 - idx == 1:
                result += word[idx]
                break

            if len(word) - 1 - idx == 2:
                if word[idx] == word[idx + 1]:
                    result += word[idx : idx + 2]
                    break
                result += word[idx + 1] + word[idx]
                continue

            if word[idx] == word[idx + 1] and word[idx] == word[idx + 2]:
                result += word[idx : idx + 3]
                continue

            shuffle_chars = list(word[idx : idx + 3])

            while shuffle_chars == list(word[idx : idx + 3]):
                shuffle(shuffle_chars)

            result += "".join(shuffle_chars)
        result += word[-1] + " "

    return result


def main() -> None:
    input_text = input("Enter text to permute words: ")

    while not input_text:
        print("You entered an empty string.")
        input_text = input("Enter text to permute words: ")

    result = pemrtuate(input_text)
    print(f"Text with permuted words:\n{result}")


if __name__ == "__main__":
    main()

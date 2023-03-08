from random import shuffle


def pemrtuate(text: str) -> str:
    """
    Get a keyboard text input and permute each word in this text.
    """
    words = text.split()
    result = []

    for word in words:
        shuffle_word = []
        if len(word) <= 3:
            result.append(word)
            continue

        shuffle_word.append(word[0])
        last_idx = len(word) - 1
        for idx in range(1, last_idx, 3):
            if last_idx - idx == 1:
                shuffle_word.append(word[idx])
                break

            if last_idx - idx == 2:
                if word[idx] == word[idx + 1]:
                    shuffle_word.append(word[idx : idx + 2])
                    break
                shuffle_word.append(word[idx + 1] + word[idx])
                continue

            if word[idx] == word[idx + 1] and word[idx] == word[idx + 2]:
                shuffle_word.append(word[idx : idx + 3])
                continue

            shuffle_chars = list(word[idx : idx + 3])

            while shuffle_chars == list(word[idx : idx + 3]):
                shuffle(shuffle_chars)

            shuffle_word.extend(shuffle_chars)

        shuffle_word.append(word[-1])
        result.append("".join(shuffle_word))

    return " ".join(result)


def main() -> None:
    input_text = input("Enter text to permute words: ")

    while not input_text:
        print("You entered an empty string.")
        input_text = input("Enter text to permute words: ")

    result = pemrtuate(input_text)
    print(f"Text with permuted words:\n{result}")


if __name__ == "__main__":
    main()

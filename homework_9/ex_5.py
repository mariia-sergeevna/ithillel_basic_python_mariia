from collections import Counter


def group_by_surname(list_of_enrollees: list):
    first_words = Counter([i.split()[1][0] for i in list_of_enrollees])
    groups = {
        range(ord("A"), ord("I") + 1): 0,
        range(ord("J"), ord("P") + 1): 0,
        range(ord("Q"), ord("T") + 1): 0,
        range(ord("U"), ord("Z") + 1): 0,
    }
    for word in first_words:
        for key in groups.keys():
            if ord(word) in key:
                groups[key] += 1
    return groups.values()


def main():
    students = ["Will Smith", "Jay Z"]
    result = group_by_surname(students)
    for idx, num in enumerate(result):
        print(f"In {idx + 1} group - {num} students")


if __name__ == "__main__":
    main()

def group_by_surname(list_of_enrollees: list):
    first_words = [i.split()[1][0].upper() for i in list_of_enrollees]
    groups = {
        "ABCDEFGHI": 0,
        "JQKLMNOP": 0,
        "QRST": 0,
        "UVWXYZ": 0,
    }
    for word in first_words:
        for key in groups.keys():
            if word in key:
                groups[key] += 1
    return groups.values()


def main():
    students = ["Will Smith", "Jay Z", "Lola Braun"]
    result = group_by_surname(students)
    for idx, num in enumerate(result):
        print(f"In {idx + 1} group - {num} students")


if __name__ == "__main__":
    main()

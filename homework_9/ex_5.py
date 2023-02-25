def group_by_surname(list_of_enrollees: list) -> list:
    result = [0] * 4
    group_1 = "ABCDEFGHI"
    group_2 = "JQKLMNOP"
    group_3 = "QRST"
    for student in list_of_enrollees:
        first_word = student.split()[1][0].upper()
        if first_word in group_1:
            result[0] += 1
        elif first_word in group_2:
            result[1] += 1
        elif first_word in group_3:
            result[2] += 1
        else:
            result[3] += 1
    return result


def main():
    students = ["Will Smith", "Jay Z", "Lola Braun"]
    result = group_by_surname(students)
    for idx, num in enumerate(result):
        print(f"In {idx + 1} group - {num} students")


if __name__ == "__main__":
    main()

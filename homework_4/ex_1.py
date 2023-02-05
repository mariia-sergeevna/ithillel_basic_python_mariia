def switch_to_capitalize_case(text: str) -> str:
    list_of_words = text.split("_")
    return "".join([word.title() for word in list_of_words])


text = input("Enter text in snake_case: ")
print(f"Text in capitalize case: {switch_to_capitalize_case(text)}")

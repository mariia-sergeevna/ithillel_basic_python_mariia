entered_string = input("Enter string: ")

print(f"Third string characters: {entered_string[2]}")
print(f"Penultimate string character: {entered_string[-2]}")
print(f"First 5 string characters: {entered_string[:5]}")
print(f"String without 2 last characters: {entered_string[:-2]}")
print(f"Characters with even indexes: {entered_string[::2]}")
print(f"Characters with odd indexes: {entered_string[1::2]}")
print(f"Characters in reverse order: {entered_string[::-1]}")
print(f"All string characters by one in reverse order: {entered_string[::-2]}")
print(f"Length of string: {len(entered_string)}")

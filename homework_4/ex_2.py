person_data = input("Enter information about person: ")
period = person_data.split("*")[2:0:-1]
age = int(period[0][:4]) - int(period[1][:4])

print(f"Name: {person_data.split('*')[0]}")
print(f"Age: {age} years")

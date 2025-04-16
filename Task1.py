mar_dict = {'Samadhan':80,'Ramesh': 40,'Alice':85}

studentname = input("Enter the student's name: ")

if studentname in mar_dict:
    print(f"{studentname}'s marks: {mar_dict.get(studentname)}")
else:
    print(f"Student not found.")

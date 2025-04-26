user_input = input("Enter text to write to the file: ")

file1 = open('output.txt',"w")
file1.write(user_input)
print(f"Data successfully written to output.txt.\n")
file1.close

additional_Data = input("Enter additional text to append: ")
file1 = open('output.txt',"a")
file1.write("\n" + additional_Data)
print(f"Data successfully appended.\n")
file1.close

file1 = open('output.txt',"r")
content = file1.read()
print(f"Final content of output.txt:\n{content}")
file1.close
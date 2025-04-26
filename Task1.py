
filename = 'sample.txt'
try:
    file1 = open(filename,"r")
    reading_file = file1.read()
    print(f"Reading file content:\n{reading_file}")
except FileNotFoundError:
    print(f"The file {filename} was not found.")
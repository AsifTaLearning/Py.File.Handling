#  File Open
# Open a File on the Server - step 1

f = open("demofile.txt", "r")

print(f.read())

# Another example

f = open("D:\Code\Python\Python file handling\demofile.txt", "r")

print(f.read())

# Read Only Parts of the File

f = open("demofile.txt", "r")

print(f.read(5))

# Read Lines

f = open("demofile.txt", "r")

print(f.readline())

# Another example

f = open("demofile.txt", "r")

print(f.readline())
print(f.readline())

# Another example

f = open("demofile.txt", "r")

for x in f:
  
  print(x)

# Close Files

f = open("demofile.txt", "r")

print(f.readline())

f.close()
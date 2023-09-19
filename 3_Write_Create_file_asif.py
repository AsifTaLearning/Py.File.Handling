# File Write
# Write to an Existing File

"a" # - Append - will append to the end of the file

"w" # - Write - will overwrite any existing content

f = open("demofile.txt", "a")

f.write("\n Now the file has more content!")

f.close()

f = open("demofile.txt", "r") # open and read the file after the appending:

print(f.read())

# Another example

f = open("demofile2.txt", "w")

f.write("Woops! I have deleted the content!")

f.close()

f = open("demofile2.txt", "r") # open and read the file after the overwriting:

print(f.read())

# Create a New File

"x" # - Create - will create a file, returns an error if the file exist

"a" # - Append - will create a file if the specified file does not exist

"w" # - Write - will create a file if the specified file does not exist

f = open("myfile.txt", "x")

# Another example

f = open("myfile.txt", "w")



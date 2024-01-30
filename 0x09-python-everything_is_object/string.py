# string.py

a = "SCHL"

# Counting the number of string objects created by the execution of the first line
with open("106-line1.txt", "w") as f:
    f.write("1")

b = "SCHL"

# Counting the number of string objects created by the execution of the second line
with open("106-line2.txt", "w") as f:
    f.write("1")

del a

# Checking if the string object pointed by 'a' is deleted after line 3
with open("106-line3.txt", "w") as f:
    f.write("Yes")

del b

# Checking if the string object pointed by 'b' is deleted after line 4
with open("106-line4.txt", "w") as f:
    f.write("Yes")

c = "SCHL"

# Counting the number of string objects created by the execution of the last line
with open("106-line5.txt", "w") as f:
    f.write("1")

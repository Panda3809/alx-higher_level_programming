#int.py

a = 1
b = 1

# Counting the number of int objects created by each line
with open("103-line1.txt", "w") as f:
    f.write("2")

a = 1024
b = 1024
del a
del b
c = 1024

# Counting the number of int objects created by each line
with open("103-line2.txt", "w") as f:
    f.write("3")

# int.py

import sys

print("I")

# Counting the number of int objects before line 2
with open("105-line1.txt", "w") as f:
    # Counting the number of small positive and negative int objects
    num_small_posints = sys.getsizeof(range(sys.maxsize)) // sys.getsizeof(1)
    num_small_negints = sys.getsizeof(range(-sys.maxsize - 1, 0)) // sys.getsizeof(-1)
    total_small_ints = num_small_posints + num_small_negints

    f.write(str(total_small_ints))
    # Optional explanation for why this number is reported

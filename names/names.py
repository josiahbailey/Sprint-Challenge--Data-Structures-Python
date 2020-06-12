import time
import sys
sys.setrecursionlimit(10**6)

start_time = time.time()


# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         if len(self.value) > len(value):
#             if not self.left:
#                 self.left = BSTNode(value)
#             else:
#                 self.left.insert(value)
#         elif len(self.value) <= len(value):
#             if not self.right:
#                 self.right = BSTNode(value)
#             else:
#                 self.right.insert(value)

#     def contains(self, value):
#         if self.value is value:
#             return True
#         elif self.right and len(self.value) <= len(value):
#             return self.right.contains(value)
#         elif self.left and len(self.value) >= len(value):
#             return self.left.contains(value)
#         else:
#             return False


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = [x for x in names_1 if x in names_2]
# duplicates = [name for name in (set(names_1) & set(names_2))]

# duplicates = []

# for x in names_1:
#     if x in names_2:
#         duplicates.append(x)

# node = BSTNode("Josiah Bailey")
# for name_1 in names_1:
#     node.insert(name_1)

# for name_2 in names_2:
#     if node.contains(name_2):
#         duplicates.append(name_2)

# counter = 0
# for i in range(10000):
#     name_1 = names_1[counter]
#     name_2 = names_2[counter]
#     print(name_1, name_2)
#     if name_1 == name_2:
#         duplicates.append(name_1)
#     counter += 1

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

duplicates = [name for name in (set(names_1) & set(names_2))]

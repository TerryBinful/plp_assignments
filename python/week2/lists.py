# Name: Terry
# Module: Python
# Assignment: Week 2
# Title: Python Built-In Data Structures


# 1. Create an empty list called my_list.
my_list = []

# 2.Append the following elements to my_list: 10, 20, 30, 40.
list_values = [10, 20, 30, 40]
for value in list_values:
    my_list.append(value)

# 3. Insert the value 15 at the second position in the list.
my_list[1] = 15

# 4. Extend my_list with another list: [50, 60, 70]
another_list = [50, 60, 70]
    # could use this - my_list.extend(another_list)
my_list = my_list + another_list

# 5. Remove the last element from my_list.
my_list.pop()

# 6. Sort my_list in ascending order.
my_list.sort()

# 7. Find and print the index of the value 30 in my_list.
print(my_list.index(30))

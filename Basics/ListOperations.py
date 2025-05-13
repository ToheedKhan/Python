
my_list = [99, 100, 4, 6, 12]

# Creating a new list of squares of each element

new_list = []

for ele in my_list:
    new_list.append(ele ** 2)

print(new_list)

# List Comprehension

new_List2 = [ele**2 for ele in my_list]

print(new_List2)

# Heterogenous element

my_list2 = [4, True, 4.5, [4, 5, 6], "str"]
print(len(my_list2))

# 2D List
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_2d)
print( list_2d[1])
print( list_2d[1][0])

# To access last element in 2 row
print( list_2d[1][-1])

my_list.sort()
print("My list after sorting: ", my_list)
print("Second Largest element: ", my_list[1])


lst = ['apple', 'orange', 'grapes', 'kiwi']
print( list( map(len, lst) ) )

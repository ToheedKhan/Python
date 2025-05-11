def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


lst = [1, 2, 3, 4, 5, 1, 2, 3]
print(remove_duplicates(lst))

#Outputs : print unique numbers from the list separated by spaces.
print(" ".join(str(x) for x in remove_duplicates(lst)))
#end="" tells print() not to add a newline (\n).
print(" ".join(str(x) for x in remove_duplicates(lst)), end="")

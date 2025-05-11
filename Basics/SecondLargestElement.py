import sys
# lst = [int(i) for i in sys.argv[1].split()]

# lst = [5, 3, 7, 2, 1, 9]
lst = [1, 1, 1, 1, 1, 1]



# Write your logic Here

if(len(lst) >= 2):
    lst.sort()
    print(lst[1])
else:
  print("None")

def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

nums = [10, 20, 4, 45, 99, 99]
print(second_largest(nums))
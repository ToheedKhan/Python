
input = ['a' , 'b' , 'a' , 'c' , 'a' , 'b' , 'd' , 'c', 'a']

my_set = set(input)

my_dic = {}

for i in my_set:
    count = 0
    for j in input:
        if i == j:
            count += 1
    my_dic[i] = count
print(my_dic)
max_value = max(my_dic.values())
max_key = [k for k, v in my_dic.items() if v == max_value]
print(max_key)

# Other way
from collections import Counter

def max_occurrence_element(lst):
    count = Counter(lst)
    most_common = count.most_common(1)[0]  # Returns (element, frequency)
    return most_common[0]

# Example usage
lst = [1, 2, 2, 3, 3, 3, 4]
print("Max occurring element:", max_occurrence_element(lst))


# Other way

def max_occurrence_element1(lst):
    freq = {}
    
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    max_count = 0
    max_element = None

    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            max_element = key

    return max_element

# Example usage
lst = [1, 2, 2, 3, 3, 3, 4]
print("Max occurring element:", max_occurrence_element1(lst))

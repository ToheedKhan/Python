import sys
# keys = [i for i in sys.argv[1].split()]
# values = [int(i) for i in sys.argv[2].split()]
keys = [1, 2, 3, 4, 5]
values = ['p', 'q', 'r', 's', 't']

dic = dict()
for i in range(len(keys)):
    dic[keys[i]] = values[i]
    

# Write your logic Here
reversed_d = {value: key for key, value in dic.items()}

print(reversed_d)
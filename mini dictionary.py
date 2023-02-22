dict={}
dict_start=input('Enter the starting alphabet from a to z : ')
dict_end=input('Enter the ending alphabet from a to z : ')
for i in range(ord(dict_start),ord(dict_end)+1):
    dict[chr(i)] = i
print(dict)

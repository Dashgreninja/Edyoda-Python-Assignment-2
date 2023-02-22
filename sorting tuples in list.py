def index(n):
    global ind
    return n[ind]

l=[]
tup=int(input("Enter how many tuples you want : "))
for i in range(tup):
    l.append(tuple(input('Enter no.s in n1,n2 format : ').split(',')))
    
ind=int(input('Enter the index you want to sort with : '))

print("Sorted list of Tuples:",end=' '),  
print(sorted(l, key = index))

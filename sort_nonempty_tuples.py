
tup1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lst1 =[]
lst2 =[]

for t in tup1:
    lst1.append(t[1],)

lst1.sort()

for l in lst1:
    for q in tup1:
        if l == int(q[1],):
            lst2.append(q)

print(lst2)















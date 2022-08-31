a = list()
n = int(input("rows: "))
m = int(input("columns: "))
k = int(input("k-row: "))
count = False

for i in range(n):
    a.append(list())
    for j in range(m):
        numb = int(input())
        a[i].append(numb)

for i in range(m):
    if len(a) > 1:
        if a[k-1][-m+i] < a[k-1][-m+i+1]:
            count = True
        else:
            count = False
    else:
        count = False

print("Array:", a)
print("Vector B", a[k-1])
if count == True:
    print("Vector B's decreasing.", int(count))
else:
    print("Vector B's not decreasing.", int(count))
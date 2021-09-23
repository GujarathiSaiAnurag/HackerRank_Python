n1 = int(input(""))
a = set(map(int , input("").split(" ")))
n2 = int(input(""))
b = set(map(int , input("").split(" ")))
c = set(a.union(b))
output =0
for i in c:
    output+=1

output = str(output)
print(output)

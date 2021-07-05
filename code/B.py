set1=set()
k=0
while True:
    line = input()
    if not line: 
        break
    else:
        set1.add(line)
for i in set1:
    k=k+1
print(k)
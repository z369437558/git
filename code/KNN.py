n=int(input())
x=[]
y=[]
class1=[]
distance1=[]
for i in range(n):
    a=input()
    a=a.split(' ',2)
    x1,y1,class11=a
    x.append(float(x1))
    y.append(float(y1))
    class1.append(class11)
    distance1.append((x[i]-0.6)**2+(y[i]-0.3)**2)
knn=[[distance1[i],class1[i]] for i in range(n)]
atot=0
btot=0
def take(elem):
    return elem[0]
knn.sort(key=take)
k=3
for i in range(k):
    if(knn[i][1]=='A'):
        atot=atot+1
    if(knn[i][1]=='B'):
        btot=btot+1
if(atot>btot):
    print("A")
else:
    print("B")
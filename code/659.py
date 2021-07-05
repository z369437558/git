num=[1,2,3,3,4,5]
n=len(num)
a=[0 for i in range(n+1)]
b=[0 for i in range(n+1)]
for i in range(1,n+1):
    a[i]=num[i-1]
def search(goal,pp):#找下一个
    if(pp>n):
        return -1
    for i in range(pp,n+1):
        if(a[i]==goal) and (b[i]==0):
            return i
        if(a[i]>goal):
            return -1
    return -1
def find1(po):#找一个子序列
    count=0
    while(po<n):
        next1=search(a[po]+1,po+1)
        if(next1!=-1):
            b[next1]=1
            po=next1
            count=count+1
        if(next1==-1)and (a[po]==max1):
            break
    if(a[po]==max1):
        count=count+1
    if(count<3):
        return -1
    else:
        return 0
ans=1
max1=0
for i in range(1,n+1):
    if(max1<a[i]):
        max1=a[i]
for i in range(1,n+1):
    if(b[i]==0):
        b[i]=1
        if(find1(i)==-1):
            ans=-1
            break
if(ans==1):
    print('True')
else:    
    print('False')
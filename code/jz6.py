a=input()
a=a.split(' ',4)
def find(l,r):
    if l==r:
        return l
    mid=(l+r)//2
    if a[mid]>a[l] and a[mid]>a[r]:
        return find(mid+1,r) 
    else:
        return find(l,mid)

ans=find(0,len(a)-1)
print(a[ans])
    
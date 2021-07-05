a=input()
a=a.split(' ',1)
a=list(map(int,a))
T,M=a
t=[0 for i in range(150)]
w=[0 for i in range(150)]
for i in range(M):
    a=input()
    a=a.split(' ',1)
    a=list(map(int,a))
    t[i+1],w[i+1]=a
import numpy as np
f=np.zeros((M+1,T+1),dtype=int)
for i in range(1,M+1):
    for j in range(1,T+1):
        if j-t[i]>=0:
            f[i][j]=max(f[i-1][j-t[i]]+w[i],f[i-1][j])
        else:
            f[i][j]=f[i-1][j]
print(f[M][T])
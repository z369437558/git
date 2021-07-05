a=input()
v=int(a)
a=input()
n=int(a)
w=[0]
import numpy as np
f=np.zeros((n+1,v+1),dtype=int)
for i in range(n):
    a=input()
    w.append(int(a))
for i in range(1,n+1):
    for j in range(1,v+1):
        if j-w[i]>=0:
            f[i][j]=max(f[i-1][j-w[i]]+w[i],f[i-1][j])
        else:
            f[i][j]=f[i-1][j]
print(v-f[n][v])
    
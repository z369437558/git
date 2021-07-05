import numpy as np
f=np.ones((50,50),dtype=int)
a=input()
a=a.split(' ',1)
a=list(map(int,a))
n,k=a
s=input()
inshu=[['0' for i in range(50)]for j in range(50)]

f[1][0]=int(s[0])
inshu[1][0]=s[0]
for i in range(1,n+1):
    for j in range(1,min(i,k+1)):
        if(inshu[i-1][j]!='0'):
            if f[i-1][j]//int(inshu[i-1][j])*int(inshu[i-1][j]+s[i-1])>f[i-1][j-1]*int(s[i-1]):
                inshu[i][j]=inshu[i][j-1]+s[i-1]
                if inshu[i][j-1]=='0':
                    f[i][j]=f[i-1][j]*int(s[i-1]) 
                else:
                    f[i][j]=f[i-1][j]//int(inshu[i-1][j])*int(inshu[i-1][j]+s[i-1])
            else:
                inshu[i][j]=s[i-1]
                f[i][j]=f[i-1][j-1]*int(s[i-1])
        else:
            if f[i-1][j]*int(inshu[i-1][j]+s[i-1])>f[i-1][j-1]*int(s[i-1]):
                inshu[i][j]=inshu[i][j-1]+s[i-1]
                if inshu[i][j-1]=='0':
                    f[i][j]=f[i-1][j]*int(s[i-1]) 
                else:
                    f[i][j]=f[i-1][j]//int(inshu[i-1][j])*int(inshu[i-1][j]+s[i-1])
            else:
                inshu[i][j]=s[i-1]
                f[i][j]=f[i-1][j-1]*int(s[i-1])
print(f[n][k])

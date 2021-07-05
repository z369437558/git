import numpy as np
a=input()
m,n=a.split(' ',1)
m=int(m)+1
n=int(n)
gongxucounter=[0 for i in range(m)]
a=input()
machinenum=jiagongtime=np.zeros((n,m),dtype=int)
b=np.zeros((m,8080),dtype=int)
q=a.split(' ',m*n-1)
q=list(map(int,q))
for i in range(n):
    a=input()
    machinenum[i]=a.split(' ',m-2)
for i in range(n):
    a=input()
    jiagongtime[i]=a.split(' ',m-2)

for i in range(len(q)): #q[i]是产品号 gongxucounter[q[i]]是工序
    if i==0 or q[i]!=q[i-1]: #从最左边找空位
        timecost=jiagongtime[gongxucounter[q[i]]] #获得时间
        machinenumnow=machinenum[q[i]][gongxucounter[q[i]]]
        gongxucounter[q[i]]=gongxucounter[q[i]]+1 #往后推工序号
        for j in range(1,8010):
            if(b[machinenumnow][j]==0):
                counter=0
                flag=0
                if counter+j>=8010:
                    flag=1
                else:
                    while(counter<timecost):
                        if b[machinenumnow][j+counter]==1:
                            flag=1
                            break
                        counter=counter+1
                if flag==0:
                    for k in range(j,j+counter):
                        b[machinenumnow][k]=1
                    rightboundry=j+counter
                    break
    else: #从上一个工序的右边界开始找空位
        timecost=jiagongtime[gongxucounter[q[i]]] #获得时间
        machinenumnow=machinenum[q[i]][gongxucounter[q[i]]]
        gongxucounter[q[i]]=gongxucounter[q[i]]+1 #往后推工序号
        for j in range(rightboundry,8010):
            if(b[machinenumnow][j]==0):
                counter=0
                flag=0
                while(counter>=timecost):
                    if b[machinenumnow][j+counter]==1:
                        flag=1
                        break
                if flag==0:
                    for k in range(j,j+counter):
                        b[machinenumnow][k]=1
                    break
max1=0
for i in range(n):
    for j in range(8010):
        if b[i][8010-j]==1 and 8010-j>max1:
            max1=8010-j
            break
print(max1)




    
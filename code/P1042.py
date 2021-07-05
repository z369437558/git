x=y=x1=y1=0
flag=0
import math
import queue
q = queue.Queue()
while flag==0:
    a1 = input()
    b=len(a1)
    for i in range(len(a1)):
        a=a1[i]
        if a=='E':
            print(x,':',y,sep='')
            q.put(x1)
            q.put(y1)
            flag=1
            break
        else:
            if a=='W':
                x=x+1
                x1=x1+1
            if a=='L':
                y=y+1
                y1=y1+1
            if (x>=11 or y>=11) and (abs(x-y)>=2):
                print(x,':',y,sep='')
                x=y=0
            if (x1>=21 or y1>=21) and (abs(x1-y1)>=2):
                q.put(x1)
                q.put(y1)
                x1=y1=0
print('')
while not q.empty():
    x1=q.get()
    y1=q.get()
    print(x1,':',y1,sep='')




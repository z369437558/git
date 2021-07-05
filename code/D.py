import random
ans=[0,0,0,0,0,0,0,0]
while True:
    a = int(input())
    if  a== 0:
        break
    else:
        ans1=0
        for i in range(1,7):
            ans[i]=0
        for i in range(a):
            aa=random.randint(1,6)
            ans[aa]=ans[aa]+1
        for i in range(1,7):
            print("{}: {}".format(i,ans[i]))
            ans1=ans1+i*ans[i]
        print("Mean: {:.2f}".format(ans1/a))




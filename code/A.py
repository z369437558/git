def partition(arr,low,high): 
    i = (low-1)        
    pivot = arr[high]     
    for j in range(low,high): 
        if   arr[j] >= pivot:   
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return (i+1)
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
k=0
a=[0 for i in range(100100)]
while True:
    a[k] = input()
    if  not a[k]:
        break
    else:
         a[k]=int(a[k])
         k=k+1
n=k
quickSort(a,0,n-1)
for i in range(0,n):
    print(a[i])

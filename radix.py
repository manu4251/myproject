def counting(a,place):
  size=len(a)
  output=[0]*size
  count=[0]*10
for i in range(0,size):
   index=a[i]//place
   count[index%10]+=1
for i in range(1,10):
   count[i]+=count[i-1]
i=size-1
while i>=0:
    index=a[i]//place
    output[count[index%10]-1]=a[i]
    count[index%10]-=1
    i-=1
for i in range(0,size):
    a[i]=output[i]
def radixsort(a):
   maxe=max(a)
   place=1
   while maxe//place>0:
       countingsort(a,place)
       place*=10
data=[121,432,564,23,1,45,788]
radixsort(data)
print(data)

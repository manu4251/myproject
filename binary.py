def binary(l,low,high,key):
   while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
             return mid
        elif l[mid]>key:
             high=mid-1
        else:
             low=mid+1
   return -1
l=[]
x=int(input("enter the no.of elements:"))
for i in range(x):
   z=int(input("enter the elements:"))
   l.append(z)
print(l)
n=len(l)
L=0
h=n-1
key=int(input("enter the key value:"))
y=binary(l,L,h,key)
if y==-1:
  print("element is not found")
else:
  print("element is found at index:",y)

def insert_s(a):
  for i in range(1,len(a)):
    j=i-1
    temp=a[i]
    while a[j]>temp and j>=0:
       a[j+1]=a[j]
       j=j-1
    a[j+1]=temp
  print(a)
l=[]
n=int(input("enter no.of elements:"))
for i in range(n):
    x=int(input("enter the items:"))
    l.append(x)
print(l)
y=insert_s(l)
 


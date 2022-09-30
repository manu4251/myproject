def partition(a,lb,ub):
  pivot=a[lb]
  i=lb
  j=ub
  while(lb<=ub):
      while(i<=j and a[i]<=pivot):
         i=i+1
      while i<=j and a[j]>pivot:
         j=j-1
      if i<=j:
         a[i],a[j]=a[j],a[i]
      else:
         a[lb],a[j]=a[j],a[lb]
         return j
def quick(a,lb,ub):
    if lb<ub:
       pos=partition(a,lb,ub)
       quick(a,lb, pos-1)
       quick(a,pos+1,ub)
    else:
        return a
a=[12,54,78,32,1,2,4]
print(a)
quick(a,0,len(a)-1)
print(a)

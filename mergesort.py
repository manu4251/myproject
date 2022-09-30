def merge(a,l,mid,h):
      i=l
      j=mid+1
      k=0
      while i<=mid and j<=h:
        if a[i]<=a[j]:
           b[k]=a[i]
           i=i+1
        else:
           b[k]=a[j]
           j=j+1
        k=k+1
      while i<=mid:
        b[k]=a[i]
        i=i+1
        k=k+1
      while j<=h:
        b[k]=a[j]
        j=j+1
        k=k+1
def mergesort(a,l,h):
  if l<h:
    mid=(l+h)/2
    mergesort(a,l,mid)
    mergesort(a,mid+1,h)
    merge(a,l,mid,h)
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
l=0
h=len(arr)-1
print("Given array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergesort(arr, l, h)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
      

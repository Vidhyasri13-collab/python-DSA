#LINEAR SEARCH
#Element at particular position

def linearsearch(a,el):
  for i in range(len(a)):
    if a[i]==el:
      print(f'element is found at index {i}')
      return 
  print('element not found')
  

a=[12,11,44,15,23,1,4,5]
linearsearch(a,23)


#Element at particular index

def linearsearch(a,el):
  for i in range(len(a)):
    if a[i]==el:
      #print(f'element is found at index {i}')
      return i
  #print('element not found')
  return -1

a=[12,11,44,15,23,1,4,5]
print(linearsearch(a,15))


#Element at multiple indexes

def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i]==el:
      ar.append(i)
      #print(f'element is found at index {i}')
      #return i
  #print('element not found')
  return ar

a=[12,11,44,15,23,1,4,15]
res=linearsearch(a,15)
for i in res:
  print(i,end=" ")

#BINARY SEARCH

def binarysearch(a,el):
    l=0
    r=len(a)
    while l<r:
        m=(l+r)//2
        if l==m:
            return -1
        if a[m]==el:
            return m
        elif a[m]<el:
            l=m
        else:
            r=m
    #return -1


a=[2,4,8,14,13,17,18]
print(binarysearch(a,17))
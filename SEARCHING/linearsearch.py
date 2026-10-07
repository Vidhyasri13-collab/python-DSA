def linearsearch(x,el):
  index=[]
  for i in range(len(x)):
    if x[i]==el:
      index.append(i)
  if len(index)>0:
    print(index)
  else:
    print('no element found')

x=[3,2,3,4,3]
el=3


def maximum(a):
  max=a[0]
  for i in a:
    if i>max:
      max=i
  print(max)
def minimum(a):
  min=a[0]
  for i in a:
    if i<min:
      min=i
  print(min)    

a=[1,2,3,4,5]
linearsearch(x,el)
maximum(a)
minimum(a)


def subarrays(a):
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      print(f'[{a[i]},{a[j]}]')

print(a)
subarrays(a)


def sumpair(a,el):
  l=0
  r=len(a)-1
  for i in range(len(a)//2):
    if a[l]+a[r]==el:
      print(l,r)
    l+=1
    r-=1

a=[12,7,19,9,21,16]
target=28
sumpair(a,target)


def ispalindrome(a):
  l=0
  r=len(a)-1
  while l<r:
    if a[l]!=a[r]:
      return False
    l+=1
    r-=1
  return True

a='momsi'
print(ispalindrome(a))
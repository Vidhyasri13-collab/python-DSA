def calprefix(a):
  sum=a[0]
  res=[0 for _ in range(len(a))]
  res[0]=sum
  for i in range(1,len(a)):
    sum+=a[i]
    res[i]=sum
  return res

def rangesum(a,st,en):
  return (prefix[en]-prefix[st-1])

def sumarray(a,k,tar):
  s=0
  for i in range(k):
    s+=a[i]
  if s==tar:
    return [a[0],a[1],a[2]]

  for i in range(k,len(a)):
    s=s+a[i]-a[i-k]
    if s==tar:
      return [a[i-k+1],a[i-1],a[i]]

  return [-1,-1]


a=[1,2,3,4,5,6,7,8,9]
prefix=calprefix(a)
print(prefix)
print(rangesum(a,3,8))
print(sumarray(a,3,15))


def eqiInd(a):
  ts=sum(a)
  ls=0
  for i in range(len(a)):
    rs=ts-ls-a[i]
    if ls==rs:
      return i
    ls+=a[i]
  return -1


a=[-7,1,5,2,-4,3,0]
print(eqiInd(a))





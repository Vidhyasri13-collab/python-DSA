n=int(input())
if n<=0:
  print("Invalid size.size should be greater than zero")
else:
  arr=list(map(int,input().split(" ")))
  sum=0
  for i in range (n):
    sum+=arr[i]
  res=sum/n
  print(res)
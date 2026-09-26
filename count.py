n=int(input())
arr=list(map(int,input().split()))
ele=int(input())
c=0
for i in arr:
  if i==ele:
    c+=1
print(c)
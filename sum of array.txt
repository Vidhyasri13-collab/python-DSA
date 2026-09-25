def sumofarr(a):
  sum=0
  for i in a:
    sum+=i
  print(sum)

n=int(input())
a=[int(input()) for i in range(n)]
sumofarr(a)
n=int(input())
l=[int(i) for i in input().split()]
sum=0
c=0
for e in l:
    sum=sum+e
avg=sum//len(l)
for e in l:
    if e>=avg:
        c=c+1
print(c)
#задача2
a=int(input())
b=int(input())
count=0
max=max(a,b)
nac=max
min=min(a,b)
flag=0
while flag!=1:
    if max%min==0:
        count=max
        flag=1
    else:
        max=max+nac
print(count)
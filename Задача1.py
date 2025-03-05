a=int(input())
b=int(input())
c=int(input())
d=int(input())
string=''
for k in range(c,d+1):
    string+=str(k)+' '
print(' ', string)
for i in range(a, b+1):
    print(i, ')', end='', sep='')
    for j in range(c, d+1):
        print(i*j, end=' ')
    print()


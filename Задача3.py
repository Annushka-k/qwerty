string=input()
sim1=string[0]
newstring=''
count=0
for i in range(len(string)):
    if string[i]==sim1:
        count+=1
    else:
        print(sim1, count, sep='', end='')
        count=1
        sim1=string[i]
if string[len(string)-2] == string[-1]:
    print(string[-1], count, sep='', end='')
else:
    print(sim1, count, sep='', end='')
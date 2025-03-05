string=input()
substring=input()
lensubstring=len(substring)
lenstring=len(string)
count=0
for i in range(lenstring):
    sravnenie=string[i:lensubstring]
    if sravnenie==substring:
        count+=1
    #string=string[i+1:]
    lensubstring = lensubstring + 1

print(count)
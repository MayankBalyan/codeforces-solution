a=int(input())
b=str(input())
c=b.split()
even=0
odd=0
for i in c:
    
    if int(i)%2==0:
        even+=1
    elif int(i)%2!=0:
        odd+=1
    
if even>odd:
    for i in range(len(c)):
        if int(c[i])%2!=0:
            print(i+1)
            break
elif odd>even:
    for i in range(len(c)):
        if int(c[i])%2==0:
            print(i+1)
            break




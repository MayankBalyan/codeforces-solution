a=str(input())
U=0
L=0
for i in a:
    if i.islower():
        L+=1
    elif i.isupper():
        U+=1
if L>=U:
    print(a.lower())
elif U>L:
    print(a.upper())
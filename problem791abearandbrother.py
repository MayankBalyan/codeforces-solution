a=str(input())
b=a.split()
limak=int(b[0])
bob=int(b[1])
c=0

while limak<=bob:
    c+=1
    
    limak*=3
    bob*=2
if c==0:
    print(1)
else:
    print(c)
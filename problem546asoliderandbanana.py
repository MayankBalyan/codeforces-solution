a=str(input())
b=a.split()
c=[]
for i in b:
    c+=[int(i)]
k=c[0]
n=c[1]
w=c[-1]
d=k*(w)*(w+1)/2
if n>d:
    print('0')
else:
    print(int(d-n))

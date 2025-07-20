testcase=int(input())
ans=[]
for i in range(testcase):
    a=int(input())
    b=str(input())
    c=b.split()
    d,e=0,0
    if a==2:
        d,e=int(c[1]),int(c[0])
    if a>2 or (d-e)<=1:
        ans+=['NO']
    else:
        ans+=['YES']
for i in ans:
    print(i)
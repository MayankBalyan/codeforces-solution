t = int(input())
ans=[]
for i in range(t):
    n, s = map(int, input().split())
    positions = list(map(int, input().split()))
    L = min(positions)
    R = max(positions)
    result = min(abs(s - L), abs(s - R)) + (R - L)
    ans+=[result]
for i in ans:
    print(i)

a=str(input())
b=''
c=['a','e','i','o','u','y']
for i in a:
    if i.lower() not in c and i.isalpha():
        b+='.'+i.lower()
print(b)

a=input()
ans=0
temp=a
for i in range(3):
    ans+=int(temp)
    temp+=a
print(ans)
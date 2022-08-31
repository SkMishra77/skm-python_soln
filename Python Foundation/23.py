a=input("Enter Str")
n=int(input())
print(a*n if (len(a)<2) else (a[:2]*n))

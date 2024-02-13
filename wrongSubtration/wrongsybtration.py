data = [int(x) for x in input().split(" ")]
n = data[0]
for i in range(data[1]):
    if n%10==0:
        n=n//10
    else:
        n-=1
print(n)

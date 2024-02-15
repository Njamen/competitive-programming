n = int(input())
a = 0
s = 0
for i in range(n):
    data = [int(x)  for x in  input().split(" ")]
    s  = s - data[0] + data[1]
    if s > a:
        a = s
print(a)
    
    

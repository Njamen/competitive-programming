n = int(input())
rep = {}
for i in range(n):
    line = input().split(" ")
    rep[line[0]] =line[1]
while True:
    try:
        li = input()
        if li not in rep:
            print("Not found")
        else:
            print(f"{li}={rep[li]}")
    except EOFError: 
        break


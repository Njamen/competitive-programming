def swap_case(s):
    data = []
    for c in s:
        if c.islower():
            data.append(c.upper())
        elif c.isupper():
            data.append(c.lower())
        else:
            data.append(c)
    return "".join(data)
            
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

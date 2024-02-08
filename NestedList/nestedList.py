if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
    temp = sorted(student, key=lambda it: (it[1], it[0]))
    temp = [x for x in temp if x[1]!=temp[0][1]]
    temp = [x[0] for x in temp if x[1]==temp[0][1]]
    print("\n".join(temp))

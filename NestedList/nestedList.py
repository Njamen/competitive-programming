if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    temp = sorted(student,key=lambda it:(it[1],it[0]))
    temp2 = [x[0] for x in temp[1:] if x[1]==temp[1][1]]
    print("\n".join(temp2))

def grade(response, answer):

    assert len(answer) == len(response)

    points = 0
    wrong = []
    correct = []

    for i in range(len(answer)):

        if response[i] == 0:
            continue
        elif answer[i] == response[i]:
            points += 1
            correct.append(i+1)
        else:
            points -= 1
            wrong.append(i + 1)

    return points, wrong, correct

if __name__ == '__main__':

    solution = [-1, -1, 1, 1, -1, 1,1, -1, -1, 1, \
                1,1,1,1, -1, 1, -1, 1, -1, -1, \
                -1, 1, 1, -1, -1, -1, -1, 1, -1]

    student = [ 0 ] * 29

    lines = []
    with open("test.txt") as f:
        lines = f.readlines()

    qnum = 0
    jump = False
    you_answer = False
    for line in lines:
        if "Answer " in line and ":" in line:
            qnum = int(line.split(" ")[1].strip().strip(":"))
            jump = False
        elif jump:
            continue
        else:
            if "(You left this blank)" in line:
                jump = True
            elif "You Answered" in line or "Correct!" in line:
                you_answer = True
            elif "True" in line or "False" in line:
                if you_answer == True:
                    student[qnum-1] = 1 if "True" in line else -1
                    you_answer = False
            else:
                continue

    print(student)

    student = [-1, -1, 1, 1, 0, -1, 0, -1, -1, 0, \
                1,1,1,1, 0, 1, 0, 1, -1, 0, \
                -1, 0, -1, 0, -1, 0, -1, 0, -1]





    pt, wrong, correct = grade(student, solution)
    print(f"Q11: {pt} pts,\nwrong: {wrong}, \ncorrect: {correct}")

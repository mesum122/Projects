score = 0
questions = 3
counter = 1

print("Welcome to the quiz , kindly give answers in A/B/C/D form ")
answer = input("question {} answer : ".format(counter)).lower()

while True:
    match answer:
        case "a":
            score += 1
            counter += 1
            answer_2 = input("question {} answer : ".format(counter)).lower()
        case _:
            counter += 1
            answer_2 = input("question {} answer : ".format(counter)).lower()
            pass
    match answer_2:
        case "c":
            score += 1
            counter += 1
            answer_3 = input("question {} answer : ".format(counter)).lower()
        case _:
            counter += 1
            answer_3 = input("question {} answer : ".format(counter)).lower()
            pass
    match answer_3:
        case "d":
            score += 1
            counter += 1
            answer_4 = input("question {} answer : ".format(counter)).lower()
        case _:
            counter += 1
            answer_4 = input("question {} answer : ".format(counter)).lower()
            pass

    match answer_4:
        case "b":
            score += 1
            counter += 1

            break
        case _:
            counter += 1
            break

percentage = score * 25
print()
print("Thanks for taking this quiz, your score is", score)
detail = input("Do you want a detailed result? (yes / no) ").lower()

if detail == "yes":
    print()
    print("Answer to question 1 was a, you answered", answer)
    print("Answer to question 2 was c, you answered", answer_2)
    print("Answer to question 3 was d, you answered", answer_3)
    print("Answer to question 4 was b, you answered", answer_4)
    print("Final percentage is " + str(percentage) + "%")
else:
    print("Thanks for taking the exam , goodbye")

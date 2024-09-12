from random import randint

print("接下来是一场中超比赛，一共进行五轮，由人类方先进攻，随后攻守交换，若五轮后......")

#isover函数还没写出来，contest函数里面有很多都是重复的！，看看怎么改

def contest():
    myscore=0
    computerscore=0
    for i in range(0,5):
        mythink = int(input())
        computer_think = randint(0, 1)
        if isequal(mythink,computer_think):
            if i%2==0:
                myscore+=1
            else:
                computerscore+=1
    iswin(myscore,computerscore)


def iswin(myscore,computerscore):
    if myscore>computerscore:
        print("Oh, you wim!")
    elif myscore<computerscore:
        print("Haha, I win!")
    else:
        print("We have the same score, let's continue!")
        game_contiune()

def game_contiune():
    myscore = 0
    computerscore = 0
    i = 1
    while myscore==computerscore:
        mythink = int(input())
        computer_think = randint(0, 1)
        if isequal(mythink, computer_think):
            if i % 2 == 0:
                myscore += 1
            else:
                computerscore += 1
        i+=1
    if myscore > computerscore:
        print("Oh, you win the extra!")
    elif myscore < computerscore:
        print("Haha, I win the extra!")


def isequal(num1,num2):
    if num1!=num2:
        return True
    else:
        return False

contest()
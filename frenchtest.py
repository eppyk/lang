import random
import datetime
import time

def file_len(wordbank):
    #defines how many lines are there in an external file
    with open(wordbank) as f:
        for i, l in enumerate(f):
            pass
    return i

def append(b, c):
    #appends new words to the wordbank
    file = open("wordbank.py", "a")

    file.write("%s\n%s\n" %(b,c))

    file.close()

def saveAns (a, x, y):
    #saving answers with a date in chart.py

    if(a=="Y"):

        file = open("chart.py", "a")
        file.write( time.strftime("%x") + "\n" + "%d\n%d\n" % (x, y))
        file.close()


def test():
    #the test itself; checks if the answer is correct
    x = 0
    y = 0
    z = "1"
    while z == "1":
        d = raw_input("Do you want to be asked in Eng or French?\n")

        if d=="Eng":
            print "Please type the French translation of: "
            f=open('wordbank.py')
            e = file_len('wordbank.py')
            g = random.randrange(1, e+1, 2)
            lines=f.readlines()
            print lines[g]
            h = raw_input() + "\n"
            if(h == lines[g-1]):
                print "Good job!"
                x += 1
            else:
                print "Oh :( Wrong. The French translation is %s" % (lines[g-1])
                y += 1


        elif d=="French":
            print "Please type the English translation:"
            f=open('wordbank.py')
            e = file_len('wordbank.py')
            g = random.randrange(0, e+1, 2)
            lines=f.readlines()
            print lines[g]
            h = raw_input() + "\n"
            if(h == lines[g+1]):
                print "Good job!"
                x += 1
            else:
                print "Oh :( Wrong. The French translation is %s" % (lines[g+1])
                y += 1
        else:
            print "wrong"

        z = raw_input("Do you want to continue? \n 1 - Yes \n 2 - No, thanks\n")

    a = (x/(x+y))*100
    print "Had enough? You answered %d questions and your score is:\n %d good answers \n %d wrong answers. \n That makes %d percent good answers." % (x+y, x, y, a)

    sav = raw_input("Do you wanna save your answers? \n Y - Yes \n N - No\n")
    saveAns(sav, x, y)


def printScores():
    #this function prints all the saved scores by date
    f=open('chart.py')
    e = file_len('chart.py')
    lines=f.readlines()
    a = 1
    while a < e-2:
        print "date:" + lines[a] + " "
        print "      " + "good:" + lines[a+1] + " "
        print "      " + "bad:" + lines[a+2] + "\n"
        a += 3

def printSpecDate(date1):

    f=open('chart.py')
    e = file_len('chart.py')
    lines=f.readlines()
    z = 0
    for i in range(0, e):
        if lines[i]==date1:
            print lines[i] + "      " + "good: " + lines[i+1] + "      " + "wrong: " + lines [i+2]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # THE MAIN PROGRAM # # # # # # # # # #

a = input("Hey! What do you wanna do? \n 1 - add a new word to the bank \n 2 - test yourself \n 3 - see the scores \n 4 - see the scores from a specific day \n")

int(a)

if (a==1):

    b = raw_input("What should that word be?\n")
    str(b)
    c = raw_input("What is its meaning?\n")
    str(c)

    append (b, c)

elif a==2:
    test()

elif a==3:
    printScores()

elif a==4:
    print "What date do you wanna see?\n"

    day = input("Day (DD): ")
    month = input("Month (MM): ")
    year = input("Year (YY): ")

    date1 = time.strftime("%m/%d/%y\n")
    print "date obtained: " + date1
    printSpecDate(date1)

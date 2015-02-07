import random
import datetime
import time

def file_len(wordbank):
    i = 0
    #defines how many lines are there in an external file
    with open(wordbank) as f:
        for i, l in enumerate(f):
            pass
    return i

def append(lang, b, c):
    #appends new words to the specific wordbank
    file = open(lang + "wordbank.py", "a")

    file.write("%s\n%s\n" %(b,c))

    file.close()

def saveAns (lang, x, y):
    #saving answers with a date in Schart.py or Fchart.py, depends on the language

        file = open(lang + "chart.py", "a")
        file.write( time.strftime("%x") + "\n" + "%d\n%d\n" % (x, y))
        file.close()


def test(lang):
    #the test itself; checks if the answer is correct
    lang2 = "Spanish"

    if (lang=="F"):
        lang2 = "French"

    x = 0
    y = 0
    z = "1"
    while z == "1":
        d = input("Do you want to be asked in English (E) or %s (%s)?\n" %(lang2, lang))

        if d=="E":
            print ("Please type the %s translation of: " %(lang2))
            f = open(lang + "wordbank.py")
            e = file_len(lang + "wordbank.py")
            print(e)
            g = random.randrange(1, e+1, 2)
            lines=f.readlines()
            print (lines[g])
            h = input() + "\n"
            if(h == lines[g-1]):
                print ("Good job!")
                x += 1
            else:
                print ("Oh :( Wrong. The %s translation is %s" % (lang2, lines[g-1]))
                y += 1


        elif d == lang:
            print ("Please type the English translation:")
            f=open(lang + "wordbank.py")
            e = file_len(lang + "wordbank.py")
            g = random.randrange(0, e+1, 2)
            lines=f.readlines()
            print (lines[g])
            h = input() + "\n"
            if(h == lines[g+1]):
                print ("Good job!")
                x += 1
            else:
                print ("Oh :( Wrong. The %s translation is %s" % (lang2, lines[g+1]))
                y += 1
        else:
            print ("wrong")

        z = input("Do you want to continue? \n 1 - Yes \n 2 - No, thanks\n")

    a = (x/(x+y))*100
    print ("Had enough? You answered %d questions and your score is:\n %d good answers \n %d wrong answers. \n That makes %d percent good answers." % (x+y, x, y, a))

    sav = input("Do you wanna save your answers? \n Y - Yes \n N - No\n")

    if sav == "Y":
        saveAns(lang, x, y)

##
def printScores(lang):
    #this function prints all the saved scores by date
    print("i got here yeah")
    f=open(lang + 'chart.py')
    e = file_len(lang + 'chart.py')
    lines=f.readlines()
    a = 0
    while a < e-1:
        print ("date:" + lines[a] + " ")
        print ("      " + "correct:" + lines[a+1] + " ")
        print ("      " + "incorrect:" + lines[a+2] + "\n")
        a += 3

def printSpecDate(lang, date1):

    f=open(lang + 'chart.py')
    e = file_len('chart.py')
    lines=f.readlines()
    z = 0
    for i in range(0, e):
        if lines[i]==date1:
            print (lines[i] + "      " + "good: " + lines[i+1] + "      " + "wrong: " + lines [i+2])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # THE MAIN PROGRAM # # # # # # # # # #

lang = str(input("Which language are you gonna polish today? \n Write F for French or S for Spanish. \n"))

a = input("Nice! What do you wanna do? \n 1 - add a new word to the bank \n 2 - test yourself \n 3 - see the scores \n 4 - see the scores from a specific day \n")


if (a=="1"):
    b = str(input("What should that word be?\n"))

    c = str(input("What is its meaning?\n"))

    append (lang, b, c)

elif a=="2":
    test(lang)

elif a=="3":
    printScores(lang)

elif a=="4":
    print ("What date do you wanna see?\n")

    day = input("Day (DD): ")
    month = input("Month (MM): ")
    year = input("Year (YY): ")

    date1 = time.strftime("%m/%d/%y\n")
    print ("date obtained: " + date1)

    printSpecDate(lang, date1)

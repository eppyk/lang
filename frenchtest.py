import random

def file_len(wordbank):
    with open(wordbank) as f:
        for i, l in enumerate(f):
            pass
    return i

def append(b, c):
    file = open("wordbank.py", "a")

    file.write("%s\n%s\n" %(b,c))

    file.close()

def test():
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


    print "Had enough? You answered %d questions and your score is:\n %d good answers \n %d wrong answers" % (x+y, x, y)



a = input("Hey! What do you wanna do? \n 1 - add a new word to the bank \n 2 - test yourself \n")

int(a)

if (a==1):

    b = raw_input("What should that word be?\n")
    str(b)
    c = raw_input("What is its meaning?\n")
    str(c)

    append (b, c)

elif a==2:
    test()

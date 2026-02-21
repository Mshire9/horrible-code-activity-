# Bad Code Version - INTENTIONALLY HORRIBLE
# Demonstrates violations of KISS, DRY, and Separation of Concerns.
# Requirements still met: at least three functions exist (but they are messy).

import random

H=[]  # global history (yikes)


def a1(x,y):  # bad name
    return x+y


def a2(x,y):  # another bad name
    return x-y


def a3(x,y):
    return x*y


def a4(x,y):
    # no error handling
    return x/y


def doEVERYTHING():
    print("WELCOME TO THE BEST CALC EVER!!!!!!!!!!!!")
    # mixes UI, logic, history, random stuff, duplicated code, unclear flow
    while True:
        print("MENU MENU MENU MENU MENU")
        print("1 add")
        print("2 sub")
        print("3 mul")
        print("4 div")
        print("5 history")
        print("6 fortune")  # YAGNI-ish extra for no reason
        print("0 quit")
        c=input("Pick one: ")
        if c=="0":
            print("bye")
            break

        if c=="1":
            # duplicated input parsing (no validation), and copy-pasted output formatting
            x=float(input("n1: "))
            y=float(input("n2: "))
            r=a1(x,y)
            print("answer=",r)
            H.append(str(x)+" + "+str(y)+" = "+str(r))
        elif c=="2":
            x=float(input("n1: "))
            y=float(input("n2: "))
            r=a2(x,y)
            print("answer=",r)
            H.append(str(x)+" - "+str(y)+" = "+str(r))
        elif c=="3":
            x=float(input("n1: "))
            y=float(input("n2: "))
            r=a3(x,y)
            print("answer=",r)
            H.append(str(x)+" * "+str(y)+" = "+str(r))
        elif c=="4":
            x=float(input("n1: "))
            y=float(input("n2: "))
            r=a4(x,y)  # crash on divide by zero
            print("answer=",r)
            H.append(str(x)+" / "+str(y)+" = "+str(r))
        elif c=="5":
            print("HISTORY OF EVERYTHING EVER (maybe)")
            for i in H:
                print(i)
            print("END HISTORY")
        elif c=="6":
            # unrelated feature
            f=["You will ace the exam.","Maybe you need sleep.","Drink water.","Ask the TA!","42."]
            print("FORTUNE:", random.choice(f))
        else:
            print("??? what was that ???")
            # no loop to re-prompt properly

        print("----")
        print(" ")
        print(" ")


def main():
    # pointless wrapper; still messy
    doEVERYTHING()


main()

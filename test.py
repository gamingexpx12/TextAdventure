# coding=utf-8
from __future__ import print_function
from time import sleep

def talk(speaker,content,speed = 1):
    print ("{}:".format(speaker))
    prev = None
    for l in content:
        if prev == " ":
            sleep(0.05  / speed) #space delay
        elif prev == "\n":
            sleep(0.7 / speed) #newline delay
        elif prev == "!":
            sleep(0.6 / speed)
        else:
            sleep(0.05 / speed) #normal delay
        print(l, end="")
        prev = l
    return
#   -   Program Begin   -   #
wiz = "Wizard of Oseberg"
edge = "Djeck"

talk(wiz, "Welcome my friend! \nWhat is your name?\n")
name = "John Cena" #raw_input(" It's : ")
talk(wiz, "Well met {}! \n".format(name))
talk(edge, "We don't have time for this, wizard! \n")
talk(wiz, "What are you talking about?", 0.3)

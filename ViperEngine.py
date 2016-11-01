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


def title(text="Title"):
    text = " {} ".format(text)
    print ("{:={align}40.38}".format(text, align = "^"))

if __name__ == '__main__':
    print("You're trying to start the engine itself, try starting an adventure instead!")

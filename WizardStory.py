import ViperEnigne
wiz = "Wizard of Oseberg"
edge = "Djeck"

talk(wiz, "Welcome my friend! \nWhat is your name?\n")
name = "John Cena" #raw_input(" It's : ")
talk(wiz, "Well met {}! \n".format(name))
talk(edge, "We don't have time for this, wizard! \n")
talk(wiz, "What are you talking about?", 0.3)
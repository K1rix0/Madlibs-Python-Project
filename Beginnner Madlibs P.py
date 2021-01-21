'''This is the first project shown in the youtube video of "12 Beginner 
Python Projects - Coding Course" on youtube by freeCodeCamp.org, though 
im not full on copying everything they show, it'll be inspiration'''

class Madlibs:
    name = None
    age = None
    fHobby = None
    fColour = None

print("~~~~~~~~~~~~~ Madlibs ~~~~~~~~~~~~~")
x = Madlibs
x.name = input("Firstly type a name: ")
x.age = input("Secondly type an age: ")
x.fHobby = input("Type your favourite hobby: ")
x.fColour = input("Type your favourite colour: ")
print('\n')

print("There was once a legend called" + x.name)
print("Legend has it he was " + x.age + " old, when he")
print("broke the world record at " + x.fHobby + " without breaking a sweat!")
print("A fun fact of him was his favourite colour was " + x.fColour.lower())
print("The End...\n")
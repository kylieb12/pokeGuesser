#Kylie Lillian Drew Christian
#Nov 13th, 2024
#Final Project! Pokemon Akinator.
#cmd F 'TOUCHED' when done -kylie
#imports
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk, ImageDraw
import pickle as pik
import math
from tkinter import messagebox
import pygame

finalround = False

CPOKEDICT = pik.load(open('my_dict.pkl', 'rb'))

root = tk.Tk()
ran = False
responses = []
megas = []
alolans = []
hisuians = []
galarians = []

# The follwing line checks the state oof the window, if the window is active,
# it continues inside the if statement
#TOUCHED
'''
from pygame import mixer
if 'normal' == root.state():
    # This line helps set the software needed to play music
    mixer.init()
    # This line loads the music
    mixer.music.load("music1.mp3")
    # This following line plays the music/ starts the record.
    mixer.music.play()
'''

root.config(background="#FFCB05")



for i in range(len(CPOKEDICT) - 1):
    if 'Alolan' in str(CPOKEDICT[i][3]):
         alolans.append(CPOKEDICT[i][1])
         if 'Galarian' not in str(CPOKEDICT[i-1][3]) and 'Mega' not in str(CPOKEDICT[i-1][3]) and 'Hisuian' not in str(CPOKEDICT[i-1][3]):
             alolans.append(CPOKEDICT[i - 1][1]) # hisuians, megas, etc always appear after their normal forms
         else:
             alolans.append(CPOKEDICT[i - 2][1])
    if 'Hisuian' in str(CPOKEDICT[i][3]):
        hisuians.append(CPOKEDICT[i][1])
        if 'Galarian' not in str(CPOKEDICT[i-1][3]) and 'Mega' not in str(CPOKEDICT[i-1][3]) and 'Alolan' not in str(CPOKEDICT[i-1][3]):
            hisuians.append(CPOKEDICT[i - 1][1]) # hisuians, megas, etc always appear after their normal forms
        else:
            hisuians.append(CPOKEDICT[i - 2][1])
    if 'Galarian' in str(CPOKEDICT[i][3]):
        galarians.append(CPOKEDICT[i][1])
        if 'Alolan' not in str(CPOKEDICT[i-1][3]) and 'Mega' not in str(CPOKEDICT[i-1][3]) and 'Hisuian' not in str(CPOKEDICT[i-1][3]):
            galarians.append(CPOKEDICT[i - 1][1]) # hisuians, megas, etc always appear after their normal forms
        else:
            galarians.append(CPOKEDICT[i - 2][1])
    if 'Mega' in str(CPOKEDICT[i][3]):
        megas.append(CPOKEDICT[i][1])
        if 'Galarian' not in str(CPOKEDICT[i-1][3]) and 'Alolan' not in str(CPOKEDICT[i-1][3]) and 'Hisuian' not in str(CPOKEDICT[i-1][3]):
            megas.append(CPOKEDICT[i - 1][1]) # hisuians, megas, etc always appear after their normal forms
        else:
            megas.append(CPOKEDICT[i - 2][1])

root.title(string='GUESS YOUR POKEMON')
root.geometry('500x600')
#classes

#Describe Question Class
class Question():
    def __init__(self, keyWord, listy,poke=None):
        self.word = keyWord
        self.qList = listy
        #if there is only one pokemon remaining in the pokeleft list
        #ask is the last pokemon your pokemon
        #else, ask the remaining questions in the list of questions
        if len(pokeLeft)==1:
            self.ques = 'is ' + pokeLeft[0] + ' your pokemon?'
        elif poke != None:
            self.ques = 'is ' + poke + ' your pokemon?'
        else:
            self.ques = self.getQuestion()

    ##create a function that shows an image of droak alks=ong with the question
    #oak_img--> oak_label shows image of dr oak
    def show_ques(self):
        ##use try and except to make sure image loads and question is asked
        try:
            #To display image, use tk.Photoimage, and set the file equal
            #to the droak png
            oak_img = tk.PhotoImage(file = 'droak.png')
            oak_label = tk.Label(root, image = oak_img)
            oak_label.image= oak_img
            oak_label.pack()
            ##This feature helps to ask the question to the user.
            #to display a new question eahc time, we set the text to self.question
            self.ques_label = tk.Label(root, text =self.ques, font=('Times', 16))
            self.ques_label.pack(pady=20)


            # List a lists of pictures through which we will cycle.
            # This list helps going through give Dr. Oak a smooth animation effect
            list_imgs = ['droak.png', 'droaktalk.png', 'droak.png', 'droaktalk.png',
                        'droak.png', 'droaktalk.png',
                         'droak.png', 'droaktalk.png', 'droak.png', 'droaktalk.png']

            # This is a for loop to update the picture of Professor Oak on screen.

            #TOUCHED
            image = Image.open(list_imgs[0])
            # Helps create an image object
            photo = ImageTk.PhotoImage(image)
            # This helps set changes on the picture
            oak_label.config(image=photo)
            # Sets the current picture to the next photo we want
            oak_label.image = photo
            # bg sets the backgorund color of the label to a yellow color
            oak_label.config(bg = "#FFCB05")
            # Makes our changes visible on  the screen
            root.update_idletasks()

            '''
            for i in range(10):
                # Following gets the path of an image and reads it
                image = Image.open(list_imgs[i])
                # Helps create an image object
                photo = ImageTk.PhotoImage(image)
                # This helps set changes on the picture
                oak_label.config(image=photo)
                # Sets the current picture to the next photo we want
                oak_label.image = photo
                # bg sets the backgorund color of the label to a yellow color
                oak_label.config(bg = "#FFCB05")
                # Makes our changes visible on  the screen
                root.update_idletasks()
                #Sets a time in between updates to give it a natural moving motion
                root.after(100)
                '''
        except Exception as e:
            self.ques_label = tk.Label(root, text =self.ques, font=('Times', 16))
            self.ques_label.pack(pady=20)

    def getQuestion(self):
        for q in self.qList:
            if self.word in q:
                self.qList.remove(q)
                return q

class Pokemon():
    """Pokemon Object containing name, etc """

    def __init__(self, name, generation, special, type1, type2, size, color, evolve, legs): # takes in parameters from the tsv
        self.name = name
        self.gen ="Generation " + str(generation) # ex. Generation 1, Generation 5, etc
        # if special isn't blank, set it to whatever it is
        if not (type(special) == float and math.isnan(special)) == True:
            self.special = special # is it a starter, does it have a mega evolution, etc
        else:
            self.special = "Boring" # if it doesn't have any special modifiers (Legendary, Baby, etc), default value is "Boring"
        self.type1 = type1
        self.type2 = type2
        self.color = color
        self.has_mega = 'None' # initialize mega, regional, specialevolve, and dualtype to No, update later
        self.has_regional = 'None'
        self.specialevolve = 'Nope'
        self.dualtype = 'Nope'

        if legs == 'y':
            self.legs = "Legs" # if it has legs, say so!
        else:
            self.legs = "Nope"
        # self.dualtype
        if not (type(type2) == float and math.isnan(type2)) == True:
             self.dualtype = 'Dual Type' # if the second type value isn't NaN, it's dual type
        if 'Lv.' in str(evolve):
            self.evolve = "Evolve"  # if it evolves a normal way
        elif evolve != '':
            self.evolve = "Evolve" # it still evolves even if its not normal
            self.specialevolve = "Special Evolution Method"  # if it evolves weird, remember that!

        if int(size) >= 1:
            self.size = 'Big' # if it's over a meter tall, it's big
        else:
            self.size = 'Small' # otherwise it's small

        for i in alolans:
            if self.name == i:
                self.has_regional = 'Alolan' # if the pokemon is found in the alolan list, it's alolan
        for i in hisuians:
            if self.name == i:
                self.has_regional = 'Hisuian' # same for hisuians,
        for i in galarians:
            if self.name == i:
                self.has_regional = 'Galarian' # and galarians,
        for i in megas:
            if self.name == i:
                self.has_mega = 'Mega' # and megas!

        #specific file paths
        if 'Alolan' in self.name: # alolan file paths
            self.image ='Alolan'+' '+self.name.split(' ')[0]+'/'+'Alolan'+' '+self.name.split(' ')[0] + '_new.png'
        elif 'Hisuian' in self.name: # hisuian file paths
            self.image = 'Hisuian' + ' ' + self.name.split(' ')[0] + '/' + 'Hisuian' + ' ' + self.name.split(' ')[0] + '_new.png'
        elif 'Galarian' in self.name: # galarian file paths
            self.image = 'Galarian' + ' ' + self.name.split(' ')[0] + '/' + 'Galarian' + ' ' + self.name.split(' ')[0] + '_new.png'
        elif 'Mega' in self.name: # mega file paths
            self.image = 'Mega' + ' ' + self.name.split(' ')[0] + '/' + 'Mega' + ' ' + self.name.split(' ')[0] + '_new.png'
        # Specific pokemon with weird names
        elif 'Deerling' in self.name:
            self.image = 'Deerling/Deerling_new.png'
        elif 'Vivillon' in self.name:
            self.image = 'Vivillion/Vivillon_new.png'
        elif 'Pumpkaboo' in self.name:
            self.image = 'Pumpkaboo/Pumpkaboo_new.png'
        elif 'Gourgeist' in self.name:
            self.image = 'Gourgeist/Gourgeist_new.png'
        elif 'Minior' in self.name:
            self.image = 'Minior (Core Form)/Minior (Core Form)_new.png'
        elif 'Alcremie' in self.name:
            self.image = 'Alcremie/Alcremie_new.png'
        elif 'Dudunsparce' in self.name:
            self.image = 'Dudunsparce (Two-Segment)/Dudunsparce (Two-Segment)_new.png'
        elif 'Ogerpon' in self.name:
            self.image = 'Ogerpon (Teal Mask)/Ogerpon (Teal Mask)_new.png'
        elif 'Squawkabilly' in self.name:
            self.image = ''
        elif 'Gimmighoul' in self.name:
            pass # we don't have a picture on file for gimmighoul
        elif self.name == 'Charizard (Mega X)': # specific weird exceptions
            self.image = 'Mega Charizard X/Mega Charizard X_new.png'

        elif self.name == 'Charizard (Mega Y)':
            self.image = "Mega Charizard Y/Mega Charizard Y_new.png"

        elif self.name == "Mewtwo (Mega X)":
            self.image = "Mega Mewtwo X/Mega Mewtwo X_new.png"

        elif self.name == "Mewtwo (Mega Y)":
            self.image = "Mega Mewtwo Y/Mega Mewtwo Y_new.png"

        elif self.name == 'Terapagos (Stellar)':
            self.image = 'Terapagos/Terapagos_new.png'
        else:         # Standard file path
            self.image = self.name + '/' + self.name + '_new' + '.png'

    def describe(self):
        print("Name: ", self.name)
        print("Generation: ", self.gen)
        print("Special: ", self.special)
        print("Type 1: ", self.type1)
        print("Type 2: ", self.type2)
        print("Color: ", self.color)
        print("Evolve: ", self.evolve)
        print("Size: ", self.size)
        print("Filename: ", self.image)
        print("Mega: ", self.has_mega)
        print("Regional: ", self.has_regional)
        print("Legs: ", self.legs)
        print("Special Evolve:", self.specialevolve)

    def compare(self, otherpk): # if two pokemon aren't identical, return False, else return True
        if self.gen != otherpk.gen:
            return False
        if self.type1 != otherpk.type1:
            return False
        if ((type(self.type2) == float and math.isnan(self.type2)) == False) and self.type2 != otherpk.type2:
            return False
        if self.special != otherpk.special:
            return False
        if self.color != otherpk.color:
            return False
        if self.evolve != otherpk.evolve:
            return False
        if self.size != otherpk.size:
            return False
        if self.has_mega != otherpk.has_mega:
            return False
        if self.has_regional != otherpk.has_regional:
            return False
        if self.legs != otherpk.legs:
            return False
        if self.specialevolve != otherpk.specialevolve:
            return False
        if self.dualtype != otherpk.dualtype:
            return False
        return True
        filehandler = open("my_dict.pkl", "rb")
        myob = pik.load(filehandler)

    def attribute(self):
        return [self.gen, self.special, self.type1, self.type2,self.color,
             self.evolve, self.size, self.has_mega, self.has_regional,
             self.legs,self.specialevolve, self.dualtype]

    #move to next question


##update function deletes the tkinter widgets on the screen and calls the start function
#which will ask the next question and show the next display
def update():
    for w in root.winfo_children():
        w.destroy()
    start()

##main game function
def start():
    global finalround
#using global helps us to modify the pokeLeft list outside of the function
    countDict = {}
    for x in pokeLeft:
        try:
            thing = pokeDict[x].attribute()
            for a in thing:
                if (type(a) == float and math.isnan(a)) == False: #issue w nan FIXED
                    if a in countDict:
                        countDict[a] = countDict[a] + 1
                    else:
                        countDict[a] = 1
        except:
            pass
    if len(pokeLeft) < 10: # if there are fewer than 10 options left, print them
        for x in pokeLeft:
            pokeDict[x].describe()
        print("\n")
    #multiple final pokemon
    similar = False
    if len(pokeLeft)!=1:
        similar = True
        i = 0
        while  i < (len(pokeLeft)-1) and similar == True:
            similar = pokeDict[pokeLeft[i]].compare(pokeDict[pokeLeft[i+1]])
            i+=1
    if similar:
        q1 = Question("hi", questionList,pokeLeft[0])
        q1.show_ques()
        finalround = True
    else:
        theQ = check(countDict, questionList)
        q1 = Question(theQ, questionList)
        print(q1.ques)
        ##show question
        q1.show_ques()

    #if user response yes, update the question list and remove the yes/no button on screen
    #call global variable pokeLeft and set it eqaul to the user_response functon with
    #its perimeters answer, theQ, and pokeLeft, and call the update function
    def ans_yes():
        global pokeLeft
        print(len(pokeLeft), len(questionList))
        pokeLeft = pokemonLeftReset(pokeDict)
        questionList = theQuestions()
        print(len(pokeLeft), len(questionList))
        input("pause")
        responses.append(theQ)
        pokeLeft = user_response("Yes", theQ,pokeLeft)
        update()
    def ans_again():
        global pokeLeft
        pokeLeft = pokemonLeftReset(pokeDict)
        questionList = theQuestions()
        print(len(pokeLeft), questionList)






    #if user response yes, update the question list and remove the yes/no button on screen
    #similar to the yes function, except it doesn't append the response to the theQ
    def ans_no():
        global pokeLeft
        pokeLeft = user_response("No", theQ, pokeLeft)
        update()
        #the indeed tells the user that they guessed their pokemon and displays
        #the imageof the pokemon
    def ans_ind():
        user_response("Indeed", 'theQ', pokeLeft)
        #TOUCHED
        #stops the previous music
        #pygame.mixer.music.stop
        #loads the following song
        #mixer.music.load("congrats.mp3")
        #plays the following song
        #mixer.music.play()
        #gets the path to the picture of the pokemon that Dr. Oak guessed.
        # it stores it within a variable
        final_poke = pokeDict[pokeLeft[0]].image
        # This is a list of images we need for pokeball throw animation at the end of the game
        poke_imgs = ['pokeball-1 (dragged).png', 'pokeball-2 (dragged).png', 'pokeball-3 (dragged).png',
                 'pokeball-4 (dragged).png', 'pokeball-5 (dragged).png', 'pokeball-6 (dragged).png',
                  'pokeball-7 (dragged).png', 'pokeball-8 (dragged).png', 'pokeball-9 (dragged).png',
                 'pokeball-10 (dragged).png', 'pokeball-11 (dragged).png', 'pokeball-12 (dragged).png',
                 'pokeball-13 (dragged).png', 'pokeball-14 (dragged).png', 'pokeball-15 (dragged).png',
                 'pokeball-16 (dragged).png', 'pokeball-17 (dragged).png', 'pokeball-18 (dragged).png',
                 'pokeball-19 (dragged).png', final_poke]

        # this line destroys the current window
        for w in root.winfo_children():
            w.destroy()
        #Displays the correct label and shows the pokemon using PIL image
        correct= "Yay, I guessed your pokemon!?"
        l_correct = tk.Label(root, text = correct, font=('Times', 16))
        l_correct.pack(pady=20)

        # These follwing line help to start creating an image on the screen that we will update
        poki_img = ImageTk.PhotoImage(Image.open(pokeDict[pokeLeft[0]].image))
        poki_label = tk.Label(root, image = poki_img)
        resizeme = Image.open(final_poke)
        # Resizing the image of the pokemon Dr. Oak guessed.
        resizeme = resizeme.resize((498,376), Image.Resampling.LANCZOS) # resize to match dimensions of the gif
        resizeme.save(final_poke) # yay i got resized
        poki_label.image = resizeme
        poki_label.pack()

        # This loop will constatly update the picture and create the smooth animation
        # very similar to the loop we used previously for Dr. Oak
        for i in range(20):
            image = Image.open(poke_imgs[i])
            photo = ImageTk.PhotoImage(image)
            poki_label.config(image=photo)
            poki_label.image = photo
            root.update_idletasks()
            # faster time updating
            root.after(75)


        #Ans_not tells the user that their pokemon was not guessed
    def ans_not():
        user_response("Not", 'theQ', pokeLeft)
        for w in root.winfo_children():
                    w.destroy()
        if len(pokeLeft)!= 1:
            pokeLeft.remove(pokeLeft[0])
            update()
        else:
            incorrect= "I'm sorry I couldn't guess your pokemon :/. Goodbye"
            l_incorrect = tk.Label(root, text = incorrect, font=('Times', 16))
            l_incorrect.pack(pady=20)


##Make buttons!!!!!

    yes_button = Button(root, text = "Yes",  command =ans_yes)
    yes_button.pack(side = 'left')
    no_button = Button(root, text = "No",  command = ans_no)
    no_button.pack(side = 'left')
        #final yes button, user will click if it is their pokemon

    indeed_button = Button(root, text = "Indeed", command= ans_ind)
    indeed_button.pack(side = 'left')
        #final no button
    not_button = Button(root, text = "Not", command= ans_not)
    not_button.pack(side = 'left')

#finds the the key that will split the deck in halfish returns key
def sortThatBaddie(dicty):
    kiy = ''
    mid = len(pokeLeft)//2
    for x in dicty:
        if kiy == '':
            kiy = x
        if (abs(dicty[x]-mid) < abs(dicty[kiy] - mid)):
            kiy =x
    return kiy

#makes sure that the middle key hasnt been asked before. calls check. returns key
def check(dicty, listy):
    while True:
        kiy = sortThatBaddie(dicty)
        turnBack = False
        if type(kiy) == int:
            kiy = str(kiy)
            turnBack = True
        if dicty[kiy] == 0:
            return kiy
        for x in listy:
            if kiy in x: # can only be used with the string type
                return kiy # ultimately returns best question to be asked
        if turnBack:
            kiy = int(kiy)
        dicty[kiy] = 0

def pokemonLeftReset(thatone):
    temp = []
    for i in thatone:
        temp.append(thatone[i].name)
    return temp
def theQuestions():
    f = open("ListofQs.txt")
    temp =[]
    for question in f:
        temp.append(question)
    f.close()
    return temp

##Create a function user_response that incoporates kylies previous code of
#store pokemon based on the users yes or no response
#maybe just send the word ending to the question function ?
def user_response(answer, theQ, pokeLeft):
    #if user answer yes we keep everything in goodbye
    goodbye = []
    for x in pokeLeft:
        thing = pokeDict[x].attribute()
        for wow in thing:
            if type(wow)==int:
                wow = str(wow)
            if wow == theQ:
                goodbye.append(x)
                #if x == "Bulbasaur":
                #    print(wow, theQ)


# if user clicks any of the buttons, return goodbye, yes, too bad, or remove
#the pokemon that doesn't match the question description
    if answer == 'Yes':
        return goodbye
    if answer == 'Indeed':
        print("Yes")
    if answer == 'Not':
        print("too bad")
    elif answer == 'No':
        for i in goodbye:
            try:
                pokeLeft.remove(i)
                if i == "Bulbasaur":
                    print("bulby", theQ)
            except:
                pass
        return pokeLeft


#creates the pokedictonary we will be pulling from and creates pokmon obj
pokeDict = {}
for i in range(len(CPOKEDICT) - 1):
    pokeDict[CPOKEDICT[i][1]] = Pokemon(CPOKEDICT[i][1],
        CPOKEDICT[i][2], CPOKEDICT[i][3], CPOKEDICT[i][4], CPOKEDICT[i][5],
         CPOKEDICT[i][7], CPOKEDICT[i][12], CPOKEDICT[i][13], CPOKEDICT[i][14])
#names of all the columns that have information
colName = ["Generation","Special","Type 1","Type 2","Color","Evolve","Size","Mega","Regional"]

#pokemon left to guess
pokeLeft = []
pokeLeft = pokemonLeftReset(pokeDict)

#imports the list of questions and puts them in a list

questionList = theQuestions()


##Play game
start()
# The following function helps stop the music once the user closes the
# game window
#TOUCHED
'''
def on_closing():
    # If the user clicks on the closing button of the window, it shows a prompt
    if tk.messagebox.askokcancel("Quit", "Do you really want to quit? :(, is a fun game"):
        # If yes, the music stops and we destroy the window too
        pygame.mixer.music.stop()
        root.destroy()

# Calls the on_closing function when we press the window closing button.
root.protocol("WM_DELETE_WINDOW", on_closing)
'''
root.mainloop()
print("your done!")

from tkinter import *
import itemlibrary
import shopvar

press = 0
chosen = 0
nickname = ""

class Start():
    def __init__(self):
        self.start = Tk()
        self.start.geometry("500x500")

        self.title = Label(self.start, text="GLADIATOR", font=("Impact", 60))
        self.title.place(x=250, y=65, anchor=CENTER)
        self.play = Button(self.start, text="Start game", font=("Arial", 20), command=self.startbutton)
        self.play.place(x=250, y=200, anchor=CENTER)
        self.instruction = Button(self.start, text="Instructions", font=("Arial", 20), comman=self.instrbut)
        self.instruction.place(x=250, y=300, anchor=CENTER)

        self.start.mainloop()

    def startbutton(self):
        self.start.destroy()
        self.nickenter = Tk()
        self.label = Label(self.nickenter, text="Enter your name, Gladiator", font=("Arial", 15), padx=10)
        self.label.pack(side=TOP)
        self.nick = Entry(self.nickenter, font=("Arial", 12))
        self.nick.pack(side=TOP)
        self.conbut = Button(self.nickenter, text="Continue", font=("Arial", 12), command=self.startbut)
        self.conbut.pack(side=TOP)
        self.nickenter.mainloop()

    def startbut(self):
        global nickname
        nickname = self.nick.get()
        self.nickenter.destroy()
        self.choicewin = Tk()
        label = Label(self.choicewin, text="Choose your weapon:")
        label.pack(side=TOP, anchor=CENTER)
        frame = Frame(self.choicewin)
        frame.pack(side=TOP, anchor=CENTER)
        self.choice = IntVar()
        pic = PhotoImage(file="turn_based_rpg\\pics\\shop\\1.png")
        #picList = []
        #for index in range(3):
        #    picList.append(PhotoImage(file="turn_based_rpg\\pics\\shop\\"+str(index+1)+".png"))
        # in case of adding new pictures, delete the #'s
        for index in range(3):
            item = Radiobutton(frame, image=pic, variable=self.choice, value=index, indicatoron=0, command=self.display)
            item.grid(column=index,row=0)
            # in case of adding new pictures, simply replace "image=pic" with "image=picList[index]"
        self.weapname = Label(self.choicewin, font=("Arial",15))
        self.weapname.pack(side=TOP, anchor=CENTER)
        self.weapdmg = Label(self.choicewin, font=("Arial",15))
        self.weapdmg.pack(side=TOP, anchor=CENTER)
        self.countcritstun = Label(self.choicewin, font=("Arial", 15))
        self.countcritstun.pack(side=TOP, anchor=CENTER)
        self.hitchance = Label(self.choicewin, font=("Arial", 15))
        self.hitchance.pack(side=TOP, anchor=CENTER)
        choosebut = Button(self.choicewin, text="Continue", font=("Arial", 12), command=self.press)
        choosebut.pack(side=TOP, anchor=CENTER)
        self.choicewin.mainloop()
        global chosen
        chosen = int(self.choice.get())
        shopvar.weapon = 9*self.choice.get()
        
    def instrbut(self):
        self.start.destroy()
        self.instr = Tk()
        self.instr.geometry("600x500")
        with open("turn_based_rpg\\instruction.txt") as file:
            text = file.read()
        label1 = Label(self.instr, text=text, font=("Arial", 12), justify=LEFT)
        label1.place(x=10, y=10, anchor=NW)
        goback = Button(self.instr, text="Return", font=("Arial", 12), command=self.back)
        goback.place(x=300, y=400, anchor=CENTER)

        self.instr.mainloop()
    def back(self):
        self.instr.destroy()
        Start()
    def display(self):
        self.countcritstun.config(text="")
        self.hitchance.config(text="")
        self.weapname.config(text=itemlibrary.weaplist[9*self.choice.get()].name)
        self.weapdmg.config(text=str(itemlibrary.weaplist[9*self.choice.get()].min)+"-"+str(itemlibrary.weaplist[9*self.choice.get()].max)+" Damage")
        if hasattr(itemlibrary.weaplist[9*self.choice.get()], "counterbonus"):
            self.countcritstun.config(text="+"+str(itemlibrary.weaplist[9*self.choice.get()].counterbonus)+"% Counter chance")
        elif hasattr(itemlibrary.weaplist[9*self.choice.get()], "critbonus"):
            self.countcritstun.config(text="+"+str(itemlibrary.weaplist[9*self.choice.get()].critbonus)+"% Crit chance")
        elif hasattr(itemlibrary.weaplist[9*self.choice.get()], "stunbonus"):
            self.countcritstun.config(text="+"+str(itemlibrary.weaplist[9*self.choice.get()].stunbonus)+" Stun length")
            self.hitchance.config(text=str(itemlibrary.weaplist[9*self.choice.get()].hitchance)+"% Hit chance")
    def press(self):
        self.choicewin.destroy()
        global press
        press += 1
from tkinter import *
import math
import itemlibrary
import shopvar

gold = 0

class Weapshop():
    def __init__(self):
        global gold
        self.gold = gold
        self.shop = Tk()
        self.shop.geometry("1180x500")
        pic = PhotoImage(file="pics\\shop\\1.png")
        #picList = []
        #for index in range(27):
        #    picList.append(PhotoImage(file="pics\\shop\\"+str(index+1)+".png"))
        # in case of adding new pictures, delete the #'s

        self.itemframe = Frame(self.shop)
        self.itemframe.pack(side=TOP, anchor=NW)

        self.x = IntVar()

        for index in range(27):
            item = Radiobutton(self.itemframe, image=pic, variable=self.x, value=index, indicatoron=0, command=self.display)
            item.grid(column=index-9*(math.floor(index/9)),row=math.floor(index/9))
        # in case of adding new pictures, simply replace "image=pic" with "image=picList[index]"

        self.weapname = Label(self.shop, font=("Arial", 15))
        self.weapname.place(x=1075, y=40, anchor=CENTER)
        self.weapdmg = Label(self.shop, font=("Arial", 15))
        self.weapdmg.place(x=1075, y=70, anchor=CENTER)
        self.countcritstun = Label(self.shop, font=("Arial", 15))
        self.countcritstun.place(x=1075, y=100, anchor=CENTER)
        self.hitchance = Label(self.shop, font=("Arial", 15))
        self.hitchance.place(x=1075, y=130, anchor=CENTER)
        self.price = Label(self.shop, font=("Arial", 15))
        self.price.place(x=1075, y=160, anchor=CENTER)
        self.current = Label(self.shop, font=("Arial", 13))
        self.current.place(x=1075, y=205, anchor=CENTER)
        self.weapname2 = Label(self.shop, font=("Arial", 15))
        self.weapname2.place(x=1075, y=230, anchor=CENTER)
        self.weapdmg2 = Label(self.shop, font=("Arial", 15))
        self.weapdmg2.place(x=1075, y=260, anchor=CENTER)
        self.countcritstun2 = Label(self.shop, font=("Arial", 15))
        self.countcritstun2.place(x=1075, y=290, anchor=CENTER)
        self.hitchance2 = Label(self.shop, font=("Arial", 15))
        self.hitchance2.place(x=1075, y=320, anchor=CENTER)

        self.buybutton = Button(self.shop, text="Buy", font=("Arial", 15), command=self.buy)
        self.buybutton.place(x=1075, y=370, anchor=CENTER)

        self.closebutton = Button(self.shop, text="Return", font=("Arial", 15), command=self.close)
        self.closebutton.place(x=1075, y=460, anchor=CENTER)
        
        self.goldamount = "Gold: "+str(self.gold)
        self.goldlabel = Label(self.shop,text=self.goldamount,font=("Arial", 18),padx=15)
        self.goldlabel.place(x=1075, y=410, anchor=CENTER)

        self.shop.mainloop()
    
    def display(self):
        self.countcritstun.config(text="")
        self.hitchance.config(text="")
        self.weapname.config(text=itemlibrary.weaplist[self.x.get()].name)
        self.weapdmg.config(text=str(itemlibrary.weaplist[self.x.get()].min)+"-"+str(itemlibrary.weaplist[self.x.get()].max)+" Damage")
        if hasattr(itemlibrary.weaplist[self.x.get()], "counterbonus"):
            self.countcritstun.config(text="+"+str(itemlibrary.weaplist[self.x.get()].counterbonus)+"% Counter chance")
        if hasattr(itemlibrary.weaplist[self.x.get()], "critbonus"):
            self.countcritstun.config(text="+"+str(itemlibrary.weaplist[self.x.get()].critbonus)+"% Crit chance")
        if hasattr(itemlibrary.weaplist[self.x.get()], "stunbonus"):
            self.countcritstun.config(text="+"+str(itemlibrary.weaplist[self.x.get()].stunbonus)+" Stun length")
            self.hitchance.config(text=str(itemlibrary.weaplist[self.x.get()].hitchance)+"% Hit chance")
        self.price.config(text=str(itemlibrary.weaplist[self.x.get()].price)+" Gold")

        self.countcritstun2.config(text="")
        self.hitchance2.config(text="")
        self.current.config(text="Current weapon:")
        self.weapname2.config(text=itemlibrary.weaplist[shopvar.weapon].name)
        self.weapdmg2.config(text=str(itemlibrary.weaplist[shopvar.weapon].min)+"-"+str(itemlibrary.weaplist[shopvar.weapon].max)+" Damage")
        if hasattr(itemlibrary.weaplist[shopvar.weapon], "counterbonus"):
            self.countcritstun2.config(text="+"+str(itemlibrary.weaplist[shopvar.weapon].counterbonus)+"% Counter chance")
        if hasattr(itemlibrary.weaplist[shopvar.weapon], "critbonus"):
            self.countcritstun2.config(text="+"+str(itemlibrary.weaplist[shopvar.weapon].critbonus)+"% Crit chance")
        if hasattr(itemlibrary.weaplist[shopvar.weapon], "stunbonus"):
            self.countcritstun2.config(text="+"+str(itemlibrary.weaplist[shopvar.weapon].stunbonus)+" Stun length")
            self.hitchance2.config(text=str(itemlibrary.weaplist[shopvar.weapon].hitchance)+"% Hit chance")
    def buy(self):
        global gold
        if gold-itemlibrary.weaplist[self.x.get()].price >= 0:
            shopvar.weapon = self.x.get()
            gold -= itemlibrary.weaplist[self.x.get()].price
            self.goldamount = "Gold: "+str(gold)
            self.goldlabel.config(text=self.goldamount)
            self.countcritstun2.config(text="")
            self.hitchance2.config(text="")
            self.current.config(text="Current weapon:")
            self.weapname2.config(text=itemlibrary.weaplist[shopvar.weapon].name)
            self.weapdmg2.config(text=str(itemlibrary.weaplist[shopvar.weapon].min)+"-"+str(itemlibrary.weaplist[shopvar.weapon].max)+" Damage")
            if hasattr(itemlibrary.weaplist[shopvar.weapon], "counterbonus"):
                self.countcritstun2.config(text="+"+str(itemlibrary.weaplist[shopvar.weapon].counterbonus)+"% Counter chance")
            if hasattr(itemlibrary.weaplist[shopvar.weapon], "critbonus"):
                self.countcritstun2.config(text="+"+str(itemlibrary.weaplist[shopvar.weapon].critbonus)+"% Crit chance")
            if hasattr(itemlibrary.weaplist[shopvar.weapon], "stunbonus"):
                self.countcritstun2.config(text="+"+str(itemlibrary.weaplist[shopvar.weapon].stunbonus)+" Stun length")
                self.hitchance2.config(text=str(itemlibrary.weaplist[shopvar.weapon].hitchance)+"% Hit chance")
        else:
            None
    def close(self):
        self.shop.destroy()

class Armorshop():
    def __init__(self):
        self.gold = gold
        self.shop = Tk()
        self.shop.geometry("850x500")
        pic = PhotoImage(file="pics\\shop\\1.png")
        #picList = []
        #for index in range(24):
        #    picList.append(PhotoImage(file="pics\\shop\\"+str(index+1)+".png"))
        # in case of adding new pictures, delete the #'s

        self.itemframe = Frame(self.shop)
        self.itemframe.pack(side=TOP, anchor=NW)

        self.x = IntVar()

        for index in range(24):
            item = Radiobutton(self.itemframe, image=pic, variable=self.x, value=index, indicatoron=0, command=self.display)
            item.grid(column=index-6*(math.floor(index/6)),row=math.floor(index/6))
        # in case of adding new pictures, simply replace "image=pic" with "image=picList[index]"

        self.armorname = Label(self.shop, font=("Arial",15))
        self.armorname.place(x=750, y=40, anchor=CENTER)
        self.armor = Label(self.shop, font=("Arial",15))
        self.armor.place(x=750, y=70, anchor=CENTER)
        self.blockcrit = Label(self.shop, font=("Arial",15))
        self.blockcrit.place(x=750, y=100, anchor=CENTER)
        self.price = Label(self.shop, font=("Arial", 15))
        self.price.place(x=750, y=130, anchor=CENTER)
        self.current = Label(self.shop, font=("Arial", 13))
        self.current.place(x=750, y=175, anchor=CENTER)
        self.armorname2 = Label(self.shop, font=("Arial",15))
        self.armorname2.place(x=750, y=200, anchor=CENTER)
        self.armor2 = Label(self.shop, font=("Arial",15))
        self.armor2.place(x=750, y=230, anchor=CENTER)
        self.blockcrit2 = Label(self.shop, font=("Arial",15))
        self.blockcrit2.place(x=750, y=260, anchor=CENTER)

        self.buybutton = Button(self.shop, text="Buy", font=("Arial", 15), command=self.buy)
        self.buybutton.place(x=750, y=310, anchor=CENTER)

        self.closebutton = Button(self.shop, text="Return", font=("Arial", 15), command=self.close)
        self.closebutton.place(x=750, y=450, anchor=CENTER)
        
        self.goldamount = "Gold: "+str(gold)
        self.goldlabel = Label(self.shop,text=self.goldamount,font=("Arial", 18),padx=15)
        self.goldlabel.place(x=750, y=350, anchor=CENTER)

        self.shop.mainloop()
    
    def display(self):
        self.blockcrit.config(text="")
        self.armorname.config(text=itemlibrary.armorlist[self.x.get()+1].name)
        self.armor.config(text=str(itemlibrary.armorlist[self.x.get()+1].armor)+" Armor")
        if hasattr(itemlibrary.armorlist[self.x.get()+1], "block"):
            self.blockcrit.config(text="+"+str(itemlibrary.armorlist[self.x.get()+1].block)+"% Block chance")
        if hasattr(itemlibrary.armorlist[self.x.get()+1], "critdef"):
            self.blockcrit.config(text="+"+str(itemlibrary.armorlist[self.x.get()+1].critdef)+"% Crit defense")
        self.price.config(text=str(itemlibrary.armorlist[self.x.get()+1].price)+" Gold")

        self.blockcrit2.config(text="")
        self.armorname2.config(text="")
        self.armor2.config(text="")

        if self.x.get() < 6:
            if shopvar.shield == 0:
                self.armorname2.config(text="")
                self.armor2.config(text="")
                self.blockcrit2.config(text="")
                self.current.config(text="")
            else:
                self.armorname2.config(text=itemlibrary.armorlist[shopvar.shield].name)
                self.armor2.config(text=str(itemlibrary.armorlist[shopvar.shield].armor)+" Armor")
                self.blockcrit2.config(text="+"+str(itemlibrary.armorlist[shopvar.shield].block)+"% Block chance")
                self.current.config(text="Current shield:")
        elif self.x.get() >= 6 and self.x.get() < 12:
            if shopvar.helmet == 0:
                self.armorname2.config(text="")
                self.armor2.config(text="")
                self.blockcrit2.config(text="")
                self.current.config(text="")
            else:
                self.armorname2.config(text=itemlibrary.armorlist[shopvar.helmet].name)
                self.armor2.config(text=str(itemlibrary.armorlist[shopvar.helmet].armor)+" Armor")
                self.blockcrit2.config(text="+"+str(itemlibrary.armorlist[shopvar.helmet].critdef)+"% Crit defense")
                self.current.config(text="Current helmet:")
        elif self.x.get() >= 12 and self.x.get() < 18:
            if shopvar.breast == 0:
                self.armorname2.config(text="")
                self.armor2.config(text="")
                self.blockcrit2.config(text="")
                self.current.config(text="")
            else:
                self.armorname2.config(text=itemlibrary.armorlist[shopvar.breast].name)
                self.armor2.config(text=str(itemlibrary.armorlist[shopvar.breast].armor)+" Armor")
                self.blockcrit2.config(text="")
                self.current.config(text="Current breastplate:")
        elif self.x.get() >= 18:
            if shopvar.boots == 0:
                self.armorname2.config(text="")
                self.armor2.config(text="")
                self.blockcrit2.config(text="")
                self.current.config(text="")
            else:
                self.armorname2.config(text=itemlibrary.armorlist[shopvar.boots].name)
                self.armor2.config(text=str(itemlibrary.armorlist[shopvar.boots].armor)+" Armor")
                self.blockcrit2.config(text="")
                self.current.config(text="Current boots:")
        
        
    def buy(self):
        global gold
        if gold-itemlibrary.armorlist[self.x.get()+1].price >= 0:
            if self.x.get() < 6:
                shopvar.shield = self.x.get()+1
                self.armorname2.config(text=itemlibrary.armorlist[shopvar.shield].name)
                self.armor2.config(text=str(itemlibrary.armorlist[shopvar.shield].armor)+" Armor")
                self.blockcrit2.config(text="+"+str(itemlibrary.armorlist[shopvar.shield].block)+"% Block chance")
                self.current.config(text="Current shield:")
            if self.x.get() >= 6 and self.x.get() < 12:
                shopvar.helmet = self.x.get()+1
                self.armorname2.config(text=itemlibrary.armorlist[shopvar.helmet].name)
                self.armor2.config(text=str(itemlibrary.armorlist[shopvar.helmet].armor)+" Armor")
                self.blockcrit2.config(text="+"+str(itemlibrary.armorlist[shopvar.helmet].critdef)+"% Crit defense")
                self.current.config(text="Current helmet:")
            if self.x.get() >= 12 and self.x.get() < 18:
                shopvar.breast = self.x.get()+1
                self.armorname2.config(text=itemlibrary.armorlist[shopvar.breast].name)
                self.armor2.config(text=str(itemlibrary.armorlist[shopvar.breast].armor)+" Armor")
                self.blockcrit2.config(text="")
                self.current.config(text="Current breastplate:")
            if self.x.get() >= 18:
                shopvar.boots = self.x.get()+1
                self.armorname2.config(text=itemlibrary.armorlist[shopvar.boots].name)
                self.armor2.config(text=str(itemlibrary.armorlist[shopvar.boots].armor)+" Armor")
                self.blockcrit2.config(text="")
                self.current.config(text="Current boots:")
            gold -= itemlibrary.armorlist[self.x.get()+1].price
            self.goldamount = "Gold: "+str(gold)
            self.goldlabel.config(text=self.goldamount)
        else:
            None
    def close(self):
        self.shop.destroy()

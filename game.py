from tkinter import *
import chara
import startscreen
import itemlibrary
import shops
import shopvar
import enemylibrary
import math
import random

freepoints = 5
player = chara.Player(0,5,5,5,5,5,0)
shield = itemlibrary.sh0
helmet = itemlibrary.h0
breast = itemlibrary.b0
boots = itemlibrary.bo0
x = 0

class GUI():
    def __init__(self, i):
        global weap, shield, helmet, breast, boots
        self.main = Tk()
        self.main.geometry("1300x500")
#############################################################################
        self.areanames = ["grimwood", "pirateharbour", "greatplains", "mistymountains", "wolfcave", "banditcamp", "barbariancamp", "ancienttemple"]
        a = PhotoImage(file="turn_based_rpg\\pics\\"+self.areanames[i]+"\\1.png")
        b = PhotoImage(file="turn_based_rpg\\pics\\"+self.areanames[i]+"\\2.png")
        c = PhotoImage(file="turn_based_rpg\\pics\\"+self.areanames[i]+"\\3.png")
        d = PhotoImage(file="turn_based_rpg\\pics\\"+self.areanames[i]+"\\4.png")
        e = PhotoImage(file="turn_based_rpg\\pics\\"+self.areanames[i]+"\\5.png")
        enemyimages = [a, b, c, d, e]
        fightlist = []
        m = 5*math.floor(player.lvl/5)

        for index in range(5):
            label = Label(self.main, image=enemyimages[index])
            label.place(x=310+170*index, y=250, anchor=CENTER)
            name = Label(self.main, text=enemylibrary.enemylist[m+index].name, font=("Arial", 15), bg="#6e0d0d", fg="#fcb103", width=14)
            name.place(x=310+170*index, y=140, anchor=CENTER)
            fight = Button(self.main, text="Fight", font=("Arial", 15), state=DISABLED, command=self.fightbutton)
            if index == 4:
                fight.config(font=("Impact", 15))
            fight.place(x=310+170*index, y=375, anchor=CENTER)
            fightlist.append(fight)
        fightlist[player.lvl%5].config(state=ACTIVE)
        
        with open("turn_based_rpg\\pics\\"+self.areanames[i]+"\\title.txt") as file:
            title = file.read()
        titlelabel = Label(self.main, text=title, font=("Arial", 20, "bold"), bg="#6e0d0d", fg="#fcb103", width=14)
        titlelabel.place(x=650, y=30, anchor=CENTER)
#############################################################################
        self.displayname(self.main)
        self.displaystats(self.main, 50, 50, 15)
        self.displaybattlestats(self.main, 370, 30, 15)
        self.displaymore()
#############################################################################
        self.addstr = Button(self.main, text="+", command=self.addstrength)
        self.addstr.place(x=150, y=50)
        self.adddex = Button(self.main, text="+", command=self.adddexterity)
        self.adddex.place(x=150, y=100)
        self.addagi = Button(self.main, text="+", command=self.addagility)
        self.addagi.place(x=150, y=150)
        self.addendu = Button(self.main, text="+", command=self.addendurance)
        self.addendu.place(x=150, y=200)
        self.addbiq = Button(self.main, text="+", command=self.addbattleiq)
        self.addbiq.place(x=150, y=250)
#############################################################################
        self.savegame = Button(self.main, text="Save Game", font=("Arial", 15), command=self.savesave)
        self.savegame.place(x=1190, y=100, anchor=CENTER)
        self.loadgame = Button(self.main, text="Load Game", font=("Arial", 15), command=self.loadsave)
        self.loadgame.place(x=1190, y=200, anchor=CENTER)
        self.weaponshop = Button(self.main, text="Weapons", font=("Arial", 15), command=self.weapshop)
        self.weaponshop.place(x=1190, y=300, anchor=CENTER)
        self.armoryshop = Button(self.main, text="Armor", font=("Arial", 15), command=self.armorshop)
        self.armoryshop.place(x=1190, y=400, anchor=CENTER)

        self.main.mainloop()
#############################################################################
    def fightbutton(self):
        self.main.destroy()
        n = int(math.floor(player.lvl/5))
        m = str(math.floor(player.lvl%5)+1)
        self.enemy = enemylibrary.enemylist[player.lvl]
        self.health = player.hp()
        self.enemyhealth = self.enemy.hp 
        self.odef = 0
        self.stun = 0
        self.fight = Tk()
        self.fight.geometry("700x600")
        image = PhotoImage(file="turn_based_rpg\\pics\\"+self.areanames[n]+"\\"+m+".png")
        imagelabel = Label(self.fight, image=image)
        imagelabel.place(x=350, y=150, anchor=CENTER)
        self.displayname(self.fight)
        self.displaystats(self.fight, 50, 25, 12)
        self.displaybattlestats(self.fight, 200, 23, 12)
        self.displayenemyname(self.fight, self.enemy)
        self.displayenemy(self.fight, 50, 25, 12, self.enemy)
        self.displayenemybattle(self.fight, 200, 23, 12, self.enemy)
        self.enemyhplabel = Label(self.fight, text="HP: "+str(self.enemyhealth)+"/"+str(self.enemy.hp), font=("Arial", 15, "bold"))
        self.enemyhplabel.place(x=350, y=30, anchor=CENTER)
        self.playerhplabel = Label(self.fight, text="HP: "+str(self.health)+"/"+str(player.hp()), font=("Arial", 15, "bold"))
        self.playerhplabel.place(x=350, y=550, anchor=CENTER)
        
        frame = Frame(self.fight, height=150, width=300, relief="sunken", borderwidth=5)
        frame.place(x=350, y=345, anchor=CENTER)
        label1 = Label(frame, font=("Arial", 12))
        label2 = Label(frame, font=("Arial", 12))
        label3 = Label(frame, font=("Arial", 12))
        label4 = Label(frame, font=("Arial", 12))
        label1.grid(column=0, row=0)
        label2.grid(column=0, row=1)
        label3.grid(column=0, row=2)
        label4.grid(column=0, row=3)
        self.labellist = [label1, label2, label3, label4]

        quickbutton = Button(self.fight, text="Quick attack", font=("Arial, 12"), command=lambda: self.attackskeleton(player.quickattack, 25))
        normalbutton = Button(self.fight, text="Normal attack", font=("Arial, 12"), command=lambda: self.attackskeleton(player.mediumattack, 0))
        powerbutton = Button(self.fight, text="Power attack", font=("Arial, 12"), command=lambda: self.attackskeleton(player.powerattack, -25))
        quickbutton.place(x=175, y=425, anchor=CENTER)
        normalbutton.place(x=350, y=425, anchor=CENTER)
        powerbutton.place(x=525, y=425, anchor=CENTER)
        self.defendbutton = Button(self.fight, text="Defend", font=("Arial, 12"), command=self.defend)
        self.odefensebutton = Button(self.fight, text="O. Defense", font=("Arial, 12"), command=self.odefense)
        self.defendbutton.place(x=260, y=490, anchor=CENTER)
        self.odefensebutton.place(x=440, y=490, anchor=CENTER)

        global weap
        self.quickchance = Label(self.fight, text=str(player.attackchance(self.enemy, weap)+25)+"%", font=("Arial", 10))
        self.normalchance = Label(self.fight, text=str(player.attackchance(self.enemy, weap))+"%", font=("Arial", 10))
        self.powerchance = Label(self.fight, text=str(player.attackchance(self.enemy, weap)-25)+"%", font=("Arial", 10))
        self.quickchance.place(x=175, y=455, anchor=CENTER)
        self.normalchance.place(x=350, y=455, anchor=CENTER)
        self.powerchance.place(x=525, y=455, anchor=CENTER)

        self.fight.mainloop()
        
        if self.enemyhealth <= 0:
            global freepoints
            freepoints += 2
            player.lvl += 1
            if player.lvl == 40:
                youwin = Tk()
                winlabel = Label(youwin, text=name+",\n"+"YOU WON!", font=("Impact", 20, "bold"), padx=25, pady=25)
                winlabel.pack()
                youwin.mainloop()
            else:
                n = int(math.floor(player.lvl/5))
                shops.gold += 100 + 50*n
                GUI(n)
        elif self.health <= 0:
            n = int(math.floor(player.lvl/5))
            GUI(n)
        else:
            n = int(math.floor(player.lvl/5))
            GUI(n)
#############################################################################
    def displayname(self, window):
        global name
        self.namestat = name
        self.namelabel = Label(window,text=self.namestat,font=("Arial", 15, "bold"),padx=10)
        self.namelabel.place(x=0, y=10)
    def displaystats(self, window, yplace, spacing, fontsize):
        player.armor = shield.armor + helmet.armor + breast.armor + boots.armor
    
        self.strstat = "Strength: "+str(player.str)
        self.dexstat = "Dexterity: "+str(player.dex)
        self.agistat = "Agility: "+str(player.agi)
        self.endustat = "Endurance: "+str(player.endu)
        self.biqstat = "Battle IQ: "+str(player.biq)

        self.strlabel = Label(window,text=self.strstat,font=("Arial", fontsize),padx=10)
        self.strlabel.place(x=0, y=yplace)
        self.dexlabel = Label(window,text=self.dexstat,font=("Arial", fontsize),padx=10)
        self.dexlabel.place(x=0, y=yplace+spacing)
        self.agilabel = Label(window,text=self.agistat,font=("Arial", fontsize),padx=10)
        self.agilabel.place(x=0, y=yplace+2*spacing)
        self.endulabel = Label(window,text=self.endustat,font=("Arial", fontsize),padx=10)
        self.endulabel.place(x=0, y=yplace+3*spacing)
        self.biqlabel = Label(window,text=self.biqstat,font=("Arial", fontsize),padx=10)
        self.biqlabel.place(x=0, y=yplace+4*spacing)
    def displaybattlestats(self, window, yplace, spacing, fontsize):
        self.damagestat = "Damage: "+str(player.mindmg(weap))+"-"+str(player.maxdmg(weap))
        self.armor = "Armor: "+str(player.armor)
        self.blockchance = "Block chance: "+str(player.blockchance(shield))+"%"
        self.counterchance = "Counter chance: "+str(player.counterchance(weap))+"%"

        self.damagelabel = Label(window,text=self.damagestat,font=("Arial", fontsize),padx=10)
        self.damagelabel.place(x=0, y=yplace)
        self.armorlabel = Label(window,text=self.armor,font=("Arial", fontsize),padx=10)
        self.armorlabel.place(x=0, y=yplace+spacing)
        self.blocklabel = Label(window,text=self.blockchance,font=("Arial", fontsize),padx=10)
        self.blocklabel.place(x=0, y=yplace+2*spacing)
        self.counterlabel = Label(window,text=self.counterchance,font=("Arial", fontsize),padx=10)
        self.counterlabel.place(x=0, y=yplace+3*spacing)
    def displaymore(self):
        self.gold = shops.gold
        self.goldamount = "Gold: "+str(self.gold)
        self.goldlabel = Label(self.main,text=self.goldamount,font=("Arial", 18),padx=30)
        self.goldlabel.place(x=1300, y=460, anchor=E)
        self.freepointsstat = "Free stat points: "+str(freepoints)
        self.hpstat = "HP: "+str(player.hp())
        self.freelabel = Label(self.main,text=self.freepointsstat,font=("Arial", 10),padx=10)
        self.freelabel.place(x=0, y=300)
        self.hplabel = Label(self.main,text=self.hpstat,font=("Arial", 15),padx=10)
        self.hplabel.place(x=0, y=340)
    def displayenemyname(self, window, enemy):
        self.enemynamestat = enemy.name
        self.enemynamelabel = Label(window,text=self.enemynamestat,font=("Arial", 15, "bold"),padx=10)
        self.enemynamelabel.place(x=517, y=10)
    def displayenemy(self, window, yplace, spacing, fontsize, enemy):
        self.enemystr = "Strength: "+str(enemy.str)
        self.enemydex = "Dexterity: "+str(enemy.dex)
        self.enemyagi = "Agility: "+str(enemy.agi)
        self.enemyendu = "Endurance: "+str(enemy.endu)
        self.enemybiq = "Battle IQ: "+str(enemy.biq)

        self.enemystrlabel = Label(window,text=self.enemystr,font=("Arial", fontsize),padx=10)
        self.enemystrlabel.place(x=517, y=yplace)
        self.enemydexlabel = Label(window,text=self.enemydex,font=("Arial", fontsize),padx=10)
        self.enemydexlabel.place(x=517, y=yplace+spacing)
        self.enemyagilabel = Label(window,text=self.enemyagi,font=("Arial", fontsize),padx=10)
        self.enemyagilabel.place(x=517, y=yplace+2*spacing)
        self.enemyendulabel = Label(window,text=self.enemyendu,font=("Arial", fontsize),padx=10)
        self.enemyendulabel.place(x=517, y=yplace+3*spacing)
        self.enemybiqlabel = Label(window,text=self.enemybiq,font=("Arial", fontsize),padx=10)
        self.enemybiqlabel.place(x=517, y=yplace+4*spacing)      
    def displayenemybattle(self, window, yplace, spacing, fontsize, enemy):
        self.enemydamagestat = "Damage: "+str(enemy.mindmg)+"-"+str(enemy.maxdmg)
        self.enemyarmor = "Armor: "+str(enemy.armor)
        self.enemyblockchance = "Block chance: "+str(enemy.blockch)+"%"
        self.enemycounterchance = "Counter chance: "+str(enemy.counterchance())+"%"

        self.enemydamagelabel = Label(window,text=self.enemydamagestat,font=("Arial", fontsize),padx=10)
        self.enemydamagelabel.place(x=517, y=yplace)
        self.enemyarmorlabel = Label(window,text=self.enemyarmor,font=("Arial", fontsize),padx=10)
        self.enemyarmorlabel.place(x=517, y=yplace+spacing)
        self.enemyblocklabel = Label(window,text=self.enemyblockchance,font=("Arial", fontsize),padx=10)
        self.enemyblocklabel.place(x=517, y=yplace+2*spacing)
        self.enemycounterlabel = Label(window,text=self.enemycounterchance,font=("Arial", fontsize),padx=10)
        self.enemycounterlabel.place(x=517, y=yplace+3*spacing)

    def addstrength(self):
        global freepoints
        if freepoints == 0:
            None
        elif freepoints > 0:
            freepoints -= 1
            player.str += 1
            self.strstat = "Strength: "+str(player.str)
            self.strlabel.config(text=self.strstat)
            self.freepointsstat = "Free stat points: "+str(freepoints)
            self.freelabel.config(text=self.freepointsstat)
            self.damagestat = "Damage: "+str(player.mindmg(weap))+"-"+str(player.maxdmg(weap))
            self.damagelabel.config(text=self.damagestat)
    def adddexterity(self):
        global freepoints
        if freepoints == 0:
            None
        elif freepoints > 0:
            freepoints -= 1
            player.dex += 1
            self.dexstat = "Dexterity: "+str(player.dex)
            self.dexlabel.config(text=self.dexstat)
            self.freepointsstat = "Free stat points: "+str(freepoints)
            self.freelabel.config(text=self.freepointsstat)
    def addagility(self):
            global freepoints
            if freepoints == 0:
                None
            elif freepoints > 0:
                freepoints -= 1
                player.agi += 1
                self.agistat = "Agility: "+str(player.agi)
                self.agilabel.config(text=self.agistat)
                self.freepointsstat = "Free stat points: "+str(freepoints)
                self.freelabel.config(text=self.freepointsstat)
    def addendurance(self):
        global freepoints
        if freepoints == 0:
            None
        elif freepoints > 0:
            freepoints -= 1
            player.endu += 1
            self.endustat = "Endurance: "+str(player.endu)
            self.endulabel.config(text=self.endustat)
            self.freepointsstat = "Free stat points: "+str(freepoints)
            self.freelabel.config(text=self.freepointsstat)
            self.hpstat = "HP: "+str(player.hp())
            self.hplabel.config(text=self.hpstat)
    def addbattleiq(self):
        global freepoints
        if freepoints == 0:
            None
        elif freepoints > 0:
            freepoints -= 1
            player.biq += 1
            self.biqstat = "Battle IQ: "+str(player.biq)
            self.biqlabel.config(text=self.biqstat)
            self.freepointsstat = "Free stat points: "+str(freepoints)
            self.freelabel.config(text=self.freepointsstat)
            self.blockchance = "Block chance: "+str(player.blockchance(shield))+"%"
            self.blocklabel.config(text=self.blockchance)
            self.counterchance = "Counter chance: "+str(player.counterchance(weap))+"%"
            self.counterlabel.config(text=self.counterchance)

    def savesave(self):
        with open("turn_based_rpg\\savefile.txt", "w") as file:
            file.write(str(player.lvl)+","+str(player.str)+","+str(player.dex)+","+str(player.agi)+","+str(player.endu)+","+str(player.biq)+","+str(freepoints)+","+str(weap.id)+","+str(shield.id)+","+str(helmet.id)+","+str(breast.id)+","+str(boots.id)+","+startscreen.nickname+","+str(shops.gold))
    def loadsave(self):
        with open("turn_based_rpg\\savefile.txt") as file:
            save=file.read().split(",")
            player.lvl = int(save[0])
            player.str = int(save[1])
            player.dex = int(save[2])
            player.agi = int(save[3])
            player.endu = int(save[4])
            player.biq = int(save[5])
            global freepoints
            freepoints = int(save[6])
            global weap
            weap = itemlibrary.weaplist[int(save[7])]
            shopvar.weapon = int(save[7])
            global shield, helmet, breast, boots
            if int(save[8]) == 0:
                shield = itemlibrary.sh0
            else:
                shield = itemlibrary.armorlist[int(save[8])]
            shopvar.shield = int(save[8])
            if int(save[9]) == 0:
                helmet = itemlibrary.h0
            else:
                helmet = itemlibrary.armorlist[int(save[9])]
            shopvar.helmet = int(save[9])
            if int(save[10]) == 0:
                breast = itemlibrary.b0
            else:
                breast = itemlibrary.armorlist[int(save[10])]
            shopvar.breast = int(save[10])
            if int(save[11]) == 0:
                boots = itemlibrary.bo0
            else:
                boots = itemlibrary.armorlist[int(save[11])]
            shopvar.boots = int(save[11])
            global name
            name = save[12]
            shops.gold = int(save[13])
            self.main.destroy()
            n = int(math.floor(player.lvl/5))
            GUI(n)

    def weapshop(self):
        self.main.destroy()
        shops.Weapshop()
        global weap
        weap = itemlibrary.weaplist[shopvar.weapon]
        n = int(math.floor(player.lvl/5))
        GUI(n)
    def armorshop(self):
        self.main.destroy()
        shops.Armorshop()
        global shield, helmet, breast, boots
        if shopvar.shield == 0:
            shield = itemlibrary.sh0
        else:
            shield = itemlibrary.armorlist[shopvar.shield]
        if shopvar.helmet == 0:
            helmet = itemlibrary.h0
        else:
            helmet = itemlibrary.armorlist[shopvar.helmet]
        if shopvar.breast == 0:
            breast = itemlibrary.b0
        else:
            breast = itemlibrary.armorlist[shopvar.breast]
        if shopvar.boots == 0:
            boots = itemlibrary.bo0
        else: 
            boots = itemlibrary.armorlist[shopvar.boots]
        # I don't like this solution
        n = int(math.floor(player.lvl/5))
        GUI(n)

    def playerattack(self, func):
        global x
        dmg = func(self.enemy, weap)
        self.enemyhealth -= dmg
        self.labellist[x].config(text=name+" dealt "+str(dmg)+" damage.")
        x += 1
    def playercounter(self):
        global x
        dmg = player.quickattack(self.enemy, weap)
        self.enemyhealth -= dmg
        self.labellist[x].config(text=name+" countered and dealt "+str(dmg)+" damage!")
        x += 1
    def playercrit(self, func):
        global x
        dmg = 2*func(self.enemy, weap)
        self.enemyhealth -= dmg
        self.labellist[x].config(text=name+" dealt "+str(dmg)+" damage!", font=("Arial", 12, "bold"))
        x += 1
    def enemyattack(self):
        global x
        enemydmg = self.enemy.enemyattack(player.armor)
        self.health -= enemydmg
        self.labellist[x].config(text="The "+self.enemy.name+" countered and dealt "+str(enemydmg)+" damage!")
        x += 1
    def enemycounter(self):
        global x
        enemydmg = self.enemy.enemycounter(player.armor)
        self.health -= enemydmg
        self.labellist[x].config(text="The "+self.enemy.name+" countered and dealt "+str(enemydmg)+" damage!")
        x += 1
    def enemycrit(self):
        global x
        enemydmg = 2*self.enemy.enemyattack(player.armor)
        self.health -= enemydmg
        self.labellist[x].config(text="The "+self.enemy.name+" dealt "+str(enemydmg)+" damage!", font=("Arial", 12, "bold"))
        x += 1
    
    def attackskeleton(self, func, chance):
        global name, x
        x = 0
        for p in range(4):
            self.labellist[p].config(text="", font=("Arial", 12))
        ifhit = random.randint(1, 100)
        ifenemy = random.randint(1, 100)
        ifblock = random.randint(1, 100)
        ifenemyblock = random.randint(1, 100)
        ifcounter = random.randint(1, 100)
        ifenemycounter = random.randint(1, 100)
        ifcrit = random.randint(1, 100)
        ifenemycrit = random.randint(1, 100)
        if self.stun == 0:
            if self.odef == 0:
                if ifhit <= player.attackchance(self.enemy, weap)+chance:
                    if ifenemyblock <= self.enemy.blockch:
                        self.labellist[x].config(text="The "+self.enemy.name+" blocked your attack!")
                        x += 1
                    else:
                        if ifcrit <= player.critchance(self.enemy, weap):
                            self.playercrit(func)
                        else:
                            self.playerattack(func)
                    if ifenemycounter <= self.enemy.counterchance():
                        self.enemycounter()
                else:
                    self.labellist[x].config(text=name+" missed his attack.")
                    x += 1
                if ifenemy <= self.enemy.attackchance(player):
                    if ifblock <= player.blockchance(shield):
                        self.labellist[x].config(text=name+" blocked the attack!")
                        x += 1
                    else:
                        if ifenemycrit <= self.enemy.critchance(player, helmet):
                            self.enemycrit()
                        else:
                            self.enemyattack()
                    if ifcounter <= player.counterchance(weap):
                        self.playercounter()
                else:
                    self.labellist[x].config(text="The "+self.enemy.name+" missed his attack.")
                    x += 1
            if self.odef == 1:
                if ifhit <= player.attackchance(self.enemy, weap)+chance+25:
                    if ifenemyblock <= self.enemy.blockch:
                        self.labellist[x].config(text="The "+self.enemy.name+"blocked your attack!")
                        x += 1
                    else:
                        if ifcrit <= player.critchance(self.enemy, weap):
                            self.playercrit(func)
                        else:
                            self.playerattack(func)
                    if ifenemycounter <= self.enemy.counterchance():
                        self.enemycounter()
                else:
                    self.labellist[x].config(text=name+" missed his attack.")
                    x += 1
                if ifenemy <= self.enemy.attackchance(player):
                    if ifblock <= player.blockchance(shield):
                        self.labellist[x].config(text=name+" blocked the attack!")
                        x += 1
                    else:
                        if ifenemycrit <= self.enemy.critchance(player, helmet):
                            self.enemycrit()
                        else:
                            self.enemyattack()
                    if ifcounter <= player.counterchance(weap):
                        self.playercounter()
                else:
                    self.labellist[x].config(text="The "+self.enemy.name+" missed his attack!")
                    x += 1
        if self.stun > 0:
            if self.odef == 0:
                if ifhit <= player.attackchance(self.enemy, weap)+chance:
                    if ifcrit <= player.critchance(self.enemy, weap):
                            self.playercrit(func)
                    else:
                        self.playerattack(func)
                else:
                    self.labellist[x].config(text=name+" missed his attack.")
                    x += 1
            if self.odef == 1:
                if ifhit <= player.attackchance(self.enemy, weap)+chance+25:
                    if ifcrit <= player.critchance(self.enemy, weap):
                            self.playercrit(func)
                    else:
                        self.playerattack(func)
                else:
                    self.labellist[x].config(text=name+" missed his attack.")
                    x += 1
            self.stun -= 1
            if self.stun == 2:
                self.labellist[x].config(text="The "+self.enemy.name+" remains stunned for the next 2 turns")
                x += 1
            elif self.stun == 1:
                self.labellist[x].config(text="The "+self.enemy.name+" remains stunned for the next turn")
                x += 1
            elif self.stun == 0:
                self.labellist[x].config(text="The "+self.enemy.name+" recovered from the stun")
                x += 1
                self.defendbutton.config(state=ACTIVE)
                self.odefensebutton.config(state=ACTIVE)
        if self.odef == 1:
            self.odef -= 1
            self.quickchance.config(text=str(player.attackchance(self.enemy, weap)+25)+"%")
            self.normalchance.config(text=str(player.attackchance(self.enemy, weap))+"%")
            self.powerchance.config(text=str(player.attackchance(self.enemy, weap)-25)+"%")
        self.enemyhplabel.config(text="HP: "+str(self.enemyhealth)+"/"+str(self.enemy.hp))
        self.playerhplabel.config(text="HP: "+str(self.health)+"/"+str(player.hp()))
        if self.enemyhealth <=0 or self.health <= 0:
            self.fight.destroy()
    def defend(self):
        global x
        x = 0
        ifenemy = random.randint(1, 100)
        ifblock = random.randint(1, 100)
        ifcounter = random.randint(1, 100)
        ifstunned = random.randint(1, 100)
        if ifenemy <= self.enemy.attackchance(player):
            if ifblock <= 2*player.blockchance(shield):
                self.labellist[x].config(text=name+" blocked the attack!")
                x += 1
                if ifcounter <= player.counterchance(weap)+40:
                    self.playercounter()
                    if hasattr(weap, "stunbonus"):
                        self.stun += 2
                        self.labellist[x].config(text=name+" stunned the "+self.enemy.name+" for 2 turns!")
                        self.defendbutton.config(state=DISABLED)
                        self.odefensebutton.config(state=DISABLED)
                        x += 1
                    else:
                        self.stun += 1
                        self.defendbutton.config(state=DISABLED)
                        self.odefensebutton.config(state=DISABLED)
                        self.labellist[x].config(text=name+" stunned the "+self.enemy.name+" for 1 turn!")
                        x += 1
            else:
                enemydmg = int(math.ceil(0.5*self.enemy.enemyattack(player.armor)))
                self.health -= enemydmg
                self.labellist[x].config(text="The "+self.enemy.name+" dealt "+str(enemydmg)+" damage.")
                x += 1
                if ifcounter <= player.counterchance(weap):
                    self.playercounter()
        else:
            self.labellist[x].config(text="The "+self.enemy.name+" missed his attack!")
            x += 1
        self.playerhplabel.config(text="HP: "+str(self.health)+"/"+str(player.hp()))
        self.enemyhplabel.config(text="HP: "+str(self.enemyhealth)+"/"+str(self.enemy.hp))
        if ifstunned <= 25+player.endu:
            self.stun += 2
            self.defendbutton.config(state=DISABLED)
            self.odefensebutton.config(state=DISABLED)
            if hasattr(weap, "stunbonus"):
                self.stun += 1
            self.labellist[x].config(text=name+" stunned the "+self.enemy.name+" for "+str(self.stun)+" turns!")
            x += 1
        if self.enemyhealth <=0 or self.health <= 0:
            self.fight.destroy()
    def odefense(self):
        x = 0
        ifenemy = random.randint(1, 100)
        ifblock = random.randint(1, 100)
        ifcounter = random.randint(1, 100)
        if ifenemy <= self.enemy.attackchance(player):
            if ifblock <= player.blockchance(shield):
                self.labellist[x].config(text=name+" blocked the attack!")
                x += 1
                if ifcounter <= player.counterchance(weap)+40:
                    self.playercounter()
                    if hasattr(weap, "stunbonus"):
                        self.stun += 2
                        self.labellist[x].config(text=name+" stunned the "+self.enemy.name+" for 2 turns!")
                        self.defendbutton.config(state=DISABLED)
                        self.odefensebutton.config(state=DISABLED)
                        x += 1
                    else:
                        self.stun += 1
                        self.defendbutton.config(state=DISABLED)
                        self.odefensebutton.config(state=DISABLED)
                        self.labellist[x].config(text=name+" stunned the "+self.enemy.name+" for 1 turn!")
                        x += 1
            else:
                enemydmg = int(math.ceil(0.5*self.enemy.enemyattack(player.armor)))
                self.health -= enemydmg
                self.labellist[x].config(text="The "+self.enemy.name+" dealt "+str(enemydmg)+" damage.")
                x += 1
                if ifcounter <= player.counterchance(weap)+40:
                    self.playercounter()
                    if hasattr(weap, "stunbonus"):
                        self.stun += 2
                        self.labellist[x].config(text=name+" stunned the "+self.enemy.name+" for 2 turns!")
                        self.defendbutton.config(state=DISABLED)
                        self.odefensebutton.config(state=DISABLED)
                        x += 1
                    else:
                        self.stun += 1
                        self.defendbutton.config(state=DISABLED)
                        self.odefensebutton.config(state=DISABLED)
                        self.labellist[x].config(text=name+" stunned the "+self.enemy.name+" for 1 turn!")
                        x += 1
        else:
            self.labellist[x].config(text="The "+self.enemy.name+" missed his attack!")
            x += 1
        self.odef = 1
        self.quickchance.config(text=str(player.attackchance(self.enemy, weap)+50)+"%")
        self.normalchance.config(text=str(player.attackchance(self.enemy, weap)+25)+"%")
        self.powerchance.config(text=str(player.attackchance(self.enemy, weap))+"%")
        self.playerhplabel.config(text="HP: "+str(self.health)+"/"+str(player.hp()))
        self.enemyhplabel.config(text="HP: "+str(self.enemyhealth)+"/"+str(self.enemy.hp))
        if self.enemyhealth <=0 or self.health <= 0:
            self.fight.destroy()

startscreen.Start()
weap = itemlibrary.weaplist[9*startscreen.chosen]

if startscreen.press == 1:
    name = startscreen.nickname
    n = int(math.floor(player.lvl/5))
    GUI(n)
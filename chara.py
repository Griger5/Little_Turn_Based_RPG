import math
import random

class Player:
    def __init__(self, lvl, str, dex, agi, endu, biq, armor):
        self.lvl = lvl
        self.str = str
        self.dex = dex
        self.agi = agi
        self.endu = endu
        self.biq = biq
        self.armor = armor
    def hp(self):
        hppoint = math.ceil((50 + 10*self.endu)*(1+self.lvl/15+(self.endu-5)/20))
        return hppoint
    def mindmg(self, weap):
        mindmg = round((1+(self.str-5)/18)*(weap.min+self.str*(weap.min/(weap.min+weap.max))))
        return mindmg
    def maxdmg(self, weap):
        maxdmg = round((1+(self.str-5)/18)*(weap.max+self.str*(weap.max/(weap.min+weap.max))))
        return maxdmg
    def blockchance(self, shield):
        block = 5+int(math.ceil(0.5*(self.biq-5)))+shield.block
        return block
    def counterchance(self, weap):
        if hasattr(weap, "counterbonus"):
            counter = 5+self.biq+weap.counterbonus
            return counter
        else:
            counter = 5+self.biq
            return counter
    def attackchance(self, enemy, weap):
        if hasattr(weap, "hitchance"):
            attackchance = math.ceil(100*self.dex/enemy.agi) - 25 + weap.hitchance
            return attackchance
        else:
            attackchance = math.ceil(100*self.dex/enemy.agi) - 25
            return attackchance
    def critchance(self, enemy, weap):
        if hasattr(weap, "critbonus"):
            critchance = 3*(self.dex + self.biq - enemy.agi) + weap.critbonus
            return critchance
        else:
            critchance = 3*(self.dex + self.biq - enemy.agi)
            return critchance
    def mediumattack(self, enemy, weap):
        mindmg = self.mindmg(weap)
        maxdmg = self.maxdmg(weap)
        dmg = random.randint(mindmg, maxdmg) - enemy.armorprotect()
        if dmg <= 0:
            dmg = 1
        return dmg
    def quickattack(self, enemy, weap):
        mindmg = round(0.6*self.mindmg(weap))
        maxdmg = round(0.6*self.maxdmg(weap))
        dmg = random.randint(mindmg, maxdmg) - enemy.armorprotect()
        if dmg <= 0:
            dmg = 1
        return dmg
    def powerattack(self, enemy, weap):
        mindmg = round(1.6*self.mindmg(weap))
        maxdmg = round(1.6*self.maxdmg(weap))
        dmg = random.randint(mindmg, maxdmg) - enemy.armorprotect()
        if dmg <= 0:
            dmg = 1
        return dmg

class Enemy:
    def __init__(self, name, hp, mindmg, maxdmg, str, dex, agi, endu, biq, blockch, armor):
        self.name = name
        self.hp = hp
        self.mindmg = mindmg
        self.maxdmg = maxdmg
        self.dex = dex
        self.agi = agi
        self.biq = biq
        self.blockch = blockch
        self.armor = armor
        self.str = str
        self.endu = endu
    def armorprotect(self):
        armorprotect = random.randint(math.floor(0.85*self.armor/100), (math.ceil(1.15*self.armor/100)))
        return armorprotect
    def attackchance(self, player):
        attackchance = math.ceil(100*self.dex/player.agi) - 20
        return attackchance
    def counterchance(self):
        counter = 5+self.biq
        return counter
    def critchance(self, player, helmet):
        critchance = 3*(self.dex + self.biq - player.agi) - helmet.critdef
        return critchance
    def enemycounter(self, armor):
        minidmg = round(0.6*(self.mindmg))
        maxidmg = round(0.6*(self.maxdmg))
        enemydmg = random.randint(minidmg, maxidmg) - random.randint(math.floor(0.85*armor/100), math.ceil(1.15*armor/100))
        if enemydmg <= 0:
            enemydmg = 1
        return enemydmg
    def enemyattack(self, armor):
        i = random.randint(0,2)
        if i == 0:
            minidmg = round(0.6*(self.mindmg))
            maxidmg = round(0.6*(self.maxdmg))
            enemydmg = random.randint(minidmg, maxidmg) - random.randint(math.floor(0.85*armor/100), math.ceil(1.15*armor/100))
            if enemydmg <= 0:
                enemydmg = 1
            return enemydmg
        elif i == 1:
            minidmg = self.mindmg
            maxidmg = self.maxdmg
            enemydmg = random.randint(minidmg, maxidmg) - random.randint(math.floor(0.85*armor/100), math.ceil(1.15*armor/100))
            if enemydmg <= 0:
                enemydmg = 1
            return enemydmg
        else:
            minidmg = round(1.6*(self.mindmg))
            maxidmg = round(1.6*(self.maxdmg))
            enemydmg = random.randint(minidmg, maxidmg) - random.randint(math.floor(0.85*armor/100), math.ceil(1.15*armor/100))
            if enemydmg <= 0:
                enemydmg = 1
            return enemydmg

class Weapon:
    def __init__(self, id, name, min, max, price):
        self.id = id
        self.name = name
        self.min = min
        self.max = max
        self.price = price
class Sword(Weapon):
    def __init__(self, id, name, min, max, counterbonus, price):
        super().__init__(id, name, min, max, price)
        self.counterbonus = counterbonus
class Axe(Weapon):
    def __init__(self, id, name, min, max, critbonus, price):
        super().__init__(id, name, min, max, price)
        self.critbonus = critbonus
class Mace(Weapon):
    def __init__(self, id, name, min, max, stunbonus, hitchance, price):
        super().__init__(id, name, min, max, price)
        self.stunbonus = stunbonus
        self.hitchance = hitchance

class Armor:
    def __init__(self, id, name, armor, price):
        self.id = id
        self.name = name
        self.armor = armor
        self.price = price
class Shield(Armor):
    def __init__(self, id, name, armor, block, price):
        super().__init__(id, name, armor, price)
        self.block = block
class Helmet(Armor):
    def __init__(self, id, name, armor, critdef, price):
        super().__init__(id, name, armor, price)
        self.critdef = critdef
'''
Created on Dec 23, 2016

@author: Trevor Stubbs

In this module I will create all the gobal Varibles and classes needed for this program.
'''

# This is my addition for git

#===============================================================================
#  Key: prefix char = what will eventually be pushed to the user
#              pp = book defined value
#===============================================================================


# Define basic character vars
charName = ""
charSex = ""
defChar = ""
charWeight = 0
charHeight = 0
charArch = ""
charRace = ""
charCareer1 = ""
charCareer2 = ""
charFaith = ""
playerName = ""
charLvl = 0
charXP = 0

# Define basic char Stats
charPhy = 0
# Strength not string
charStr = 0
charSpd = 0
charAgl = 0
charPrw = 0
charPoi = 0
charInt = 0
charArc = 0
charPer = 0

# Max stat vars
maxPhy = 0
maxStr = 0
maxSpd = 0
maxAgl = 0
maxPrw = 0
maxPoi = 0
maxInt = 0
maxArc = 0
maxPer = 0

# class the holds all the data about races
class charRace:
    class human():
        #create human function outputs a list[6]
        def humanStats(self):
            return charPhy + 5, charSpd + 6, charStr + 4, charAgl + 3, charPrw + 4, charPoi + 4, charInt + 3, charArc + 0, charPer + 3
        humanArch = ["Gifted", "Intellectual", "Mighty", "Skilled"]
        #=======================================================================
        # def humanLanguage(self):
        #     return
        #=======================================================================
    
    class dwarf():
        #creates dwarf method ouptputs list[6]
        def dwarfStats(self):
            return charPhy + 6, charSpd + 4, charStr + 5, charAgl + 3, charPrw + 4, charPoi + 3, charInt + 4, charArc + 0, charPer + 3
        dwarfArch = ["Gifted", "Intellectual", "Mighty", "Skilled"]
        #=======================================================================
        # def dwarfLanguage(self):
        #     return
        #=======================================================================
    
    class gobber():
        # Gobber Method: output list[6]
        def gobber(self):
            return charPhy + 4, charSpd + 6, charStr + 3, charAgl + 4, charPrw + 4, charPoi + 3, charInt + 3, charArc + 0, charPer + 3
        gobberArch = ["Intellectual", "Mighty", "Skilled"]
            
    class iosan():
        # Iosan method: output list[6]
        def iosanStats(self):
            return charPhy + 5, charSpd + 6, charStr + 4, charAgl + 3, charPrw + 4, charPoi + 4, charInt + 4, charArc + 0, charPer + 3
    
    class nyss():
        # Nyss method: output list[6]
        def nyssStats(self):
            return charPhy + 5, charSpd + 6, charStr + 4, charAgl + 4, charPrw + 4, charPoi + 4, charInt + 3, charArc + 0, charPer + 3
    
    class ogrun():
        # Ogrun method: output list[6]
        def ogrunStats(self):
            return charPhy + 6, charSpd + 5, charStr + 6, charAgl + 3, charPrw + 4, charPoi + 3, charInt + 3, charArc + 0, charPer + 2
    
    class trolkin():
        # Trollking method: output list [6]
        def trollkinStats(self):
            return charPhy + 6, charSpd + 5, charStr + 5, charAgl + 3, charPrw + 4, charPoi + 2, charInt + 3, charArc + 0, charPer + 3
 

a=0 
print(charRace.human.humanStats
    
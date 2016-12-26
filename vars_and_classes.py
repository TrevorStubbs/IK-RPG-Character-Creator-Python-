'''
Created on Dec 23, 2016

@author: Trevor Stubbs

In this module I will create all the gobal Varibles and classes needed for this program.
'''

#===============================================================================
#  Key: prefix char = what will eventually be pushed to the user
#              privPress = book defined value
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
charFaith = "none"
playerName = ""
charLvl = 0
charXP = 0

# Define basic char Stats
charPhy = 0
# Strength not string
charStr = 0
charSpd = 0
charAgi = 0
charPrw = 0
charPoi = 0
charInt = 0
charArc = 0
charPer = 0
# charStats = [0, 0, 0, 0, 0, 0, 0]

# Max stat vars
maxPhy = 0
maxStr = 0
maxSpd = 0
maxAgi = 0
maxPrw = 0
maxPoi = 0
maxInt = 0
maxArc = 0
maxPer = 0


    #create human function outputs a list[6]
def human(a):
    a = 0
    a = 5+ 5 
    return a

# charSpd + 6, charStr + 4, charAgi + 3, charPrw + 4, charPoi + 4, charInt + 3, charArc + 0, charPer + 3
    
def dwarf():
    return charPhy + 5, charSpd + 6, charStr + 4, charAgi + 3, charPrw + 4, charPoi + 4, charInt + 3, charArc + 0, charPer + 3

human(a)
print(a)
'''
Created on Mar 9, 2017

Program to enter Abilities into a JSON Database

@author: Trevor Stubbs
'''

# This is a test project to load data into a json file
# Author Trevor Stubbs

import json

def abilityDatabase():
    abilityInput = str(input("Ability Name: "))
    prerequisiteInput = str(input("Prerequisite(s): "))
    descriptionInput = str(input("Description: "))

    dataInput = []
    dataInput.append({"Ability": abilityInput, "Prerequisite": prerequisiteInput, "Description": descriptionInput})
    print(json.dumps(dataInput, indent=4))

    #append this info into the abilities.json file
    fout = open('abilities.json', 'a')
    json.dump(dataInput, fout, indent=4)
    fout.close()
    
def main():
    i = 1
    while i == 1:
        abilityDatabase()
        g = int(input("Do you want to enter another? \n1. Yes \n2. No "))
        if g == 2: i =2
    
if __name__ == "__main__": main()
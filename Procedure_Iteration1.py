'''
Created on Feb 14, 2017

@author: 6700K_RGB_Build
'''
# This is a procedural prototype to the application
# TODO = things that need to be worked on

#These next variables define empty variables which will be used once a race is chosen.
#===============================================================================
# char_phy = 0 
# char_str = 0
# char_spd = 0
# char_agi = 0
# char_prw = 0
# char_poi = 0
# char_int = 0
# char_arc = 0
# char_per = 0
#===============================================================================

# These next few variables fill in the top part of the character sheet
char_name = str(input("What is your character's name? "))
char_sex = str(input("What is your character's sex? "))
# char_def = str(input("What is your character's defining characteristics? "))
# char_weight = str(input("How much does your character weight? "))
# char_height = str(input("How tall is your character? ))
# char_faith = str(input("What faith does your character follow? "))

print("Choose your character's race.")
char_race = int(input("1. Human \n2. Dwarf\n3. Gobber\n4. Iosan\n5. Nyss\n6. Ogrun\n7. Trollkin\nWhat is your character's race? "))
#1 = human, 2 = dwarf, 3 = gobber, 4 = iosan, 5= nyss, 6 = ogrun, 7 = trollkin
if char_race == 1: # if Human is selected set all the base stats.
    char_phy = 5
    char_spd = 6
    char_str = 4
    char_agi = 3
    char_prw = 4
    char_poi = 4
    char_int = 3
    char_arc = 0
    char_per = 3
elif char_race == 2: # if Dwarf is selected set all the base stats.
    char_phy = 6
    char_spd = 4
    char_str = 5
    char_agi = 3
    char_prw = 4
    char_poi = 3
    char_int = 4
    char_arc = 0
    char_per = 3
elif char_race == 3: # if Gobber is selected set all the base stats.
    char_phy = 4
    char_spd = 6
    char_str = 3
    char_agi = 4
    char_prw = 4
    char_poi = 3
    char_int = 3
    char_arc = 0
    char_per = 3
elif char_race == 4: # if Iosan is selected set all the base stats.
    char_phy = 5
    char_spd = 6
    char_str = 4
    char_agi = 3
    char_prw = 4
    char_poi = 4
    char_int = 4
    char_arc = 0
    char_per = 3
elif char_race == 5: # if Nyss is selected set all the base stats.
    char_phy = 5
    char_spd = 6
    char_str = 4
    char_agi = 4
    char_prw = 4
    char_poi = 4
    char_int = 3
    char_arc = 0
    char_per = 3
elif char_race == 6: # if Ogrun is selected set all the base stats.
    char_phy = 6
    char_spd = 5
    char_str = 6
    char_agi = 3
    char_prw = 4
    char_poi = 3
    char_int = 3
    char_arc = 0
    char_per = 2
elif char_race == 7: # if Trollkin is selected set all the base stats.
    char_phy = 6
    char_spd = 5
    char_str = 5
    char_agi = 3
    char_prw = 4
    char_poi = 2
    char_int = 3
    char_arc = 0
    char_per = 3
else:
    print("That is not a race.") #TODO figure out how to loop back
    
# Choosing character's languages    
if char_race == 1:
    print("Your character knows 2 languages.")
    lang_one = str(input("What is your character's first language? "))
    lang_two = str(input("What is your character's second language? "))
elif char_race == 2:
    print("Your character knows 2 languages: Rhulic(Dwarvish) and another.")
    lang_one = str("Rhulic")
    lang_two = str(input("What is your character's second language? "))
elif char_race == 3:
    print("Your character knows 2 languages: Gobberish and another.")
    lang_one = str("Gobberish")
    lang_two = str(input("What is your character's second language? "))
elif char_race == 4:
    print("Your character knows 2 languages: Shyr and another.")
    lang_one = str("Shyr")
    lang_two = str(input("What is your character's second language? "))
elif char_race == 5:
    print("Your character knows 2 languages: Aeric and another.")
    lang_one = str("Aeric")
    lang_two = str(input("What is your character's second language? "))
elif char_race == 6:
    print("Your character knows 3 languages: Molgur-Og, Rhulic and another.")
    lang_one = str("Molgur-Og")
    lang_two = str("Rhulic")
    lang_three = str(input("What is your character's third language? "))
else:
    print("Your character knows 2 languages: Molgur-Trul and another.")
    lang_one = str("Molgur-Trul")
    lang_two = str(input("What is your character's second language? "))
    
# setting the character's height
if char_race == 1:
    #human height
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Human males are 61-75 inches in height.")
        char_height = str(input("How tall is your character? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Human females are 55-69 inches in height")
        char_height = str(input("How tall is your character? "))
    else:
        print("Humans are between 55-75 inches tall.")
        char_height = str(input("How tall is your character? "))
elif char_race == 2:
    # dwarf height
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Dwarf males are 52-60 inches in height.")
        char_height = str(input("How tall is your character? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Dwarf females are 47-55 inches in height")
        char_height = str(input("How tall is your character? "))
    else:
        print("Dwarfs are between 47-60 inches tall.")
        char_height = str(input("How tall is your character? "))
elif char_race == 3:
    # gobber height
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Gobber males are 33-42 inches in height.")
        char_height = str(input("How tall is your character? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Gobber females are 32-40 inches in height")
        char_height = str(input("How tall is your character? "))
    else:
        print("Gobbers are between 32-42 inches tall.")
        char_height = str(input("How tall is your character? "))
elif char_race == 4:
    # Isoan height
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Iosan males are 65-75 inches in height.")
        char_height = str(input("How tall is your character? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Iosan females are 60-70 inches in height")
        char_height = str(input("How tall is your character? "))
    else:
        print("Iosan elves are between 60-75 inches tall.")
        char_height = str(input("How tall is your character? "))
elif char_race == 5:
    # Nyss height
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Nyss males are 67-77 inches in height.")
        char_height = str(input("How tall is your character? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Nyss females are 62-72 inches in height")
        char_height = str(input("How tall is your character? "))
    else:
        print("Nyss elves are between 62-77 inches tall.")
        char_height = str(input("How tall is your character? "))
elif char_race == 6:
    # Ogrun height
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Ogrun males are 90-105 inches in height.")
        char_height = str(input("How tall is your character? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Ogrun females are 82-97 inches in height")
        char_height = str(input("How tall is your character? "))
    else:
        print("Ogruns are between 82-105 inches tall.")
        char_height = str(input("How tall is your character? "))
else:
    # Trollkin height
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Trollkin males are 71-84 inches in height.")
        char_height = str(input("How tall is your character? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Trollkin females are 63-76 inches in height")
        char_height = str(input("How tall is your character? "))
    else:
        print("Trollkins are between 63-84 inches tall.")
        char_height = str(input("How tall is your character? "))

# Setting your character's weight
if char_race == 1:
    #human weight
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Human males weigh 110-200 pounds.")
        char_height = str(input("How much does your character weigh? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Human females weigh 90-170 pounds.")
        char_height = str(input("How much does your character weigh? "))
    else:
        print("Humans weigh between 90-200 pounds.")
        char_height = str(input("How much does your character weigh? "))      
if char_race == 2:
    #dwarf weight
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Dwaf males weigh 150-190 pounds.")
        char_height = str(input("How much does your character weigh? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Dwarf females weigh 105-145 pounds.")
        char_height = str(input("How much does your character weigh? "))
    else:
        print("Humans weigh between 105-190 pounds.")
        char_height = str(input("How much does your character weigh? ")) 
if char_race == 3:
    #gobber weight
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Gobber males weigh 42-60 pounds.")
        char_height = str(input("How much does your character weigh? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Gobber females weigh 38-55 pounds.")
        char_height = str(input("How much does your character weigh? "))
    else:
        print("Gobber weigh between 42-55 pounds.")
        char_height = str(input("How much does your character weigh? "))   
if char_race == 4:
    #Iosan weight
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Iosan males weigh 125-180 pounds.")
        char_height = str(input("How much does your character weigh? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Iosan females weigh 85-140 pounds.")
        char_height = str(input("How much does your character weigh? "))
    else:
        print("Iosan weigh between 85-180 pounds.")
        char_height = str(input("How much does your character weigh? ")) 
if char_race == 5:
    #Nyss weight
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Nyss males weigh 140-195 pounds.")
        char_height = str(input("How much does your character weigh? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Nyss females weigh 95-130 pounds.")
        char_height = str(input("How much does your character weigh? "))
    else:
        print("Nyss weigh between 95-195 pounds.")
        char_height = str(input("How much does your character weigh? ")) 
if char_race == 6:
    #human weight
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Ogrun males weigh 450-500 pounds.")
        char_height = str(input("How much does your character weigh? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Ogrun females weigh 330-380 pounds.")
        char_height = str(input("How much does your character weigh? "))
    else:
        print("Ogrun weigh between 330-500 pounds.")
        char_height = str(input("How much does your character weigh? "))
if char_race == 7:
    #Trollkin weight
    if char_sex == "Male" or char_race == "male" or char_race == 'm' or char_race == 'M':
        print("Trollkin males weigh 250-330 pounds.")
        char_height = str(input("How much does your character weigh? "))
    elif char_sex == "Female" or char_sex == "female" or char_sex == "f" or char_sex == "F":
        print("Trollkin females weigh 150-230 pounds.")
        char_height = str(input("How much does your character weigh? "))
    else:
        print("Trollkin weigh between 150-330 pounds.")
        char_height = str(input("How much does your character weigh? "))  

# Selecting Archtype
# 1 = Gifted, 2 = Intellectual, 3 = Mighty, 4 = Skilled
print("Chose your character's archtype.")
#for humans, dwarfs, iosans
if char_race == 1 or char_race == 2 or char_race == 4:
    char_arch = int(input("1. Gifted \n2. Intellectual \n3. Mighty \n4. Skilled \nWhat is your character's archtype? "))
#for Nyss and Trollkin
elif char_race == 5 or char_race == 7:
    char_arch = int(input("1. Gifted \n2. Mighty \n3. Skilled \nWhat is your character's archtype? "))
    if char_arch == 2:
        char_arch = 3
    elif char_arch == 3:
        char_arch = 4
#for Gobber
elif char_race == 3:
    char_arch = int(input("1. Intellectual \n2. Mighty \n3. Skilled \nWhat is your character's archtype? "))
    if char_arch == 1:
        char_arch = 2
    elif char_arch == 2:
        char_arch = 3
    elif char_arch == 3:
        char_arch = 4
#for Ogrun
elif char_race == 6:
    char_arch = int(input("1. Mighty \n2. Skilled \nWhat is your character's archtype? "))
    if char_arch == 1:
        char_arch = 3
    elif char_arch == 2:
        char_arch = 4

#chose archtype benifits
if char_arch == 1:
    # Gifted
    if char_race == 1 or char_race == 2 or char_race == 4:
        # Chose arcane school and set base arcane value
        print("Your gifted character needs to choose how they controls magic.")
        arcane_school = int(input("1. Focuser \n2. Will Weaver \nHow does your character control magic? "))
        if arcane_school == 1:
            char_arc = 2
        else: 
            char_arc = 3
    else:
        arcane_school = 2
        char_arc = 3
    print("A Gifted character gains one of the following benefits. Pg. 115")
    # may need to rename arch_benefit to something specific to each archtype
    arch_benefit = int(input("1. Addional Study \n2. Combat Caster \n3. Fast Caster \n4. Feat: Dominator \n" 
                             "5. Feat: Powerful Caster \n6. Feat: Quick Caster \n7. Feat: Strength of will \n"
                             "8. Magic Sensitivity \n9. Rune Reader \n10. Warding Circle \n"
                             "What benefit do you want to assign to your character? "))
elif char_arch == 2:
    # Intellectual
    #TODO must figure how how to incorperate this benefit into the character sheet
    print("You gain +1 to your attack and damage rolls. Additionally while in your command range friendly characters"
          "gain +1 to their attack and damage rolls")
    print("Additionally a Intellectual character gains one of the following benefits. Pg. 115")
    # rename?
    arch_benefit = int(input("1. Battlefield Coordinator \n2. Feat Flawless Timing \n3. Feat: Prescient \n"
                             "4. Feat: Perfect Plot \n5. Feat: Plan of Action \n6. Feat: Quick Thinking \n"
                             "7. Feat: Unconventional Warfare \n8. Genius \n9. Hyper Perception \n"
                             "10. Photographic Memory \nWhat benefit do you want to assign to your character? "))
elif char_arch == 3:
    # Mighty
    #TODO incorperate benifit
    print("Mighty characters gain an additional die on their damage rolls.")
    print("Additionally a Mighty character gains one of the following benefits. Pg. 116")
    # rename?
    arch_benefit = int(input("1. Beat Back \n2. Feat: Back Swing \n3. Feat: Bounding Leap \n"
                             "4. Feat: Countr Charge \n5. Feat: Invulnerable \n6. Feat: Revitalize \n"
                             "7. Feat: Shield Breaker \n8. Feat: Vendetta \n9. Righteous Anger \n"
                             "10. Tough \nWhat benefit do you want to assign to your charater? "))   
else:
    # Skilled
    #TODO incorperate benefits
    print("A Skilled character gains an additional attack during a turn they attack.")
    print("Additionally a Skilled character gains one of the following benefits. Pg. 116")
    arch_benefit = int(input("1. Ambidextrous \n2. Cagey \n3. Deft \n4. Feat: Defensive Strike \n"
                             "5. Feat: Disarm \n6. Feat: Swashbuckler \n7. Feat: Untouchable \n"
                             "8. Preternatural Awareness \n9. Sidestep \n10. Virtuoso"
                             "What benefit do you want to assign to your charater? "))
# Character careers.
print("Your Character starts with 2 careers.")
#human
if char_race == 1:
    #gifted
    if char_arch == 1:
        #focuser
        if arcane_school == 1:
            char_career1 = int(input("1. Alchemist \n2. Arcane Mechanik \n3. Arcanist \n4. Aristocrat \n"
                                     "5. Bounty Hunter \n6. Cuttthroat \n7. Duelist \n8. Field Mechanik \n"
                                     "9. Gun Mage \n10. Highwayman \n11. Investigator \n12. Iron Fang \n"
                                     "13. Knight \n14. Man-at-Arms \n15. Military Officer \n16. Pirate \n"
                                     "17. Pistoleer \n18. Priest \n19. Ranger \n20. Rifleman \n21. Soldier \n"
                                     "22. Sorcerer \n23. Spy \n24. Stormblade \n25. Thief \n26. Trencher \n"
                                     "27. Warcaster \nWhat is your character's first career? "))
            char_career2 = int(input("What is your character's second career? "))
        #Weaver
        else:
            char_career1 = int(input("1. Alchemist \n2. Arcane Mechanik \n3. Arcanist \n4. Aristocrat \n"
                                     "5. Bounty Hunter \n6. Cuttthroat \n7. Duelist \n8. Field Mechanik \n"
                                     "9. Gun Mage \n10. Highwayman \n11. Investigator \n12. Iron Fang \n"
                                     "13. Knight \n14. Man-at-Arms \n15. Military Officer \n16. Pirate \n"
                                     "17. Pistoleer\n18. Priest \n19. Ranger \n20. Rifleman \n21. Soldier \n"
                                     "22. Sorcerer \n23. Spy \n24. Stormblade \n25. Thief \n26. Trencher \n"
                                     "What is your character's first career? "))
            char_career2 = int(input("What is your character's second career? "))
    #all other archtypes
    else:
        char_career1 = int(input("1. Alchemist \n2. Aristocrat \n"
                                 "3. Bounty Hunter \n4. Cuttthroat \n5. Duelist \n6. Field Mechanik \n"
                                 "7. Highwayman \n8. Investigator \n9. Iron Fang \n"
                                 "10. Knight \n11. Man-at-Arms \n12. Military Officer \n13. Pirate \n"
                                 "14. Pistoleer \n15. Ranger \n16. Rifleman \n17. Soldier \n"
                                 "18. Spy \n19. Stormblade \n20. Thief \n21. Trencher \n"
                                 "What is your character's first career? "))
        char_career2 = int(input("What is your character's second career? "))
#dwarf and Nyss TODO rewrite nyss' careers to not include some gifted careers.
elif char_race == 2 or char_race == 5:
    #gifted
    if char_arch == 1:
        #focuser
        if arcane_school == 1:
            char_career1 = int(input("1. Alchemist \n2. Arcane Mechanik \n3. Arcanist \n"
                                     "4. Bounty Hunter \n5. Cuttthroat \n6. Duelist \n7. Field Mechanik \n"
                                     "8. Gun Mage \n9. Highwayman \n10. Investigator \n"
                                     "11. Man-at-Arms \n12. Military Officer \n13. Pirate \n"
                                     "14. Pistoleer \n15. Ranger \n16. Rifleman \n17. Soldier \n"
                                     "18. Sorcerer \n19. Spy \n20. Thief \n"
                                     "21. Warcaster \nWhat is your character's first career? "))
            char_career2 = int(input("What is your character's second career? "))
        else:
            char_career1 = int(input("1. Alchemist \n2. Arcane Mechanik \n3. Arcanist \n"
                                     "4. Bounty Hunter \n5. Cuttthroat \n6. Duelist \n7. Field Mechanik \n"
                                     "8. Gun Mage \n9. Highwayman \n10. Investigator \n"
                                     "11. Man-at-Arms \n12. Military Officer \n13. Pirate \n"
                                     "14. Pistoleer \n15. Ranger \n16. Rifleman \n17. Soldier \n"
                                     "18. Sorcerer \n19. Spy \n20. Thief \n"
                                     "What is your character's first career? "))
            char_career2 = int(input("What is your character's second career? "))
    #all other arch
    else:
        char_career1 = int(input("1. Alchemist \n"
                                 "2. Bounty Hunter \n3. Cuttthroat \n4. Duelist \n5. Field Mechanik \n"
                                 "6. Highwayman \n7. Investigator \n"
                                 "8. Man-at-Arms \n9. Military Officer \n10. Pirate \n"
                                 "11. Pistoleer \n12. Ranger \n13. Rifleman \n14. Soldier \n"
                                 "15. Spy \n16. Thief \n"
                                 "What is your character's first career? "))
        char_career2 = int(input("What is your character's second career? "))
#gobber
elif char_race == 3:
    char_career1 = int(input("1. Alchemist \n"
                             "2. Bounty Hunter \n3. Cuttthroat \n4. Duelist \n5. Field Mechanik \n"
                             "6. Highwayman \n7. Investigator \n"
                             "8. Man-at-Arms \n9. Military Officer \n10. Pirate \n"
                             "11. Pistoleer \n12. Ranger \n13. Rifleman \n14. Soldier \n"
                             "15. Spy \n16. Thief \n"
                             "What is your character's first career? "))
    char_career2 = int(input("What is your character's second career? "))
#Iosan
elif char_race == 4:
    #Gifted
    if char_arch == 1:
        #focuser
        if arcane_school == 1:
            char_career1 = int(input("1. Alchemist \n2. Arcane Mechanik \n3. Arcanist \n"
                                     "4. Bounty Hunter \n5. Cuttthroat \n6. Duelist \n7. Field Mechanik \n"
                                     "8. Gun Mage \n9. Highwayman \n10. Investigator \n11. Knight \n"
                                     "12. Mage Hunter \n13. Man-at-Arms \n14. Military Officer \n15. Pirate \n"
                                     "16. Pistoleer \n17. Ranger \n18. Rifleman \n19. Soldier \n"
                                     "20. Sorcerer \n21. Spy \n22. Thief \n"
                                     "23. Warcaster \nWhat is your character's first career? "))
            char_career2 = int(input("What is your character's second career? "))
        #Weaver
        else:
            char_career1 = int(input("1. Alchemist \n2. Arcane Mechanik \n3. Arcanist \n"
                                     "4. Bounty Hunter \n5. Cuttthroat \n6. Duelist \n7. Field Mechanik \n"
                                     "8. Gun Mage \n9. Highwayman \n10. Investigator \n11. Knight \n"
                                     "12. Mage Hunter \n13. Man-at-Arms \n14. Military Officer \n15. Pirate \n"
                                     "16. Pistoleer \n17. Ranger \n18. Rifleman \n19. Soldier \n"
                                     "20. Sorcerer \n21. Spy \n22. Thief \n"
                                     "What is your character's first career? "))
            char_career2 = int(input("What is your character's second career? "))
    #all other char_arch
    else:
        char_career1 = int(input("1. Alchemist \n"
                                 "2. Bounty Hunter \n3. Cuttthroat \n4. Duelist \n5. Field Mechanik \n"
                                 "6. Highwayman \n7. Investigator \n8. Knight \n"
                                 "9. Mage Hunter \n10. Man-at-Arms \n11. Military Officer \n12. Pirate \n"
                                 "13. Pistoleer \n14. Ranger \n15. Rifleman \n16. Soldier \n"
                                 "17. Spy \n18. Thief \n"
                                 "What is your character's first career? "))
        char_career2 = int(input("What is your character's second career? "))
#Ogrun
elif char_race == 6:
    char_career1 = int(input("1. Alchemist \n"
                             "2. Bounty Hunter \n3. Cuttthroat \n4. Duelist \n5. Field Mechanik \n"
                             "6. Highwayman \n7. Investigator \n"
                             "8. Man-at-Arms \n9. Military Officer \n10. Pirate \n"
                             "11. Pistoleer \n12. Ranger \n13. Rifleman \n14. Soldier \n"
                             "15. Spy \n16. Thief \n18. Trencher"
                             "What is your character's first career? "))
    char_career2 = int(input("What is your character's second career? "))
    
#Trollkin TODO trollkin cant have arcane mechanik, arcanist or warcaster careers.
else:
    #Gifted 
    if char_arch == 1:
        #focuser
        if arcane_school == 1:
            char_career1 = int(input("1. Alchemist \n2. Arcane Mechanik \n3. Arcanist \n"
                                     "4. Bounty Hunter \n5. Cuttthroat \n6. Duelist \n7. Field Mechanik \n"
                                     "8. Gun Mage \n9. Highwayman \n10. Investigator \n"
                                     "11. Man-at-Arms \n12. Military Officer \n13. Pirate \n"
                                     "14. Pistoleer \n15. Ranger \n16. Rifleman \n17. Soldier \n"
                                     "18. Sorcerer \n19. Spy \n20. Thief \n21. Trencher"
                                     "22. Warcaster \nWhat is your character's first career? "))
            char_career2 = int(input("What is your character's second career? "))
        else:
            char_career1 = int(input("1. Alchemist \n2. Arcane Mechanik \n3. Arcanist \n"
                                     "4. Bounty Hunter \n5. Cuttthroat \n6. Duelist \n7. Field Mechanik \n"
                                     "8. Gun Mage \n9. Highwayman \n10. Investigator \n"
                                     "11. Man-at-Arms \n12. Military Officer \n13. Pirate \n"
                                     "14. Pistoleer \n15. Ranger \n16. Rifleman \n17. Soldier \n"
                                     "18. Sorcerer \n19. Spy \n20. Thief \n21. Trencher"
                                     "What is your character's first career? "))
            char_career2 = int(input("What is your character's second career? "))
    else:
        char_career1 = int(input("1. Alchemist \n"
                                 "2. Bounty Hunter \n3. Cuttthroat \n4. Duelist \n5. Field Mechanik \n"
                                 "6. Highwayman \n7. Investigator \n"
                                 "8. Man-at-Arms \n9. Military Officer \n10. Pirate \n"
                                 "11. Pistoleer \n12. Ranger \n13. Rifleman \n14. Soldier \n"
                                 "15. Spy \n16. Thief \n17. Trencher"
                                 "What is your character's first career? "))
        char_career2 = int(input("What is your character's second career? "))
            
#===============================================================================
# #increase you stats
# if char_race == 1:
#===============================================================================
                

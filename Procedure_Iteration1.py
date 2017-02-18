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
char_race = int(input("1. Human \r2. Dwarf\r3. Gobber\r4. Iosan\r5. Nyss\r6. Ogrun\r7. Trollkin\rWhat is your character's race? "))
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
    print("That is not a race.")
    
# Choosing character's languages    
if char_race == 1 or char_race == 2 or char_race == 3 or char_race == 4 or char_race == 5 or char_race == 7:
    print("Your character knows 2 languages.")
    lang_one = str(input("What is you're character's first language? "))
    lang_two = str(input("What is you're character's second language? "))
else:
    print("Your character knows 3 languages. ")
    lang_one = str(input("What is you're character's first language? "))
    lang_two = str(input("What is you're character's second language? "))
    lang_three = str(input("What is you're character's third language? "))
    
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
if char_race == 1 or char_race == 2 or char_race == 4:
    char_arch = int(input("1. Gifted \r2. Intellectual \r3. Mighty \r4. Skilled\rWhat is your character's archtype? "))
elif char_race == 5 or char_race == 7:
    char_arch = int(input("1. Gifted \r2. Mighty \r 3. Skilled\rWhat is your character's archtype? "))
    if char_arch == 2:
        char_arch = 3
    elif char_arch == 3:
        char_arch = 4
elif char_race == 3:
    char_arch = int(input("1. Intellectual \r2. Mighty \r3. Skilled\rWhat is your character's archtype? "))
    if char_arch == 1:
        char_arch = 2
    elif char_arch == 2:
        char_arch = 3
    elif char_arch == 3:
        char_arch = 4
elif char_race == 6:
    char_arch = int(input("1. Mighty \r2. Skilled\rWhat is your character's archtype? "))

#chose archtype benifits
if char_arch == 1:
    # Gifted
    # Chose arcane school and set base arcane value
    print("A gifted character needs tho choose how they controls magic.")
    arcane_school = int(input("1. Focuser \r2. Will Weaver\rHow does your character control magic? "))
    if arcane_school == 1:
        char_arc = 2
    else: 
        char_arc = 3
    print("Additionally a Gifted character gains one of the following benefits. Pg. 115")
    # may need to rename arch_benefit to something specific to each archtype
    arch_benefit = int(input("1. Addional Study \r2. Combat Caster \r3. Fast Caster \r4. Feat: Dominator \r" 
                             "5. Feat: Powerful Caster \r6. Feat: Quick Caster \r7. Feat: Strength of will \r"
                             "8. Magic Sensitivity \r9. Rune Reader \r10. Warding Circle \r"
                             "What benifit do you want to assign to your character?"))
elif char_arch == 2:
    # Intellectual
    #TODO must figure how how to incorperate this benifit into the character sheet
    print("You gain +1 to your attack and damage rolls. Additionally while in your command range friendly characters"
          "gain +1 to their attack and damage rolls")
    print("Additionally a Intellectual character gains one of the following benefits. Pg. 115")
    # rename?
    arch_benefit = int(input("1. Battlefield Coordinator \r2. Feat Flawless Timing \r3. Feat: Prescient \r"
                             "4. Feat: Perfect Plot \r5. Feat: Plan of Action \r6. Feat: Quick Thinking \r"
                             "7. Feat: Unconventional Warfare \r8. Genius \r9. Hyper Perception \r"
                             "10. Photographic Memory \rWhat benefit do you want to assign to your character?"))
elif char_arch == 3:
    # Mighty
    #TODO incorperate benifit
    print("Mighty characters gain an additional die on their damage rolls.")
    print("Additionally a Mighty character gains one of the following benefits. Pg. 116")
    # rename?
    arch_benefit = int(input("1. Beat Back \r2. Feat: Back Swing \r3. Feat: Bounding Leap \r"
                             "4. Feat: Countr Charge \r5. Feat: Invulnerable \r6. Feat: Revitalize \r"
                             "7. Feat: Shield Breaker \r8. Feat: Vendetta \r9. Righteous Anger \r"
                             "10. Tough \rWhat benefit do you want to assign to your charater?"))   
else:
    # Skilled
    #TODO incorperate benefits
    print("A Skilled character gains an additional attack during a turn they attack.")
    print("Additionally a Skilled character gains one of the following benefits. Pg. 116")
    arch_benefit = int(input("1. Ambidextrous \r2. Cagey \r3. Deft \r4. Feat: Defensive Strike \r"
                             "5. Feat: Disarm \r6. Feat: Swashbuckler \r7. Feat: Untouchable \r"
                             "8. Preternatural Awareness \r9. Sidestep \r10. Virtuoso"))
    
    
    
    
    
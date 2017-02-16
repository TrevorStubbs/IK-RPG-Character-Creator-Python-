'''
Created on Feb 14, 2017

@author: 6700K_RGB_Build
'''
# This is a procedural prototype to the application

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
#char_name = str(input("What is your character's name? "))
char_sex = str(input("What is your character's sex? "))
#char_def = str(input("What is your character's defining characteristics? "))
# char_weight = str(input("How much does your character weight? "))
# char_height = str(input("How tall is your character? ))
#char_faith = str(input("What faith does your character follow? "))

char_race = int(input("1. Human \r2. Dwarf\r3. Gobber\r4. Iosan\r5. Nyss\r6. Ogrun\r7. Trollkin\rWhat is your character's race? "))

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
    print("You get 2 languages.")
    lang_one = str(input("What is you're character's first language? "))
    lang_two = str(input("What is you're character's second language? "))
else:
    print("You get 3 languages. ")
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

print("Characer's height is {} inches".format(char_height))
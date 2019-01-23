

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:30:06 2017

@author: akank
"""


target1 = "life stressful work clash"
target2 = "clash work stressful knife"
target3 = "clasp work stressful knife"
target4 = "life stressful album flashes"
target5 = "wife work stressed clamp"
target6 = "dreadful needful begger sport"

def DiceCoefficient(str1,str2):
    set_of_str1=set(str1.split())
    set_of_str2=set(str2.split())
      
    print("\n\nInter:",float(len(set_of_str1&set_of_str2) ))
    print("Value:",len(set_of_str1) +len(set_of_str2))
  
    dice_coeffient=2*float(len(set_of_str1&set_of_str2)) / (len(set_of_str1) +len(set_of_str2) )
    print("Dice:",dice_coeffient)
    
    dice_distance=1-dice_coeffient
    rounded_dis=round(dice_distance,2) 
    return(rounded_dis)
dis1=DiceCoefficient(target1,target2)
print("Dice Coefficient Distance of target 1 and target 2:",dis1)

dis2=DiceCoefficient(target1,target3)
print("Dice Coefficient Distance of target 1 and target 3:",dis2)

dis3=DiceCoefficient(target1,target4)
print("Dice Coefficient Distance of target 1 and target 4:",dis3)

dis4=DiceCoefficient(target1,target5)
print("Dice Coefficient Distance of target 1 and target 5:",dis4)

dis5=DiceCoefficient(target1,target6)
print("Dice Coefficient Distance of target 1 and target 6:",dis5)

dis6=DiceCoefficient(target2,target3)
print("Dice Coefficient Distance of target 2 and target 3:",dis6)

dis7=DiceCoefficient(target2,target4)
print("Dice Coefficient Distance of target 2 and target 4:",dis7)

dis8=DiceCoefficient(target2,target5)
print("Dice Coefficient Distance of target 2 and target 5:",dis8)

dis9=DiceCoefficient(target2,target6)
print("Dice Coefficient Distance of target 2 and target 6:",dis9)

dis10=DiceCoefficient(target3,target4)
print("Dice Coefficient Distance of target 3 and target 4:",dis10)

dis11=DiceCoefficient(target3,target5)
print("Dice Coefficient Distance of target 3 and target 5:",dis11)

dis12=DiceCoefficient(target3,target6)
print("Dice Coefficient Distance of target 3 and target 6:",dis12)

dis13=DiceCoefficient(target4,target5)
print("Dice Coefficient Distance of target 4 and target 5",dis13)

dis14=DiceCoefficient(target4,target6)
print("Dice Coefficient Distance of target 4 and target 6:",dis14)

dis15=DiceCoefficient(target5,target6)
print("Dice Coefficient Distance of target 5 and target 6:",dis15)
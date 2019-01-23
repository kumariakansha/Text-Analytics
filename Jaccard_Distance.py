# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:30:06 2017

@author: akank
"""

def JaccardIndex(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = float(len(set1 & set2)) / len(set1 | set2)
    return round(ans, 2)

target1 = "life stressful work clash"
target2 = "life needful begger sport"
target3 = "life stressful album flashes"
target4 = "life cream stress buster aha haaha"
target5 = "wife work stressed clamp"
target6 = "clash work stressful knife"

def JaccardDistance(str1,str2):
    set_of_str1=set(str1.split())
    set_of_str2=set(str2.split())
        
    print(float(len(set_of_str1&set_of_str2) ))
    print(len(set_of_str1 | set_of_str2))
  
    jacc_index=float(len(set_of_str1&set_of_str2) ) /len(set_of_str1 | set_of_str2)
    
    rounded_distance=round(jacc_index,3)
    
    jacc_distance=1-rounded_distance
    rounded_jacc=round(jacc_distance,2)
    return(rounded_jacc)

dis1=JaccardDistance(target1,target2)
print("Jaccard Distance of target 1 and target 2:",dis1)

dis2=JaccardDistance(target1,target3)
print("Jaccard Distance of target 1 and target 3:",dis2)

dis3=JaccardDistance(target1,target4)
print("Jaccard Distance of target 1 and target 4:",dis3)

dis4=JaccardDistance(target1,target5)
print("Jaccard Distance of target 1 and target 5:",dis4)

dis5=JaccardDistance(target1,target6)
print("Jaccard Distance of target 1 and target 6:",dis5)

dis6=JaccardDistance(target2,target3)
print("Jaccard Distance of target 2 and target 3:",dis6)

dis7=JaccardDistance(target2,target4)
print("Jaccard Distance of target 2 and target 4:",dis7)

dis8=JaccardDistance(target2,target5)
print("Jaccard Distance of target 2 and target 5:",dis8)

dis9=JaccardDistance(target2,target6)
print("Jaccard Distance of target 2 and target 6:",dis9)

dis10=JaccardDistance(target3,target4)
print("Jaccard Distance of target 3 and target 4:",dis10)

dis11=JaccardDistance(target3,target5)
print("Jaccard Distance of target 3 and target 5:",dis11)

dis12=JaccardDistance(target3,target6)
print("Jaccard Distance of target 3 and target 6:",dis12)

dis13=JaccardDistance(target4,target5)
print("Jaccard Distance of target 4 and target 5",dis13)

dis14=JaccardDistance(target4,target6)
print("Jaccard Distance of target 4 and target 6:",dis14)

dis15=JaccardDistance(target5,target6)
print("Jaccard Distance of target 5 and target 6:",dis15)
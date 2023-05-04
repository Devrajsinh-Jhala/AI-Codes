import copy
list = []       #Meet Mehta 20BCP126
openl = []
closedl = []
class my_dictionary(dict):
  def __init__(self):
    self = dict()
  def add(self, key, value):
    self[key] = value
dict = my_dictionary()

def fill(jug, maxlimit, num):
    initial = copy.copy(jug)
    initial[num] = maxlimit
    return initial
def empty(jug, num):
    initial = copy.copy(jug)
    initial[num] = 0
    # if initial not in list:
    #     list.append(initial)
    return initial
def transfer(jug, num1,num2,max1,max2):
    initial = copy.copy(jug)
    # transfer from 1 to 2
    current_2 = max2 - initial[num2]
    if current_2>0:
        if current_2 <= initial[num1]:
            initial[num2] = initial[num2] + current_2
            initial[num1] -= current_2
        else:
            initial[num2] += initial[num1]
            initial[num1] = 0
    # if initial not in list:
    #     list.append(initial)
    return initial
def check_transfer(jug, num1,num2,max1,max2):
    current_2 = max2 - jug[num2]
    if jug==[0,0]:
        return False
    elif current_2>0:
        return True
    else: 
        return False
def check_fill(jug, num1,max1):
    if (jug[num1] == max1):
        return False
    else:
        return True
def check_empty(jug, num1, max1):
    if (jug[num1] == 0):
        return False
    else:
        return True


def tree(jug, num1,num2,max1,max2, target):
    if jug == target:
        return
    if jug not in list:
            if check_fill(jug,num1,max1):
                child1=fill(jug,max1,num1)
            else: 
                child1=None
            if check_fill(jug,num2,max2):
                child2=fill(jug,max2,num2)
            else: 
                child2=None
            if check_empty(jug,num1,max1):
                child3=empty(jug,num1)
            else: 
                child3=None
            if check_empty(jug,num2,max2):
                child4=empty(jug,num2)
            else:
                child4=None
            if check_transfer(jug,num1,num2,max1,max2):
                child5=transfer(jug,num1,num2,max1,max2)
            else:
                child5=None
            if check_transfer(jug,num2,num1,max2,max1):
                child6=transfer(jug,num2,num1,max2,max1)
            else:
                child6=None
            
            list.append(jug)
            temp_list=[]
            if child1!=None:
                temp_list.append(child1)
                openl.append(child1)
            if child2!=None:
                temp_list.append(child2)
                openl.append(child2)
            if child3!=None:
                temp_list.append(child3)
                openl.append(child3)
            if child4!=None:
                temp_list.append(child4)
                openl.append(child4)
            if child5!=None:
                temp_list.append(child5)
                openl.append(child5)
            if child6!=None:
                temp_list.append(child6)
                openl.append(child6)
            openl.pop(0)
            # closedl.append(jug)
            closedl.insert(0, jug)
            
            dict.add(str(jug), temp_list)
            if child1 != None:
                tree(child1, 0,1,5,4,target)
            if child2 != None:
                tree(child2, 0,1,5,4,target)
            if child3 != None:
                tree(child3, 0,1,5,4,target)
            if child4 != None:
                tree(child4, 0,1,5,4,target)
            if child5 != None:
                tree(child5, 0,1,5,4,target)
            if child6 != None:
                tree(child6, 0,1,5,4,target)
    else:
        return
jug = [0,0]
maxlimit = int(input("Enter max limit of first jug: "))
maxlimit2 = int(input("Enter max limit of second jug: "))
target1 = int(input("Target volume of jug 1: "))
target = [target1, 0]
openl.append(jug)

print("------------------------------------------------------------------------")
tree(jug, 0,1,maxlimit,maxlimit2,target)
closedl.append(target)
print("Open List :" ,end=" ")
print(openl)
print("------------------------------------------------------------------------")
print("Closed List :" ,end=" ")
print(closedl)
print("------------------------------------------------------------------------")

realclosedl = []
i=1
j=2
while j<len(closedl)+1:
    if closedl[-i] in dict[str(closedl[-(j)])]:
        realclosedl.insert(0,closedl[-(j)])
        i+=1
    j+=1
realclosedl.insert(0, [0,0])
realclosedl.append(target)
print("--------------Tree----------------")
for k,v in dict.items():
    Lprint = (str(k)+"  --->   "+str(v))
    Lprint = Lprint.replace("[[","[").replace("]]", "]")
    print(Lprint)
print("----------------------------------")
print("Path: " ,end="")
print(realclosedl)
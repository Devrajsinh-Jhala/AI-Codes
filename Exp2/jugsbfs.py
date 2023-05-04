root = [0,0]
print("Closed List: ")
# Meeet Mehta   20BCP126    
openL = []
closeL = []
end = [2,0]
maps = {}
openL.append(root)
print(root,end=" ")
while True:
    node = openL[0]
    closeL.insert(0,node)
    openL.pop(0)
    five = node[0]
    four = node[1]
    maps[str(node)] = []
    lis = maps[str(node)]
    if end == [five,four]:
        break
    if five < 5:        #fill 1
        five = 5
        if [five,four] not in closeL and [five,four] not in openL:
           openL.append([five,four])
           lis.append([five,four])
           print([five,four],end=" ")
        five = node[0]
        four = node[1]
    if four < 4:
        four = 4
        if [five,four] not in closeL and [five,four] not in openL:
           openL.append([five,four])
           lis.append([five,four])
           print([five,four],end=" ")
        five = node[0]
        four = node[1]
    if five > 0:
        five = 0        #empty
        if [five,four] not in closeL:
           openL.append([five,four])
           lis.append([five,four])
           print([five,four],end=" ")
        five = node[0]
        four = node[1]
    if four > 0:
        four = 0        #empty
        if [five,four] not in closeL:
           openL.append([five,four])
           lis.append([five,four])
           print([five,four],end=" ")
        five = node[0]
        four = node[1]
    if five > 0 and four < 4:
        if four+five > 4:   #transfer
            temp = 4 - four
            five-=temp
            four+=temp
        else:
            four+=five
            five = 0
        if [five,four] not in closeL:
           openL.append([five,four])
           lis.append([five,four])
           print([five,four],end=" ")
        five = node[0]
        four = node[1]
    if four > 0 and five < 5:
        if four+five > 5:
            temp = 5 - five
            four-=temp
            five+=temp
        else:
            five+=four
            four = 0
        if [five,four] not in closeL:
           openL.append([five,four])
           lis.append([five,four])
           print([five,four],end=" ")
        five = node[0]
        four = node[1]
i = 0
while True:
    if closeL[i+1] == root:break
    if closeL[i] in maps[str(closeL[i+1])]:
        i+=1
    else:
        closeL.pop(i+1)
closeL.reverse()
print("")
print("--------------------------------------------------------------------------")
print("Path: ")
print(closeL)
print("--------------------------------------------------------------------------")
print("Tree Dictionary")
print(maps)
print("--------------------------------------------------------------------------")
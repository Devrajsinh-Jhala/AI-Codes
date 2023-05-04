from copy import copy
import time
# Time taken by A-star algorithm is greater than Hill climbing
seconds = time.time()
# Meet Mehta
start   =   [2, 8, 3, 1, 6, 4, 7, 0, 5]
end     =   [1, 2, 3, 8, 0, 4, 7, 6, 5]
openL   =   []
closeL  =   []


def checkHvalue(li):
    hV = 0
    for i in range(0, 9):
        if li[i] != end[i] and li[i] != 0:
            hV += 1
    return hV


openL.insert(0,[checkHvalue(start), 0, start])
openP = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}
while True:
    lis = openL[0]
    closeL.append(lis)
    openL.pop(0)
    g = closeL[-1][1]
    if lis[2] == end:
        break
    for i in openP[lis[2].index(0)]:
        tempL = copy(lis[2])
        zeroI = tempL.index(0)
        tempL[i], tempL[zeroI] = tempL[zeroI], tempL[i]     #swap
        if lis not in openL:
            fValue = checkHvalue(tempL)+lis[1]+1
            openL.append([fValue, lis[1]+1, tempL])
    openL = sorted(openL, key=lambda x: x[0])
    closeL.reverse()
    while True:
        if closeL[0][1] > g:
            closeL.pop(0)
        else:
            break
print()
closeL.sort(key=lambda x:x[1])
for i in closeL:
    print("Total FValue: ",i[0]),
    print("Total GValue: ",i[1]),
    print(i[2])
    print("\n")

afterseconds= time.time()
time_taken = afterseconds - seconds
print(time_taken)
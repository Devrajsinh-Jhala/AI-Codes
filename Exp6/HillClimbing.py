from copy import copy
import time
seconds = time.time()
# Time taken by hill climbing is comparatively lesser

start = [2, 8, 3, 1, 6, 4, 7, 0, 5]
end = [1, 2, 3, 8, 0, 4, 7, 6, 5]
openL = []
closeL = []


def checkHvalue(li):
    hV = 0
    for i in range(0, 9):
        if li[i] != end[i] and li[i] != 0:
            hV += 1
    return hV


openL.append([checkHvalue(start), 0, start])
openP = {
    0: [3, 1],
    1: [0, 2, 4],
    2: [1, 5],
    3: [4, 0, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}
s = 0
while True:
    lis = openL[0]
    if lis[2] == end or s == 10:
        break
    lisSuff = openP[lis[2].index(0)]
    for i in lisSuff:
        tempL = copy(lis[2])
        zeroI = tempL.index(0)
        tempL[i], tempL[zeroI] = tempL[zeroI], tempL[i]
        hValue = checkHvalue(tempL)
        if hValue <= lis[0] and lis not in closeL:
            print(tempL, hValue)
            openL.append([hValue, lis[1]+1, tempL])
            closeL.append(lis)
            openL.pop(0)
            break
        break
    s += 1

afterseconds = time.time()
time_taken = afterseconds - seconds
print(time_taken)

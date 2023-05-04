nodes = {
    "A": [["B", 10], ["C", 4]],
    "B": [["A", 10], ["C", 4], ["D", 6]],
    "C": [["A", 4], ["B", 4], ["E", 6]],
    "D": [["B", 6], ["E", 6], ["F", 4]],
    "E": [["C", 6], ["D", 6], ["G", 14]],
    "F": [["D", 4], ["G", 4]],
    "G": [],
}

hValue = {"A": 16, "B": 4, "C": 16, "D": 2, "E": 1, "F": 4, "G": 0}
    
start = "A"
end = "G"
visited = []
cost = {}
openL = []
maps = {}
for i in nodes.keys():
    li = []
    for j in nodes[i]:
        li.append(j[0])
    maps[i] = li

openL.append(["A", 0]) #start node
cost[openL[0][0]] = 0 #value 0

while True:
    lastNode = openL[0] 
    l = nodes[openL[0][0]]
    visited.append(openL[0])
    openL.pop(0)
    flag = False
    for i in l:
        if i not in visited:
            if i[0] not in cost:
                flag = True
                cost[i[0]] = i[1] + lastNode[1]
                openL.append([i[0], cost[i[0]]])
            else:
                if cost[i[0]] + hValue[i[0]] > i[1] + lastNode[1]:
                    flag = True
                    for j in openL:
                        if j[0] == i[0]:
                            cost[i[0]] = i[1] + lastNode[1]
                            openL[openL.index(j)] = [i[0], cost[i[0]]]
    if not flag and len(l) != 0:
        visited.pop(-1)
    openL.sort(key=lambda i: i[1])
    if openL == []:
        break
visited.reverse()
while True:
    if visited[0][0] != end:
        visited.pop(0)
    else:
        break
i = 0
j = 1
visited.reverse()
while True: #removing unnecessary nodes
    if visited[j][0] == end:
        break
    if visited[i][0] not in maps[visited[j][0]]:
        visited.remove(visited[j])
    else:
        i += 1
        j += 1
print("\nLowest Cost of each Node")
for i in cost.keys():
    print(f"{i}:{cost[i]}")
print("\nPath")
for i in visited[:-1]:
    print(i[0], end="--->")
print(visited[-1][0])
# print(maps)
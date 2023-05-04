import heapq
def ucs(graph, start, goal):
    heap = [(0, start)]
    cost = {start: 0}
    parent = {start: None}
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]

        for neighbor in graph[current_node]:
            new_cost = current_cost + graph[current_node][neighbor]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(heap, (new_cost, neighbor))
        print(parent)
    return None
graph = {
    'S' : {'A':5, 'B': 9, 'D':6},
    'A' : {'B':3, 'G1': 9},
    'B' : {'A':2, 'C':1},
    'C' : {'S':6, 'G2':5, 'F':7},
    'D' : {'C':2, 'E':2},
    'E': {'G3':7},
    'F' : {'D':2, 'G3':8}}
path = ucs(graph, "S", "G2")
print("---------------------------------\nPath is :",end=" ")
print(path)

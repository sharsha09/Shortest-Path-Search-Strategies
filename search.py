from operator import itemgetter

def bfs(graph, start, goal):
    queue = [[start]]
    open = [start]
    closed = set()
    while True:
        if not open:
            raise Exception("No more nodes in queue!")
        pathtraversed = queue.pop(0)
        node = pathtraversed[-1]
        if node == goal:
            return pathtraversed
        if node not in closed:
            for children in graph.get(node, []):
                if children not in open and children not in closed:
                    temppath = list(pathtraversed)
                    temppath.append(children)
                    queue.append(temppath)
                    open.append(children)
            closed.add(node)
            open.remove(node)


def dfs(graph, start, goal):
    queue = [[start]]
    open = [start]
    closed = set()
    while True:
        if not open:
            raise Exception("No more nodes in tree!")
        pathtraversed = queue.pop(0)
        node = pathtraversed[-1]
        if node == goal:
            return pathtraversed
        if node not in closed:
            asd = list(graph.get(node, []))
            asd.reverse()
            for children in asd:
                    if children not in open and children not in closed:
                        temppath = list(pathtraversed)
                        temppath.append(children)
                        queue.insert(0, temppath)
                        #checkQueue.pop()
                        open.append(children)
            closed.add(node)
            open.remove(node)

def ucs(graph, start, goal):
    tempQueue = []
    temppath = [[]]
    queue = [[[start, 0]]]
    open = [[start, 0]]
    closed = []
    child = []
    pathtraversed = []
    while True:
        if not open[0]:
            raise Exception("No more nodes in tree!")
        pathtraversed = queue.pop(0)
        nodecost = pathtraversed[-1]
        node = nodecost[0]
        cost = nodecost[1]
        if node == goal:
            return pathtraversed
        openListNode = []
        for k in open:
            openListNode.append(k[0])
        closedListNode = []
        for l in closed:
            closedListNode.append(l[0])
        if graph.get(node, None) is not None:
                newlist = []
                for children in graph.get(node, []):
                    children[1] = int(children[1]) + cost
                    newlist.append(children)
                tempQueue = sorted(newlist, key=itemgetter(1))
                for i in tempQueue:
                    child = i[0]
                    childcost = i[1]
                    if child not in openListNode and child not in closedListNode:
                        temppath = list(pathtraversed)
                        temppath.append(i)
                        queue.append(temppath)
                        index = -1
                        for paths in queue:
                            index = index + 1
                            pathDistance = paths[-1][-1]
                            if childcost < pathDistance:
                                queue.insert(index, temppath)
                                queue.pop(-1)
                                break
                        open.append(i)
                        #closed.append(nodecost)
                    elif child in openListNode:
                        for sublist in open:
                            if sublist[0] == child:
                                openChildCost = sublist[1]
                                if childcost < openChildCost:
                                    open.remove(sublist)
                                    for m in queue:
                                        if sublist in m[:]:
                                            queue.remove(m)
                                    temppath = list(pathtraversed)
                                    temppath.append(i)
                                    queue.append(temppath)
                                    index = -1
                                    for paths in queue:
                                        index = index + 1
                                        pathDistance = paths[-1][-1]
                                        if childcost < pathDistance:
                                            queue.insert(index, temppath)
                                            queue.pop(-1)
                                            break
                                    open.append(i)
                                    #closed.append(nodecost)
                    elif child in closedListNode:
                        for sublist1 in closed:
                            if sublist1[0] == child:
                                closedChildCost = sublist1[1]
                                if childcost < closedChildCost:
                                    open.remove(sublist1)
                                    for n in queue:
                                        if sublist1 in n[:]:
                                            queue.remove(n)
                                    temppath = list(pathtraversed)
                                    temppath.append(i)
                                    queue.append(temppath)
                                    index = -1
                                    for paths in queue:
                                        index = index + 1
                                        pathDistance = paths[-1][-1]
                                        if childcost < pathDistance:
                                            queue.insert(index, temppath)
                                            queue.pop(-1)
                                            break
                                    open.append(i)
                                    #closed.append(nodecost)
                closed.append(nodecost)
                open.remove(nodecost)
        else:
            closed.append(nodecost)
            open.remove(nodecost)


def astar(graph, sundaygraph, start, goal):
    tempQueue = []
    temppath = [[]]
    startsundaycost = int(sundaygraph[start])
    queue = [[[start, 0, startsundaycost]]]
    open = [[start, 0, startsundaycost]]
    closed = []
    child = []
    pathtraversed = []
    while True:
        if not open[0]:
            raise Exception("No more nodes in tree!")
        pathtraversed = queue.pop(0)
        nodecost = pathtraversed[-1]
        node = nodecost[0]
        cost = nodecost[1]
        if node == goal:
            return pathtraversed
        openListNode = []
        for k in open:
            openListNode.append(k[0])
        closedListNode = []
        for l in closed:
            closedListNode.append(l[0])
        if graph.get(node, None) is not None:
                newlist = []
                for children in graph.get(node, []):
                    children[1] = int(children[1]) + cost
                    newlist.append(children)
                #tempQueue = sorted(newlist, key=itemgetter(1))
                for i in newlist:
                    child = i[0]
                    childcost = i[1]
                    sundaycost = sundaygraph[child]
                    i.append(i[1] + int(sundaycost))
                    totalcost = i[2]
                    if child not in openListNode and child not in closedListNode:
                        temppath = list(pathtraversed)
                        temppath.append(i)
                        queue.append(temppath)
                        index = -1
                        for paths in queue:
                            index = index + 1
                            pathDistance = paths[-1][-1]
                            if totalcost < pathDistance:
                                queue.insert(index, temppath)
                                queue.pop(-1)
                                break
                        open.append(i)
                        #closed.append(nodecost)
                    elif child in openListNode:
                        for sublist in open:
                            if sublist[0] == child:
                                openChildCost = sublist[2]
                                if totalcost < openChildCost:
                                    open.remove(sublist)
                                    for m in queue:
                                        if sublist in m[:]:
                                            queue.remove(m)
                                    temppath = list(pathtraversed)
                                    temppath.append(i)
                                    queue.append(temppath)
                                    index = -1
                                    for paths in queue:
                                        index = index + 1
                                        pathDistance = paths[-1][-1]
                                        if totalcost < pathDistance:
                                            queue.insert(index, temppath)
                                            queue.pop(-1)
                                            break
                                    open.append(i)
                                    #closed.append(nodecost)
                    elif child in closedListNode:
                        for sublist1 in closed:
                            if sublist1[0] == child:
                                closedChildCost = sublist1[2]
                                if totalcost < closedChildCost:
                                    open.remove(sublist1)
                                    for n in queue:
                                        if sublist1 in n[:]:
                                            queue.remove(n)
                                    temppath = list(pathtraversed)
                                    temppath.append(i)
                                    queue.append(temppath)
                                    index = -1
                                    for paths in queue:
                                        index = index + 1
                                        pathDistance = paths[-1][-1]
                                        if childcost < pathDistance:
                                            queue.insert(index, temppath)
                                            queue.pop(-1)
                                            break
                                    open.append(i)
                                    #closed.append(nodecost)
                closed.append(nodecost)
                open.remove(nodecost)
        else:
            closed.append(nodecost)
            open.remove(nodecost)



with open('input.txt', 'r') as f:
    file = f.read()
    mainList = file.splitlines()

algo = mainList[0]
start = mainList[1]
goal = mainList[2]
numberOfTrafficLines = mainList[3]

graph = {}
graph2 = {}
for i in mainList[4:4 + int(numberOfTrafficLines)]:
    subList = i.split(" ")
    if str(subList[0]) in graph.keys():
        graph[subList[0]].append(subList[1])
        graph2[subList[0]].append([subList[1], subList[2]])
    else:
        graph[subList[0]] = [subList[1]]
        graph2[subList[0]] = [[subList[1], subList[2]]]

numberOfSundayTrafficLines = mainList[3 + (int(numberOfTrafficLines) + 1)]

sundayGraph = {}
for j in mainList[3 + (int(numberOfTrafficLines) + 2):]:
    (key, val) = j.split(" ")
    sundayGraph[key] = val

if algo == 'BFS':
    pathlist = bfs(graph, start, goal)
    with open('output.txt', 'w') as fwrite:
        n = 0
        for k in pathlist:
            fwrite.write(k + ' ' + str(n) + '\n')
            n += 1
elif algo == 'DFS':
    pathlist = dfs(graph, start, goal)
    with open('output.txt', 'w') as fwrite:
        n = 0
        for k in pathlist:
            fwrite.write(k + ' ' + str(n) + '\n')
            n += 1
elif algo == 'UCS':
    pathlist = ucs(graph2, start, goal)
    with open('output.txt', 'w') as fwrite:
        for k in pathlist:
            fwrite.write(k[0] + " " + str(k[1]) + '\n')
elif algo == 'A*':
    pathlist = astar(graph2, sundayGraph, start, goal)
    with open('output.txt', 'w') as fwrite:
        for k in pathlist:
            fwrite.write(k[0] + " " + str(k[1]) + '\n')




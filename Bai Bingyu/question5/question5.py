# Question5 
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Grid:
    def __init__(self,L,beads):
        self.items = dict()
        for i in range(L):
            row = dict()
            for j in range(L):
                row[j] = "0"
            self.items[i] = row
        self.local = [0,0]
        self.beads = beads
    
    def fill(self,r,c,color):
        self.items[r][c] = color
        self.beads[color] -= 1
        return self
        
    def read(self,r,c):
        return self.items[r][c]
    
    def setLocal(self,x,y):
        self.local = [x,y]
    
    def getLocal(self):
        return self.local
    
    def getBeads(self):
        return self.beads
          
    def __str__(self):
        return str(self.items)


def count(Grid,L):
    penalty = 0
    for i in range(L):
        for j in range(L):
            color = Grid.read(i,j)
            if i>0:
                if Grid.read(i-1,j)==color:
                    penalty+=0.5
            if i<L-1:
                if Grid.read(i+1,j)==color:
                    penalty+=0.5
            if j>0:
                if Grid.read(i,j-1)==color:
                    penalty+=0.5
            if j<L-1:
                if Grid.read(i,j+1)==color:
                    penalty+=0.5
    return penalty


import copy

l = int(input())
n = int(input())
allBeads = dict()
for i in range(n):
    [color,number] = input().split()
    allBeads[color] = int(number)
allColors = list(allBeads.keys())
g = Grid(l,allBeads)
allGrids = Queue()
allGrids.enqueue(g)
result = list()


while not allGrids.isEmpty():
    G = allGrids.dequeue()
    [i,j]=G.getLocal()
    up = "0"
    left = "0"
    if i == l and j == 0:
        result.append(G)
    else:
        if i > 0:
            up = G.read(i-1,j)
        if j > 0:
            left = G.read(i,j-1)
        cand = list()
        for x in allColors:
            if x not in [up,left]:
                if G.getBeads()[x] >0:
                    cand.append(x)
                else:
                    pass
        if len(cand)==0:
            for y in allColors:
                if G.getBeads()[y] >0:
                    cand.append(y)
        if j == l-1:
            s = i+1
            t = 0
        else:
            s = i
            t = j+1
        for color in cand:
            new = copy.deepcopy(G)
            new.fill(i,j,color)
            new.setLocal(s,t)
            allGrids.enqueue(new)
            
ans = dict()
for x in result:
    penalty = count(x,l)
    if penalty in ans:
        ans[penalty].append(x)
    else:
        ans[penalty] = [x]

least = min(list(ans.keys()))
arg = ans[least]
for n in range(len(arg)):
    print("No."+str(n+1))
    for i in range(l):
        for j in range(l):
            print(arg[n].read(i,j),end=" ")
        print("")
    
    
    
    
    
    
    
    
    
    
    
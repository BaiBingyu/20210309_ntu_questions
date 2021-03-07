# Question 4 - 4 neighbors
n = int(input())
# input the number of the rows
grid = dict()
# "grid" records the numberon each location
for i in range(n):
    # input the sequence of every row
    m = input().split()
    row = dict()
    for j in range(len(m)):
        row[j]=m[j]
    grid[i]=row


# this function helps find the points in the nerighborhood that connects to the given one
# it works recursively
def explore(r,c,s):
    grid[r][c] = s
    if r-1 >= 0:
        if grid[r-1][c] == "1": # north
            explore(r-1,c,s)
        if c-1 >= 0:
            if grid[r-1][c-1] == "1": # northwest
                explore(r-1,c-1,s)
        if c+1 < len(m): # northeast
            if grid[r-1][c+1] == "1":
                explore(r-1,c+1,s)
    if r+1 < n:
        if grid[r+1][c] == "1": # south
            explore(r+1,c,s)
        if c-1 >= 0:
            if grid[r+1][c-1] == "1": # southwesy
                explore(r+1,c-1,s)
        if c+1 < len(m):
            if grid[r+1][c+1] == "1": # southeast
                explore(r+1,c+1,s)
    if c-1 >= 0: # west
        if grid[r][c-1] == "1":
            explore(r,c-1,s)
    if c+1 < len(m): # east
        if grid[r][c+1] == "1":
            explore(r,c+1,s)

# the count of the connected cluster
s = 1
for c in range(len(m)):
    for r in range(n):
        if grid[r][c] == "1":
            explore(r,c,s)
            s += 1


for i in range(n):
    for j in range(len(m)):
        print(grid[i][j],end="  ")
    print("")

# Question 1
[m, n] = input().split()
# input the numbers of the columns and the rows
m = int(m)
n = int(n)
long = m+n-2
halflong = long/2
s = int(input())
# input the sum (only one integer)
initial =int( (1+m)*m/2 + m*(n-1) )
dif = initial-s
coor = dict()
for i in range(0,long):
    if i < halflong:
        coor[i+1]="D"
    else:
        coor[i+1]="R"
move = halflong
end = long
while dif>0:
    if end-move < dif:
        coor[move]="R"
        coor[end]="D"
        dif = dif-(end-move)
        end = end-1
        move = move-1
    else:
        coor[move+dif]="D"
        coor[move]="R"
        break
ans = str()
for i in range(1,long+1):
    ans += coor[i]
print(ans)
# output the path (one of the possible paths)
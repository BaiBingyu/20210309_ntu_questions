# Question 7.1.1
# 2 dimentional
# convert coordinate to index
# all of the integers are input successively
total = input().split()
coor = list()
for i in range(0, len(total)-1):
    if i%2 == 0:
        coor.append([int(total[i]),int(total[i+1])])
    else:
        pass
L = 50
for x in coor:
    print(L*x[1]+x[0])

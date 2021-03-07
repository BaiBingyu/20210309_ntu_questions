# Question 6
# I count the number of the points at which a ray from the given point intersects the polygon
points = list()
u = int(input()) # the number of the points
v = int(input()) # the number of the vertices of the polygon
# input the coordinate of the points
for i in range(u):
    [s, t] = input().split()
    points.append([int(s),int(t)])


poly_ini = list()
# input the coordinate of the vertices of the polygon
for i in range(v):
    [x, y] = input().split()
    poly_ini.append([x,y])
poly_ini.append(poly_ini[0])


# this function tells whether a given point is inside or outside the polygon
def judge(point):
    poly = list()
    # suppose the given point to be the original point
    # recompute the coordinates of the vertices of the polygon to simplify the calculations
    for item in poly_ini:
        poly.append([int(item[0])-point[0],int(item[1])-point[1]])
    p=len(poly)-1    
    ans=None
    # if the point is on the edge of the polygon
    for i in range(0, p):
        if poly[i][0]*poly[i+1][1]-poly[i+1][0]*poly[i][1] == 0:
            if poly[i][0]*poly[i+1][0] <= 0:
                ans = "Inside(On)"
                return ans
    cross=0
    # set the default intersection number
    for i in range(0, p):
        if poly[i][1]*poly[i+1][1]<0:
            if (poly[i+1][0]*poly[i][1]-poly[i][0]*poly[i+1][1])*\
            (poly[i][1]-poly[i+1][1]) > 0:
                # the intersect point is on the positive region of the x axis
                cross+=1
            else:
                pass
        elif poly[i][1]*poly[i+1][1]==0:
            # one of the vertices is on the positive region of the x axis
            if poly[i][1] == 0:
                # to avoid counting repeatatively
                if poly[i][0] > 0:
                    if i > 0:
                    # to ensure the index won't go out of range
                        if poly[i-1][1]*poly[i+1][1]>0:
                            # the ray just touches the vertex but goes through the segment
                            pass
                        elif poly[i-1][1]*poly[i+1][1]<0:
                            # the ray goes through the segment
                            cross+=1
                        else:
                            pass
                    else: # i==0
                        prev = poly[p-1][1]
                        if prev*poly[i+1][1]>0:
                            pass
                        elif prev*poly[i+1][1]<0:
                            cross+=1
                        else:
                            pass
                else:
                    pass
            else:
                pass
        else:
            pass
    if cross%2==0:
        ans = "Outside"
    else:
        ans = "Inside"
    return ans


for x in points:
    output = str()
    for y in x:
        output = output + str(y) + " "
    print(output,end="")
    print(judge(x))
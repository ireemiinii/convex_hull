# Author : İrem Bakır
#   This code I have written is an algorithm that finds the
#   largest convex of random 50 points.
#
#   Date : 06.04.2021
#
#
#I have defined the libraries I use
import random
import matplotlib.pyplot as plt
import time


#Time start in here
start_time = time.time()  
n = range(50)
border_points = []
set_of_points = []
non_hull_points = []

#Generate random points
for i in n :
    set_of_points.append((random.randint(0, 100), random.randint(0, 100)))

#Get slope of point x with to lowest point
def get_slope_with_lowest_point(x, lowest_point):
    try:
        return -(x[0] - lowest_point[0]) / (x[1] - lowest_point[1])
    except:
        if ((x[0] - lowest_point[0]) < 0):
            return 10000
        else:
            return -10000 + x[0] - lowest_point[0]


#Sort points according to y axis
set_of_points.sort(key=lambda x: x[1])
lowest_point = set_of_points.pop(0)

#Sort points according to slope with lowest_point
set_of_points.sort(key=lambda x: get_slope_with_lowest_point(x, lowest_point), reverse=True)

#Initialize hull
p1 = set_of_points.pop()
p2 = set_of_points.pop()
border_points.extend([lowest_point, p1, p2])


#Get orientation of 3 points
def orient(p1, p2, p3):
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    if (val == 0):
        return 0
    if (val > 0):
        return 1
    else:
        return 2


while (set_of_points):
    current_point = set_of_points.pop()
    current_point_orientation = orient(border_points[-1], current_point, border_points[-2])
#If counterclock wise add to hull
    if (current_point_orientation > 1):  
        border_points.append(current_point)
#Pop points till orientation is clockwise
    else:
        non_hull_points.append(border_points.pop())  
        while (True):
            try:
                current_point_orientation = orient(border_points[-1], current_point, border_points[-2])
                if (current_point_orientation < 2):
                    non_hull_points.append(border_points.pop())
                else:
                    break
            except:
                break
        border_points.append(current_point)

#Plot points
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter([x[0] for x in non_hull_points], [x[1] for x in non_hull_points], c='blue')  
ax.scatter([x[0] for x in border_points], [x[1] for x in border_points], c='red') 

#Join hull points
i = 0
while i < len(border_points):
    x, y = zip(border_points[i - 1], border_points[i])
    ax.plot(x, y, c='red')
    i += 1

end_time = time.time()  #End time in here
print('Graham Scan Time:', end_time - start_time)  #Print the difference between the two times
plt.show()




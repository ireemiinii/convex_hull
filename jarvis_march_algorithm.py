# Author : İrem Bakır
#   This code I have written is an algorithm that finds the
#   largest convex of random 50 points.
#
#   Date : 05.04.2021
#
#

#I have defined the libraries I use
import matplotlib.pyplot as plt
import random
import time

# Time start in here
start_time = time.time()


#I first defined them by creating a point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#I created the other class to define lines.
class line_vector(object):
    set_of_points = [] #List of points to stay in the convex
    border_points = [] #List of points that make up the sides of the convex

    def __init__(self):
        pass

    def add(self, point):
        self.set_of_points.append(point)
        
#The distance between two points.
    def distance_between_two_points(self,origin, p1, p2): 

        difference = (
            ((p2.x - origin.x) * (p1.y - origin.y))
            - ((p1.x - origin.x) * (p2.y - origin.y))
        )

        return difference

#Get leftmost point
    def leftmost_point(self):   
        points = self.set_of_points

        start = points[0]
        min_x = start.x
        for p in points[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        point = start
        self.border_points.append(start)

        far_point = None
        while far_point is not start:

#Get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
    
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self.distance_between_two_points(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self.border_points.append(far_point)
            point = far_point

    def jarvis_march(self):
        if self.set_of_points and not self.border_points:
            self.leftmost_point()

        return self.border_points
#Display set of points
    def display_points(self):
        x = [p.x for p in self.set_of_points]
        y = [p.y for p in self.set_of_points]
        plt.plot(x, y,'b',marker='.', linestyle='None')
#Display border points
    def display_envelope(self):
        hx = [p.x for p in self.border_points]
        hy = [p.y for p in self.border_points]
        plt.plot(hx, hy, 'r')

        plt.title('Convex Hull')
        end_time = time.time() #End time in here
        print('Jarvis March Time:', end_time - start_time) #Print the difference between the two times

        plt.show()
#Generate random points
def random_points():
    lv = line_vector()
    for _ in range(50):
        lv.add(Point(random.randint(0, 100), random.randint(0, 100)))
    print("Points on hull:", lv.jarvis_march())
    lv.display_points()
    lv.display_envelope()


random_points()


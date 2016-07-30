#The Actual Question:
# http://cemc.uwaterloo.ca/contests/computing/2016/CCOQR/data_structure.pdf
# https://dmoj.ca/problem/ccoqr16p3


#because sys.stdin.readline() is faster than input()
import sys

#reads and stores the first line of input 
(rowTot, m) = (sys.stdin.readline()).split()

#declares an array to keep the "coordinates" in
dataPoints = []

#adds stuff into the array
for i in range(0, int(m), 1):
    (r, c) = (sys.stdin.readline()).split()
    dataPoints.append([int(c), int(rowTot)+1 - int(r)])

#sorts the array so I can actually work without
#constantly checking through the whole array
dataPoints.sort()

#declares a variable to keep the actual answer in
output = 0

#This is a misnomer; first part is the current column and
#second is the number of filled rows in it
prevCol = dataPoints[0]

#because it should end if there are no points left
#but not before the last block is dealt with
while (len(dataPoints) > 0) or (prevCol[1] > 0):
    #pops in case of data points on the same column
    while len(dataPoints) > 1 and dataPoints[0][0] == dataPoints[1][0]:
        dataPoints.pop(0)
        
    #runs only if there's at least one more data point
    while (len(dataPoints) > 0):
        #runs only if there's another point in a column before the
        #most recent triangle ends
        if (prevCol[1] > (dataPoints[0][0] - prevCol[0])):
        #adds (most recent ammount of rows)*distance between last column and that of most recent data point
        #before subtracting the triangle at the top because it's part of a triangle
        #In other words, it calculates a rectangle before subtracting a triangle
            output = output + (
                (prevCol[1]*(dataPoints[0][0] - prevCol[0])) -
                ((dataPoints[0][0] - prevCol[0] - 1)**2 +
                 (dataPoints[0][0]- prevCol[0] - 1))/2)
        else:
            #just adds a triangle if the triangle can just run through
            output = output + (prevCol[1]*(prevCol[1] + 1))/2
        #designates the variable for the next data point
        #chooses what the higher number for what the row might be
        prevCol = [dataPoints[0][0],
                   max(dataPoints[0][1],
                       prevCol[1] -(dataPoints[0][0] - prevCol[0]))]
        #pops data we no longer need
        dataPoints.pop(0)

    #adds the last triangle now that there are no more points
    output = output + (prevCol[1]*(prevCol[1] + 1))/2
    #designates prevCol[1] as 0 so that the loop actually ends
    prevCol = [0, 0]

#prints the solution
print (int(output))

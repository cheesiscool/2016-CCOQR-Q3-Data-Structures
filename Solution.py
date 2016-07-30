import sys

(rowTot, m) = (sys.stdin.readline()).split()

dataPoints = []

for i in range(0, int(m), 1):
    (r, c) = (sys.stdin.readline()).split()
    dataPoints.append([int(c), int(rowTot)+1 - int(r)])

dataPoints.sort()
output = 0
prevCol = dataPoints[0]

while (len(dataPoints) > 0) or (prevCol[1] > 0):
    while len(dataPoints) > 1 and dataPoints[0][0] == dataPoints[1][0]:
        dataPoints.pop(0)
        
    while (len(dataPoints) > 0):
        if (prevCol[1] > (dataPoints[0][0] - prevCol[0])):
            output = output + (
                (prevCol[1]*(dataPoints[0][0] - prevCol[0])) -
                ((dataPoints[0][0] - prevCol[0] - 1)**2 +
                 (dataPoints[0][0]- prevCol[0] - 1))/2)
        else:
            output = output + (prevCol[1]*(prevCol[1] + 1))/2
        prevCol = [dataPoints[0][0],
                   max(dataPoints[0][1],
                       prevCol[1] -(dataPoints[0][0] - prevCol[0]))]
        dataPoints.pop(0)

    output = output + (prevCol[1]*(prevCol[1] + 1))/2
    prevCol = [0, 0]


print (int(output))

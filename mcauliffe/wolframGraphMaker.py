import random

def nodeList(xNum, yNum):
	out = []
	for i in range(0,xNum):
		out.append([])
		for j in range(i*yNum,yNum+i*yNum):
			out[i].append(j+1)
	return out

def listEdges(edgeList):

	edgeList = []
	sums = []

	for i in range(0,len(nodes)):
		for j in range(0, len(nodes[i])):
			try:
				current = nodes[i][j]
			except:
				current = None
			try:
				across = nodes[i+1][j]
				if not(current==across):
					edgeList.append(str(current)+"<->"+str(across))
			except:
				across = None
			try:
				down = nodes[i][j+1]
				if not(current==down):
					edgeList.append(str(current)+"<->"+str(down))
			except:
				across = None
			try:
				upRight = nodes[i+1][j+1]
				if not(str(current + upRight) in sums) or not(current==upRight):
					edgeList.append(str(current)+"<->"+str(upRight))
				
					sums.append(str(current)+str(upRight))
					sums.append(str(upRight)+str(current))
			except:
				upRight = None
			try:
				assert j-1>=0
				downRight = nodes[i+1][j-1]

				if not(str(current + downRight) in sums) or not(current==downRight):
					edgeList.append(str(current)+"<->"+str(downRight))
				
					sums.append(str(current)+str(downRight))
					sums.append(str(downRight)+str(current))
			except:
				downRight = None

	return edgeList
def wolframFormatEdges(inList):
	wolfString = "{"

	for i in inList:
		wolfString = wolfString + i + ","

	return wolfString[:-1] + "}"

def weightsList(edges, velocityList): #add direction in future
	outputList = []
	for i in range(0, len(edges)):
		outputList.append(1/velocityList[i])
	
	outputString = str(outputList).strip("[")
	outputString = outputString.strip("]")
	
	return ", EdgeWeight->" + "{" + outputString + "}"

nodes = nodeList(10,10)
listOfEdges = listEdges(nodes)

velocityList = []
for x in range (0, len(listOfEdges)):
    velocityList.append(random.randint(1, 20))

weights = weightsList(listOfEdges, velocityList)
edges = wolframFormatEdges(listOfEdges)

# print(listOfEdges)

print("[" + edges + weights + "]")
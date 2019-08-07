import sys
import numpy as np

p = float(sys.argv[3])
f = open(sys.argv[1])

maze = []
while  True:
	line = f.readline()
	if line == "":
		break
	arr = line.split()
	arr = [int(x) for x in arr]
	maze.append(arr)
		
cols = len(maze[0])
rows = len(maze)
numStates = rows*cols
numActions = 4
start = -1
end = -1

acs = [[] for _ in range(numStates)]

for i in range(rows):
	for j in range(cols):
		if maze[i][j] == 0 or maze[i][j] == 2:

			if i != 0 and maze[i-1][j] != 1:
				acs[i*cols + j].append(0)

			if j!= 0 and maze[i][j-1] != 1:
				acs[i*cols + j].append(1)

			if j != (cols-1) and maze[i][j+1] != 1:
				acs[i*cols + j].append(2)

			if i != (rows-1) and maze[i+1][j] != 1:
				acs[i*cols + j].append(3)


		if maze[i][j] == 2:
			start = i*cols + j

		if maze[i][j] == 3:
			end = i*cols + j


f = open(sys.argv[2])
P = []
while  True:
	line = f.readline()
	if line.split()[0] == "iterations":
		break
	P.append(int(line.split()[1]))

state = start
actions = []

while state != end:
	a = P[state]
	a_s = acs[state]
	n = len(a_s)

	pd = []

	for i in range(n) :
		if a_s[i] == a :
			pd.append(p + (1-p)/n)
		else:
			pd.append((1-p)/n)

	

	a = np.random.choice(a_s,1,p = pd)


	actions.append(a)
	if a == 0:
		state = state - cols
	elif a == 1:
		state = state - 1
	elif a == 2:
		state = state + 1
	elif a == 3:
		state = state + cols
	

for i in range(len(actions)):
	if actions[i] == 0:
		actions[i] = 'N'
	if actions[i] == 1:
		actions[i] = 'W'
	if actions[i] == 2:
		actions[i] = 'E'
	if actions[i] == 3:
		actions[i] = 'S'
	
print(' '.join(map(str, actions)) )
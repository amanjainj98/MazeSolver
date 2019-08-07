import sys

p = float(sys.argv[2])
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
transitions = [ dict() for _ in range(numStates)]

for i in range(rows):
	for j in range(cols):
		if maze[i][j] == 0 or maze[i][j] == 2:

			acs = []
			ns = []

			if i != 0 and maze[i-1][j] != 1:
				acs.append(0)
				ns.append((i-1)*cols + j)

			if j!= 0 and maze[i][j-1] != 1:
				acs.append(1)
				ns.append(i*cols + j-1)

			if j != (cols-1) and maze[i][j+1] != 1:
				acs.append(2)
				ns.append(i*cols + j+1)

			if i != (rows-1) and maze[i+1][j] != 1:
				acs.append(3)
				ns.append((i+1)*cols + j)


			n = len(acs)


			if n !=0:

				for a in range(len(acs)):
					for b in range(len(acs)):
						if a==b :
							if acs[a] in transitions[i*cols + j]:
								transitions[i*cols + j][acs[a]].append(tuple([ns[b],-1,p + (1-p)/n]))
							else:
								transitions[i*cols + j][acs[a]] = [tuple([ns[b],-1,p + (1-p)/n])]
								
						else :
							if acs[a] in transitions[i*cols + j]:
								transitions[i*cols + j][acs[a]].append(tuple([ns[b],-1,(1-p)/n]))
							else:
								transitions[i*cols + j][acs[a]] = [tuple([ns[b],-1,(1-p)/n])]


		if maze[i][j] == 2:
			start = i*cols + j

		if maze[i][j] == 3:
			end = i*cols + j


print("numStates",numStates)
print("numActions",numActions)
print("start",start)
print("end",end)

for i in range(numStates):
	if transitions[i]:
		for key in transitions[i].keys():
			l = transitions[i][key]
			for j in range(len(l)):
				print("transition",i,key,l[j][0],l[j][1],l[j][2])


print("discount",1.0)

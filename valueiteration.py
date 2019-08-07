import sys
import random

f = open(sys.argv[1])
numStates = int(f.readline().split()[1])
numActions = int(f.readline().split()[1])
start = int(f.readline().split()[1])
end = f.readline().split()[1:]
end = [int(x) for x in end]

transitions = [ dict() for _ in range(numStates)]

line = ""

# print(numStates,numActions,start,end)

while  True:
	line = f.readline()
	s = line.split()
	if s[0] == "discount":
		break

	if int(s[2]) in transitions[int(s[1])]:

		transitions[int(s[1])][int(s[2])].append(tuple([int(s[3]),float(s[4]),float(s[5])]))

	else:
		transitions[int(s[1])][int(s[2])] = [tuple([int(s[3]),float(s[4]),float(s[5])])]

discount = float(line.split()[1])


def not_close_enough(V1,V2):
	for s in range(numStates):
		if abs(V1[s] - V2[s]) > 10**(-16) :
			return True
	return False



V = [ 1.0 for _ in range(numStates)]
V1 = [ 0.0 for _ in range(numStates)]
P = [ -1 for _ in range(numStates)]

iterations = 0


while not_close_enough(V1,V):
	V = V1.copy()

	for s in range(numStates):
		if s in end:
			continue

		maxm = -1 * float('inf')
		action = -1
		for a in range(numActions) :
			if a not in transitions[s]:
				continue

			l = transitions[s][a]
			summ = 0.0
			for i in range(len(l)):
				s1 = l[i][0]
				summ = summ + (l[i][2]*(l[i][1] + discount*V[s1]))

			if summ > maxm:
				maxm = summ
				action = a

		V1[s] = maxm
		P[s] = action

	iterations = iterations + 1

for s in range(numStates):
	print(round(V1[s],11),P[s])

print("iterations", iterations)


# print(numStates,numActions,start,end,transitions[2][1])
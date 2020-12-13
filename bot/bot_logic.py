import random

def random_filling(T):
    l = [r*3+c for r in range(3) for c in range(3) if not T[r][c]]
    return random.choice(l)

def not_finished(T):
	Finished = False

	for r in T:
		if r[0]==r[1] and r[1]==r[2] and r[2]!=0 :
			Finished = True

	if not Finished :
		for n in range(3):
			l = [T[m][n] for m in range(3)]
			if l[0]==l[1] and l[1]==l[2] and l[2]!=0 :
				Finished = True

	if not Finished :
		l = [T[n][n] for n in range(3)]
		if l[0]==l[1] and l[1]==l[2] and l[2]!=0 :
			Finished = True

	if not Finished :
		l = [T[2-n][n] for n in range(3)]
		if l[0]==l[1] and l[1]==l[2] and l[2]!=0 :
			Finished = True

	if Finished:
		print("by not finished")
		return 9
	else:
		return random_filling(T)

def checking_validity(T):

	num = [0]*3

	for r in T:
		for c in r:
			num[c]+=1

	if num[1] - num[2] == 1 and num[0] != 0 :
		return not_finished(T)
	else :
		print("check")
		return 9

def main(T):
    return checking_validity(T)

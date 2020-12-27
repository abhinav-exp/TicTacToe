import random

def random_filling(T):
    l = [r*3+c for r in range(3) for c in range(3) if not T[r][c]]
    return random.choice(l)

def fun_loose_plan(T):
	R = [False]*3
	C = [False]*3
	D = [False]*3

	def fun(L):
		return L in [[1,0,0], [0,1,0], [0,0,1]]

	for r in range(3):
		if fun(T[r]):
			R[r] = True

	for c in range(3):
		if fun([r[c] for r in T]):
			C[c] = True

	if fun([T[n][n] for n in range(3)]):
		D[0] = True

	if fun([T[n][2-n] for n in range(3)]):
		D[1] = True

	for r in range(3):
		for c in range(3):
			if not T[r][c]:
				if R[r]*C[c]:
					return r*3+c
				if r==c and D[0]*(R[r]+C[c]):
					return r*3+c
				if r+c == 2 and D[1]*(R[r]+C[c]):
					return r*3+c
				if r==c and r+c == 2 and D[0]*D[1]:
					return r*3+c

	return random_filling(T)

def fun_win_plan(T):
	R = [False]*3
	C = [False]*3
	D = [False]*3

	def fun(L):
		return L in [[2,0,0], [0,2,0], [0,0,2]]

	for r in range(3):
		if fun(T[r]):
			R[r] = True

	for c in range(3):
		if fun([r[c] for r in T]):
			C[c] = True

	if fun([T[n][n] for n in range(3)]):
		D[0] = True

	if fun([T[n][2-n] for n in range(3)]):
		D[1] = True

	for r in range(3):
		for c in range(3):
			if not T[r][c]:
				if R[r]*C[c]:
					return r*3+c
				if r==c and D[0]*(R[r]+C[c]):
					return r*3+c
				if r+c == 2 and D[1]*(R[r]+C[c]):
					return r*3+c
				if r==c and r+c == 2 and D[0]*D[1]:
					return r*3+c

	return fun_loose_plan(T)

def fun_loosing_option(T):

	def fun(L):
		return L in [[1,1,0], [0,1,1], [1,0,1]]

	for r in range(3):
		for c in range(3):
			if not T[r][c]:
				if fun(T[r]):
					return r*3+c
				if fun([T[n][c] for n in range(3)]):
					return r*3+c
				if r==c and fun([T[n][n] for n in range(3)]):
					return r*3+c
				if r+c==2 and fun([T[n][2-n] for n in range(3)]):
					return r*3+c

	return fun_win_plan(T)

def fun_winning_option(T):

	def fun(L):
		return L in [[2,2,0], [0,2,2], [2,0,2]]

	for r in range(3):
		for c in range(3):
			if not T[r][c]:
				if fun(T[r]):
					return r*3+c
				if fun([T[n][c] for n in range(3)]):
					return r*3+c
				if r==c and fun([T[n][n] for n in range(3)]):
					return r*3+c
				if r+c==2 and fun([T[n][2-n] for n in range(3)]):
					return r*3+c

	return fun_loosing_option(T)


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
		return fun_winning_option(T)

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

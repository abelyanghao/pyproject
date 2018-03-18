from random import choice
import copy
def f(list):
	if len(list) < 2:
		return list
	for i, a in enumerate(list):
		if a == 0:
			break
	j = min(i + 1, len(list))
	while j < len(list) and i < len(list):
		while list[j] == 0 and j < len(list) - 1:
			j += 1
		while list[i] != 0 and i < len(list) - 1:
			i += 1
		list[i] = list[j]
		list[j] = 0
		i += 1
		j += 1
	return list

#重复合并
def meger(list, i):
	while list[i] == list[i - 1]:
			list[i - 1] *= 2
			list[i] = 0
			i -= 1
	return i

def f1(list):
	for i, a in enumerate(list):
		if a == 0: 
			break
	if i == len(list) - 1:
		i = len(list)
	while i >= 1:
		i = meger(list, i - 1)
	return list

def shift(list):
	if len(list) < 2:
		return list
	f(f1(f(list)))
	while list[0] == list[1] and list[0] != 0:
		f(f1(f(list)))
	return list

#矩阵转置 按主对角线
def re1(state):
	for i in range(1,4):
		for j in range(i):
			state[i][j], state[j][i] = state[j][i], state[i][j]
#矩阵转置 按副对角线
def re2(state):  
	for i in range(3):
		for j in range(3 - i):
			state[i][j], state[3 - j][3 - i] = state[3 - j][3 - i], state[i][j]

#矩阵左右翻转
def re3(state):
	for i in range(4):
		for j in range(2):
			state[i][j], state[i][3 - j] = state[i][3 - j], state[i][j]

def move(state,action):
	if action == 'a':      #往左移动
		for i in range(4):
			shift(state[i])
	if action == 'w':      #往上移动
		re1(state)
		for i in range(4):
			shift(state[i])
		re1(state)
	if action == 's':      #往下移动
		re2(state)
		for i in range(4):
			shift(state[i])
		re2(state)
	if action == 'd':     #向右移动
		re3(state)
		for i in range(4):
			shift(state[i])
		re3(state)
	return state


def myPrint(state):
	for i in range(4):
		for j in range(4):
			print(state[i][j],end = '   ')
		print()

def main():
	init_state = [[0,4,4,2],
		[8,8,8,4],
		[0,0,2,2],
		[0,0,0,0]]
	myPrint(init_state)
	old_state = init_state
	action = 'q'
	new_action = input('欢迎进入，请输入下一步操作:')
	while action != new_action:
		state = copy.deepcopy(old_state)
		new_state = move(old_state,new_action)
		if new_state != state:
			for i in range(4):
				for j in range(4):
					if new_state[i][j] == 0:
						new_state[i][j] = choice([0,0,0,0,0,0,0,2,4])
		else:
			flag = True
			for i in range(4):
				for j in range(4):
					if new_state[i][j] == 0:
						flag = False
						break
			if flag:
				print('you lose')
		myPrint(new_state)
		new_action = input('请输入下一步操作:')



main()
'''init_state = [[0,4,4,2],
		[8,8,8,4],
		[0,0,2,2],
		[0,0,0,0]]

for i in range(4):
	for j in range(4):
		if init_state[i][j] == 0:
			init_state[i][j] = choice([0,2,4])
myPrint(init_state)'''


'''def test(state):
	print('old_state:')
	myPrint(state)
	print('new_state:')
	myPrint(move(state,'a'))
	print()
	myPrint(state)

test([[0,4,4,2],
	[8,8,8,4],
	[0,0,2,2],
	[0,0,0,0]])'''


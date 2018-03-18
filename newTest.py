from random import choice
import copy
from tkinter import *

class chessboard(object):
	def __init__(self, init_state, r, c):
		super(chessboard, self).__init__()
		self.init_state = init_state
		self.r = r
		self.c = c
		old_state = None
    
	def get_state(self):
		return self.init_state

	#moveleft函数实现list中非零数字左移	
	def moveleft(self, list):
		num = -1     
		for key in list:
			if key != 0:
				num += 1
				list[num] = key	
		for i in range(num + 1 , len(list)):
			list[i] = 0
		return num

	#meger函数实现list中索引i向左相邻重复数字合并，只进行一次
	def meger(self, list, i):
		while list[i] == list[i - 1]:
				list[i - 1] *= 2
				list[i] = 0
				i -= 1
		return i
	
	#megerall函数实现list（非零元素靠左）中从右到左动态重复合并（右优先)
	def megerall(self, list):
		i = self.moveleft(list)
		while i >= 1:
			i = self.meger(list, i)
			if i > 0 and list[i - 1] != list[i]:
				i -= 1
		self.moveleft(list)

	#numRandom函数找到所有空位，并在两个位置随机生成2或4
	def numRandom(self):
		l = []
		if self.old_state != self.init_state:
			for i in range(self.r):
				for j in range(self.c):
					if self.init_state[i][j] == 0:
						l.append([i,j])
			for k in range(2):
				r = choice(range(len(l)))
				i, j = l[r][0], l[r][1]
				self.init_state[i][j] = choice([2,4])

	#choose函数实现取指定的一行（从左到右）或者一列（从上到下）元素组成一个list
	def choose(self, i, dir):
		choose_list = []
		if dir == 'r':
			for j in range(self.c):
				choose_list.append(self.init_state[i][j])
		if dir == 'c':
			for j in range(self.r):
				choose_list.append(self.init_state[j][i])
		return choose_list

	#place函数实现放置一行（从左到右）或者一列（从上到下）
	def place(self, i, dir, list):
		if dir == 'r':
			self.init_state[i] = list
		if dir == 'c':
			for j in range(self.r):
				self.init_state[j][i] = list[j]

	#move实现棋盘按方向移动
	def move(self, action):
		if action == 'a':   #向左
			for i in range(self.r):
				self.megerall(self.init_state[i])
		if action == 'w':   #向上
			for i in range(self.c):
				choose_list = self.choose(i, 'c')
				self.megerall(choose_list)
				self.place(i, 'c', choose_list)
		if action == 's':   #向下
			for i in range(self.c):
				choose_list = self.choose(i, 'c')
				choose_list.reverse()
				self.megerall(choose_list)
				choose_list.reverse()
				self.place(i, 'c', choose_list)
		if action == 'd':   #向右
			for i in range(self.r):
				choose_list = self.choose(i, 'r')
				choose_list.reverse()
				self.megerall(choose_list)
				choose_list.reverse()
				self.place(i, 'r', choose_list)


	#move_random函数实现棋盘整体向指定方向移动,并且在棋盘改变之后随机增加数字
	def move_random(self, action):
		self.old_state = copy.deepcopy(self.init_state)
		self.move(action)
		self.numRandom()
	
init_state = [[0,0,0,2],
				[0,0,0,2],
				[4,2,0,0],
				[0,0,0,2]]
r, c = 4, 4
chess = chessboard(init_state, r, c)


root = Tk()

chessframe = Frame(root, height = 400, width = 400, bg = 'pink')
chessframe.pack(side = 'top')

elements = [[],[],[],[]]
state = chess.get_state()
for i in range(r):
	for j in range(c):
		elements[i].append(Button(chessframe, font = 25, height = 5, width = 10, text = state[i][j] if state[i][j] != 0 else '', fg = 'red'))
		elements[i][j].grid(row = i, column = j)

def wtf_w():
	def myshfit(state):
		print("向上")
		for i in range(r):
			for j in range(c):
				elements[i][j]['text'] = state[i][j] if state[i][j] != 0 else ''
	chess.move_random('w')
	myshfit(chess.get_state())

def wtf_a():
	def myshfit(state):
		print("向左")
		for i in range(r):
			for j in range(c):
				elements[i][j]['text'] = state[i][j] if state[i][j] != 0 else ''
	chess.move_random('a')
	myshfit(chess.get_state())

def wtf_s():
	def myshfit(state):
		print("向下")
		for i in range(r):
			for j in range(c):
				elements[i][j]['text'] = state[i][j] if state[i][j] != 0 else ''
	chess.move_random('s')
	myshfit(chess.get_state())

def wtf_d():
	def myshfit(state):
		print("向右")
		for i in range(r):
			for j in range(c):
				elements[i][j]['text'] = state[i][j] if state[i][j] != 0 else ''
	chess.move_random('d')
	myshfit(chess.get_state())

text = {'向上': wtf_w, '向左': wtf_a, '向下': wtf_s, '向右': wtf_d}
for key, value in text.items():
	quit = Button(text = key, fg = "red", command = value)
	quit.pack(side = "left")

root.mainloop()




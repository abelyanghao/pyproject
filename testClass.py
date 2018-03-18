from random import choice
import copy
from tkinter import *

class chessboard:
	init_state = [[0,0,0,2],
				[0,0,0,2],
				[4,2,0,0],
				[0,0,0,2]]
	old_state = None

	#moveleft函数实现list中非零数字左移			
	def moveleft(list):
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

	#meger函数实现list中索引i向左相邻重复数字合并
	def meger(list, i):
		while list[i] == list[i - 1]:
				list[i - 1] *= 2
				list[i] = 0
				i -= 1
		return i

	#megerall函数实现list中所有重复数字的合并,但会产生空格
	def megerall(self, list):
		for i, a in enumerate(list):
			if a == 0: 
				break
		if i == len(list) - 1:
			i = len(list)
		while i >= 1:
			i = self.meger(list, i - 1)
		return list

	#shift函数完成最终移动后的状态
	def shift(self, list):
		if len(list) < 2:
			return list
		self.moveleft(self.megerall(self, self.moveleft(list)))
		while list[0] == list[1] and list[0] != 0:
			self.moveleft(self.megerall(self, self.moveleft(list)))
		return list

	#矩阵转置 按主对角线
	def re1(self):
		for i in range(1,4):
			for j in range(i):
				self.init_state[i][j], self.init_state[j][i] = self.init_state[j][i], self.init_state[i][j]
	#矩阵转置 按副对角线
	def re2(self):  
		for i in range(3):
			for j in range(3 - i):
				self.init_state[i][j], self.init_state[3 - j][3 - i] = self.init_state[3 - j][3 - i], self.init_state[i][j]

	#矩阵左右翻转
	def re3(self):
		for i in range(4):
			for j in range(2):
				self.init_state[i][j], self.init_state[i][3 - j] = self.init_state[i][3 - j], self.init_state[i][j]

	#move函数实现棋盘整体向指定方向移动
	def move(self, action):
		self.old_state = copy.deepcopy(self.init_state)
		if action == 'a':      #往左移动
			for i in range(4):
				self.shift(self, self.init_state[i])
		if action == 'w':      #往上移动
			self.re1(self)
			for i in range(4):
				self.shift(self, self.init_state[i])
			self.re1(self)
		if action == 's':      #往下移动
			self.re2(self)
			for i in range(4):
				self.shift(self, self.init_state[i])
			self.re2(self)
		if action == 'd':     #向右移动
			self.re3(self)
			for i in range(4):
				self.shift(self, self.init_state[i])
			self.re3(self)
		return self.init_state

	#numRandom函数找到所有空位，并在两个位置随机生成2或4
	def numRandom(self):
		l = []
		if self.old_state != self.init_state:
			for i in range(4):
				for j in range(4):
					if self.init_state[i][j] == 0:
						l.append([i,j])
			for k in range(2):
				r = choice(range(len(l)))
				i, j = l[r][0], l[r][1]
				self.init_state[i][j] = choice([2,4])
			
		else:
			flag = True
			for i in range(4):
				for j in range(4):
					if self.init_state[i][j] == 0:
						flag = False
						break
			if flag:
				print('you lose')
		return self.init_state

    #打印棋盘
	def myPrint(self):
		for i in range(4):
			for j in range(4):
				print(self.init_state[i][j],end = '   ')
			print()

c = chessboard

root = Tk()

chessframe = Frame(root, height = 400, width = 400, bg = 'pink')
chessframe.pack(side = 'top')

elements = [[],[],[],[]]
for i in range(4):
	for j in range(4):
		elements[i].append(Button(chessframe, font = 25, height = 5, width = 10, text = c.init_state[i][j] if c.init_state[i][j] != 0 else '', fg = 'red'))
		elements[i][j].grid(row = i, column = j)



def wtf_w():
	def myshfit(state):
		print("向上")
		for i in range(4):
			for j in range(4):
				elements[i][j]['text'] = state[i][j] if state[i][j] != 0 else ''
	c.move(c,'w')
	myshfit(c.numRandom(c))

def wtf_a():
	def myshfit(state):
		print("向左")
		for i in range(4):
			for j in range(4):
				elements[i][j]['text'] = state[i][j] if state[i][j] != 0 else ''
	c.move(c,'a')
	myshfit(c.numRandom(c))

def wtf_s():
	def myshfit(state):
		print("向下")
		for i in range(4):
			for j in range(4):
				elements[i][j]['text'] = state[i][j] if state[i][j] != 0 else ''
	c.move(c,'s')
	myshfit(c.numRandom(c))

def wtf_d():
	def myshfit(state):
		print("向右")
		for i in range(4):
			for j in range(4):
				elements[i][j]['text'] = state[i][j] if state[i][j] != 0 else ''
	c.move(c,'d')
	myshfit(c.numRandom(c))

text = {'向上': wtf_w, '向左': wtf_a, '向下': wtf_s, '向右': wtf_d}
for key, value in text.items():
	quit = Button(text = key, fg = "red", command = value)
	quit.pack(side = "left")

root.mainloop()

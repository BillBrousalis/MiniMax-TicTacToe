#!/usr/bin/env python3
import tictactoe

class minimax():
	def __init__(self):
		print('initializing minimax class...')

	def calc(self, sample_state, turn):
		self.env = tictactoe.tictactoe()
		self.ai = turn
		self.state = sample_state
		#self.winner, self.done = self.env.minimax_check(self.state, -self.ai)
		self.current_state = sample_state 
		max_A, pos = self.max()
		return max_A, pos
	
	def max(self):
		# -1 > loss , 0 > tie , +1 > win
		maxv = -2
		p = None
		self.winner, self.done = self.env.minimax_check(self.current_state)
		if self.winner != None:
			# if ai won
			if self.winner == self.ai:
				return (1, 0)
			# if ai opponent won
			else:
				return (-1, 0)
		elif self.done:
			# tie
			return (0, 0)
	
		for pos in range(0, 9):
			# if pos is empty
			if self.current_state[pos] == 0:
				self.current_state[pos] = self.ai    
				(m, min_pos) = self.min()
				if m > maxv:
					maxv = m
					p = pos
					#print(f'current : {maxv} , {p}')
				self.current_state[pos] = 0
		return (maxv, p)

	def min(self):
		minv = 2
		q = None
		self.winner, self.done = self.env.minimax_check(self.current_state)
		if self.winner != None:
			if self.winner == self.ai:
				return (1, 0)
			else:
				return (-1, 0)
		elif self.done:
			return (0, 0)
		for pos in range(0, 9):
			if self.current_state[pos] == 0:
				self.current_state[pos] = -self.ai
				(m, max_pos) = self.max()
				if m < minv:
					minv = m
					q = pos
					#print(f'current : {minv} , {q}')
				self.current_state[pos] = 0
		return (minv, q)

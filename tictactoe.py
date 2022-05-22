#!/usr/bin/env python3
import numpy as np
import os, sys

sys.path.append(os.getcwd())
class tictactoe():
	def __init__(self):
		self.reset()
	
	def reset(self):
		self.winner = None
		self.step_count = 0
		self.done = False
		self.state = [0] * 9
		self.turn = 1
		return self.state

	def minimax_check(self, sample_state):
		winner = None
		done = False
		s = sample_state
		for i in range(3):
			if s[3*i] != 0 and all([x==s[3*i] for x in s[3*i:3*i+3]]):
				winner = s[3*i] 
			elif s[i] != 0 and all([x==s[i] for x in [s[i], s[3+i], s[6+i]]]):
				winner = s[i] 
		if s[0] != 0 and all([x==s[0] for x in [s[0], s[4], s[8]]]):
			winner = s[0] 
		elif s[2] != 0 and all([x==s[2] for x in [s[2], s[4], s[6]]]):
			winner = s[2] 
		
		if winner != None:
			done = True
		elif sample_state.count(0) == 0:
			done = True
		return winner, done

	def iswinner(self, sample_state):
		s = sample_state
		# checking horizontal - vertical axis
		for i in range(3):
			if all([x==self.turn for x in s[3*i:3*i+3]]):
				self.winner = self.turn
				return True
			elif all([x==self.turn for x in [s[i], s[3+i], s[6+i]]]):
				self.winner = self.turn
				return True
		# checking diagonals
		if all([x==self.turn for x in [s[0], s[4], s[8]]]):
			self.winner = self.turn
			return True
		elif all([x==self.turn for x in [s[2], s[4], s[6]]]):
			self.winner = self.turn
			return True
		return False

	def step(self, act):
		turn = self.turn
		last_state = [x for x in self.state] 
		self.step_count += 1
		if self.state[act] != 0:
			# make illegal move = LOSE 
			print('#### ILLEGAL MOVE ####')
			self.done = True
		else:
			self.state[act] = self.turn
			if self.iswinner(self.state):
				# WIN
				winner = 'X' if self.turn == 1 else 'O'
				print(f'#### PLAYER {winner} WON ####')
				self.done = True
			else:
				if self.step_count >= 9:
					# TIE
					self.done = True
					print('#### TIE ####')
				self.turn = -self.turn
		return self.state, self.done

	def winner(self):
		return self.winner

	def load_state(self):
		return self.state

	def render(self):
		indexing = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
		#print('current board state:')
		board_render = '+-----------+   +-----------+\n'
		for row in range(3):
			board_render += '|'
			for col in range(3):
				symbol = self.state[3*row+col]
				if symbol == 1:
					symbol = ' X '
				elif symbol == -1:
					symbol = ' O '
				else:
					symbol = '   '
				board_render += f'{symbol}|' 
			board_render += f'   | {indexing[row][0]} | {indexing[row][1]} | {indexing[row][2]} |'
			board_render += '\n'
			board_render += '+-----------+   +-----------+\n'
		print(board_render)

if __name__ == '__main__':
	# EXAMPLE GAME
	env = tictactoe()
	env.step(4)
	env.render()
	env.step(8)
	env.render()
	env.step(1)
	env.render()
	env.step(5)
	env.render()
	env.step(7)
	env.render()

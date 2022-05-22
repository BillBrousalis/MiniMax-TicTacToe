#!/usr/bin/env python3
import time
import tictactoe
import minimax

class game():
  def __init__(self):
    self.ai_first = False
    self.minimax = minimax.minimax()
    self.env = tictactoe.tictactoe()
    self.env.reset()

  def play(self):
    turn  = 1 
    if self.ai_first: 
      turn = -turn
    self.env.render()
    time.sleep(0.5)
    while not self.env.done:
      print(f'state : {self.env.state}')
      if turn == 1:
        self.usr_move()
      else:
        self.ai_move()
      turn = -turn
      self.env.render()

  def ai_alone(self):
    while not self.env.done:
      self.ai_move()
      self.env.render()
      time.sleep(0.5)

  def usr_move(self):
    print('Enter pos to play ([0-8]) :')
    m = input()
    try:
      m = int(m, 10)
      if m > 8 or m < 0:
        exit()
    except:
      print('that was not a number...')
      exit()
    self.env.step(m)

  def ai_move(self):
    state = self.env.load_state()
    maxv, best_pos = self.minimax.calc(state, self.env.turn)
    print(f'playing : ({best_pos})')
    self.env.step(best_pos)

if __name__ == '__main__':
  mygame = game()
  c = input("1. Play vs AI\n2. AI vs itself\n> ")
  if c == '1':
    mygame.play()
  elif c == '2':
    mygame.ai_alone()
  else:
    print(f"Invalid option [ {c} ]")

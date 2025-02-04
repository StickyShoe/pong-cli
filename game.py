from os import system, name
import pyautogui
import keyboard
from pynput.keyboard import Key, Controller
mykeyboard = Controller()

import math

from time import sleep

i = 0

cells = {
        '0': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '1': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '2': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '3': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '4': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '5': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '6': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '7': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ']
        }

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

ball_speed = 25
randomness = 3

paddle1_y = 3
paddle2_y = 4

ball_x = 3
ball_y = 3

x_speed = 1
y_speed = 1


def position_paddle1():
    cells[str(paddle1_y)][1] = 'X'

def position_ball():
    cells[str(ball_y)][ball_x] = 'O'


def draw_board():
    for row in cells:
        column = cells[row]
        print(''.join([x for x in column]))

def get_input():
    global paddle1_y
    if keyboard.is_pressed('j'):
        cells[str(paddle1_y)][1] = '|'
        paddle1_y += 1
    if keyboard.is_pressed('k'):
        cells[str(paddle1_y)][1] = '|'
        paddle1_y -= 1

while True:
    if ball_x > 10:
        x_speed = -1
    if ball_x < 2:
        x_speed = 1
    if ball_y < 1:
        y_speed = 1
    if ball_y > 6:
        y_speed = -1
    ball_x += x_speed
    ball_y += y_speed
    draw_board()
    get_input()
    position_paddle1()
    cells[str((ball_y - y_speed))][ball_x - x_speed] = ' '
    position_ball()
    #print((' ' * abs(int(math.sin(i)*ball_speed))) + 'O')
    sleep(0.1)
    #i += 1
    clear()


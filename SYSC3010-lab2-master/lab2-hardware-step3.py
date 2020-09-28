#Used an offical RPi Project, the website provided general guidelines to complete the code,
#This is the code to run PONG on the sense hat.
#https://projects.raspberrypi.org/en/projects/sense-hat-pong

from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
red = (255,0,0)
sense.clear()
bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_bat():
  sense.set_pixel(0,bat_y, 0,0,255)
  sense.set_pixel(0,bat_y-1, 0,0,255)
  sense.set_pixel(0,bat_y+1, 0,0,255)

def draw_ball():
  sense.set_pixel(ball_position[0],ball_position[1], 0,255,0)
  ball_position[0] += ball_velocity[0]
  if ball_position[0] == 7 or ball_position[0] == 0:
    ball_velocity[0] = -ball_velocity[0]
  if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y + 1):
    ball_velocity[0] = -ball_velocity[0]
  if ball_position[0] == 0:
    sense.show_message("You Lose")


def move_up(event):
  global bat_y
  if event.action =='pressed' and bat_y > 1:
    bat_y -= 1;



def move_down(event):
  global bat_y
  if event.action =='pressed' and bat_y < 6:
    bat_y += 1;
  
#main
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
while True:
  sense.clear(0, 0, 0)
  draw_bat()
  draw_ball()
  sleep (0.25)


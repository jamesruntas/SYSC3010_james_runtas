import sense_hat
from time import sleep, time
from random import randint

sense = sense_hat.SenseHat()
sense.clear()



letter_color = (200,200,0)  
counter = 0;

up_key = sense_hat.DIRECTION_UP
down_key = sense_hat.DIRECTION_DOWN
right_key = sense_hat.DIRECTION_RIGHT
left_key = sense_hat.DIRECTION_LEFT
pressed = sense_hat.ACTION_PRESSED
Y = (255, 255, 0)

B = (0, 0, 255)
X = (0, 0, 0)

j_output = [
    X, X, X, X, X, X, X, X,
    X, X, X, Y, Y, Y, X, X,
    X, X, X, X, Y, X, X, X,
    X, X, X, X, Y, X, X, X,
    X, X, X, X, Y, X, X, X,
    X, X, Y, X, Y, X, X, X,
    X, X, Y, Y, Y, X, X, X,
    X, X, X, X, X, X, X, X
  ]
r_output = [
    X, X, X, X, X, X, X, X,
    X, X, B, B, B, X, X, X,
    X, X, B, X, B, X, X, X,
    X, X, B, B, B, X, X, X,
    X, X, B, B, X, X, X, X,
    X, X, B, X, B, X, X, X,
    X, X, B, X, B, X, X, X,
    X, X, B, X, B, X, X, X
  ]

def drawJ ():
  if (counter % 2) == 0:
    sense.clear()
    sense.set_pixels(j_output)
  else:
    return

def drawR ():
  if (counter % 2) != 0:
    sense.clear()
    sense.set_pixels(r_output)
  else:
    return
  
while True:

  events = sense.stick.get_events()
  if events:
    for e in events:
      if e.direction ==  up_key and e.action == pressed:
        counter = counter + 1;
        drawJ()
        drawR()
      elif e.direction ==  down_key and e.action == pressed:
        counter = counter + 1;
        drawJ()
        drawR()
      elif e.direction ==  right_key and e.action == pressed:
        counter = counter + 1;
        drawJ()
        drawR()
      elif e.direction ==  left_key and e.action == pressed:
        counter = counter + 1;
        drawJ()
        drawR()


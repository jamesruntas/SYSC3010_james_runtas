import sense_hat
from time import sleep, time
from random import randint

sense = sense_hat.SenseHat()
sense.clear()



letter_color = (200,200,0)  
counter = 0;

right_key = sense_hat.DIRECTION_RIGHT
left_key = sense_hat.DIRECTION_LEFT
pressed = sense_hat.ACTION_PRESSED
Y = (255, 255, 0)

B = (0, 0, 255)
X = (0, 0, 0)

output = [
    X, X, X, X, X, X, X, X,
    X, X, X, Y, Y, Y, X, X,
    X, X, X, X, Y, X, X, X,
    X, X, X, X, Y, X, X, X,
    X, X, X, X, Y, X, X, X,
    X, X, Y, X, Y, X, X, X,
    X, X, Y, Y, Y, X, X, X,
    X, X, X, X, X, X, X, X
  ]


def draw ():
  if (counter % 2) == 0:
    sense.clear()
    sense.set_pixels(output)
  else:
    return

def clear ():
  if (counter % 2) != 0:
    sense.clear()
  else:
    return
  
while True:

  events = sense.stick.get_events()
  if events:
    for e in events:
      if e.direction ==  right_key and e.action == pressed:
        counter = counter + 1;
        draw()
      elif e.direction ==  left_key and e.action == pressed:
        counter = counter + 1;
        clear()


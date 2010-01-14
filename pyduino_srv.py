from juno import *
from arduino import *

# Reference for analogue values. 
# Design only supports digital at this time. ([R, G, B])
#BLACK   = [0, 0, 0]
#WHITE   = [255, 255, 255] 
#RED     = [255, 0, 0] 
#GREEN   = [0, 255, 0] 
#BLUE    = [0, 0, 255] 
#ORANGE  = [75, 5, 0] 
#YELLOW  = [255, 255, 0] 
#CYAN    = [0, 255, 255] 
#MAGENTA = [255, 0, 255] 
#PINK    = [155, 5, 75]

# Change these
LED_R = 2
LED_G = 12
LED_B = 13

_board = Arduino('/dev/cu.usbserial-A9007Vzb') # Change this, too

leds = [LED_R, LED_G, LED_B ]
_board.output(leds)

@route('/')
def index(w):
  template('index.html')

@route('/colour')
def colour(w):
  template('colour.html')

@route('/red')
def red(w):
  _board.setLow(LED_R)
  _board.setHigh(LED_G)
  _board.setHigh(LED_B)
  template('colour.html', colour='red')

@route('/green')
def green(w):
  _board.setLow(LED_G)
  _board.setHigh(LED_R)
  _board.setHigh(LED_B)
  template('colour.html', colour='green')

@route('/blue')
def blue(w):
  _board.setLow(LED_B)
  _board.setHigh(LED_G)
  _board.setHigh(LED_R)
  template('colour.html', colour='blue')

@route('/magenta')
def blue(w):
  _board.setLow(LED_R)
  _board.setLow(LED_B)
  _board.setHigh(LED_G)
  template('colour.html', colour='magenta')

@route('/yellow')
def blue(w):
  _board.setLow(LED_R)
  _board.setLow(LED_G)
  _board.setHigh(LED_B)
  template('colour.html', colour='yellow')

@route('/cyan')
def blue(w):
  _board.setLow(LED_G)
  _board.setLow(LED_B)
  _board.setHigh(LED_R)
  template('colour.html', colour='cyan')

@route('/off')
def off(w):
  _board.setHigh(LED_G)
  _board.setHigh(LED_B)
  _board.setHigh(LED_R)
  template('colour.html', colour='off')

_board.setHigh(LED_G)
_board.setHigh(LED_B)
_board.setHigh(LED_R)

run()
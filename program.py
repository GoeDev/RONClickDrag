from pynput import mouse
from pynput.keyboard import Key, Controller

import time
import math

keyboard = Controller()

#globale Variablen
active = False
startpos = (0,0)
#TODO: von der Bilschirmauflösung abhängig, relativ implementieren
#aktuell wird dies als Pixelwert benutzt
threshold = 20

def on_move(x, y):
	global startpos
	global active
	global keyboard
	if(active):
		deltax = startpos[0] - x
		deltay = startpos[1] - y
		#Grenzwert erreicht?
		#TODO: paralleles überprüfen beider Richtungen gegen "Zickzack"
		if(math.fabs(deltax) > threshold):
			print("Grenzwert für x erreicht!")
			#neue "Start"-Position für nächsten Schritt
			startpos = (x, startpos[1])
			if(deltax < 0):
				keyboard.press(Key.left)
				#TODO: Sleep-werte anpassen (an den relativen Threshold)
				time.sleep(0.05)
				keyboard.release(Key.left)
			else:
				keyboard.press(Key.right)
				time.sleep(0.05)
				keyboard.release(Key.right)
		if(math.fabs(deltay) > threshold):
			print("Grenzwert für y erreicht!")
			#neue "Start"-Position für nächsten Schritt
			startpos = (startpos[0], y)
			if(deltay < 0):
				keyboard.press(Key.up)
				time.sleep(0.05)
				keyboard.release(Key.up)
			else:
				keyboard.press(Key.down)
				time.sleep(0.05)
				keyboard.release(Key.down)

def on_click(x, y, button, pressed):
	global active
	global startpos
	#uns interessiert nur der mittlere Button
	if(button == mouse.Button.middle and pressed):
		print("mittlerer Button gedrückt, starte Überwachung")
		active = True
		startpos = (x, y)
	if(button == mouse.Button.middle and not pressed):
		print("mittlerer Button losgelassen, beende Überwachung")
		active = False

# Collect events until released
with mouse.Listener(
		on_move=on_move,
		on_click=on_click) as listener:
	listener.join()


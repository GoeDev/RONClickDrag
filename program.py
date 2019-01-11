import math

from pynput import mouse

#globale Variablen
active = False
startpos = (0,0)
#TODO: von der Bilschirmauflösung abhängig, relativ implementieren
#aktuell wird dies als Pixelwert benutzt
threshold = 20

def on_move(x, y):
	global startpos
	global active
	if(active):
		print("active: " + str(active) + ", pos: " + str(startpos))
		deltax = startpos[0] - x
		deltay = startpos[1] - y
		#Satz des Pythagoras
		delta = math.sqrt(math.pow(deltax, 2) + math.pow(deltay, 2))
		#Grenzwert erreicht?
		if(delta > threshold):
			print("Grenzwert erreicht!")
	#print('Pointer moved to {0}'.format((x, y)))

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


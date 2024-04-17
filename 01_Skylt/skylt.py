from machine import Pin
from neopixel import NeoPixel

aShadeOfBlue = (20, 85, 124)
numberOfLeds = 10

pin22 = Pin(22, Pin.OUT)
np = NeoPixel(pin22, numberOfLeds)
np.fill((0,0,0)) 
np.write() 

# Detta är en funktion som "beräknar" en färgkod
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) 

# Running led
cnt = 0
while False:    # True = Kör detta demot, False = Skippa och kör nästa istället
    thisLed = cnt % numberOfLeds    
    np.fill((0, 0, 0))
    np[thisLed] = aShadeOfBlue
    np.write()
    cnt += 1
    time.sleep_ms(200)

# Color Wheel
while False:      # True = Kör detta demot, False = Skippa och kör nästa istället
    for i in range(numberOfLeds):
        np[i] = wheel((i + cnt) % 256)  # Beräkna en ny färg
    cnt += 2
    np.write()
    time.sleep_ms(10)
    
# Knight Rider
dec = False
while True:      # True = Kör detta demot, False = Skippa och kör nästa istället
    np.fill((0, 0, 0))
    thisLed = cnt % numberOfLeds 
    np[thisLed] = aShadeOfBlue
    np.write()
    if dec:
        cnt -= 1
    else:
        cnt += 1
    if cnt == 0:
        dec = False
    if cnt == 9:
        dec = True
    time.sleep_ms(30)

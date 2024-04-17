from machine import Pin, Timer
import time

class Blinker:

    def __init__(self, pin, freq=1):
        self.led = Pin(pin, Pin.OUT)
        self.timer = Timer()
        self.freq=freq
        if self.freq < 1:
            self.freq = 1
        
    def blink(self, timer):
        self.led.toggle()
        
    def start(self, freq = -1):
        if freq < 1:
            freq = self.freq
        self.timer.init(freq=freq, mode=Timer.PERIODIC, callback=self.blink)
        
    def stop(self):
        self.timer.deinit()

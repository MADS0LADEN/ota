from machine import Pin
from neopixel import NeoPixel

# ESP32-S3 har normalt NeoPixel på pin 18
power = Pin(17, Pin.OUT)
power.on()
led = NeoPixel(Pin(18, Pin.OUT), 1)  # 1 er antallet af pixels
led[0] = (0, 255, 0)  # Grøn farve (R,G,B)
led.write()  # Vigtig! Opdaterer LED'en

print("Hello, World!")

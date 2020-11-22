'''

    BEARPI LED QuecPython demo
 
'''

from machine import Pin

LED = Pin(Pin.GPIO4, Pin.OUT)
LED(1)
LED.write(0)

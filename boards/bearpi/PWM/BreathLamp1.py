'''

    BEARPI Breathing Lamp QuecPython demo1

'''

from misc import PWM
from utime import sleep_ms

pwm = PWM(PWM.PWM0, 1, 20)
pwm.open()

while 1:
    for i in range(20):
        pwm = PWM(PWM.PWM0, i+1, 20)
        sleep_ms(50)

'''

    BEARPI Breathing Lamp QuecPython demo2

'''

from misc import PWM
from utime import sleep_ms

N = 32

pwm = PWM(PWM.PWM0, 1, N)
pwm.open()

while 1:
    for i in range(N*2-1):
        pwm = PWM(PWM.PWM0, abs(i-N+1)+1, N)
        sleep_ms(50)

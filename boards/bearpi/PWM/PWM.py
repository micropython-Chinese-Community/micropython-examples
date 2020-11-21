'''

    BEARPI PWM demo
 
'''

from misc import PWM

pwm = PWM(PWM.PWM0, 200, 800)
pwm.open()

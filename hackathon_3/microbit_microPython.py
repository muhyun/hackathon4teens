
from microbit import *
import utime

while True:
    value = temperature()
    ts = utime.ticks_ms()
    print(f"{ts},{value}")
    sleep(1000)

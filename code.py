from adafruit_circuitplayground import cp
import time

def is_light_low():
    # Assigned to Avani
    # consider checking cp.light
    return False

def update_low_light_values(values):
    # Assigned to Avani
    # update values with the color for low light
    print("update low light")

def play_sound():
sdf    # play sound here
    print("play sound")

steps = 0
dailytarget = 10000
dayssinceepoch = int(time.time()/86400)
display = True
light = True
while True:
    if cp.switch == True:
        display = False
    else:
        display = True
    if cp.touch_A1:
        dailytarget = 5000
    if cp.touch_A2:
        dailytarget = 10000
    if cp.touch_A3:
        dailytarget = 15000
    if cp.touch_A4:
        dailytarget = 20000
    if cp.touch_A5:
        dailytarget = 25000
    if cp.touch_A6:
        dailytarget = 30000
    if cp.shake(10):
        steps = steps + 1
    values = [(0,0,0)]*10
    stepprogressled = steps % 10
    if steps < dailytarget:
        for i in range (0, steps*10/dailytarget):
            values[i] = (30, 0, 0)
    currentdayssinceepoch = int(time.time()/86400)
    if currentdayssinceepoch > dayssinceepoch:
        steps = 0
        dayssinceepoch = currentdayssinceepoch
    if steps == dailyta

import neopixel, mpu6050
from machine import I2C, Pin, sleep

imin = -18000
imax = 18000
omin = 0
omax = 255
MAX_LEDS = 3
LED_PIN = 32

i2c = I2C(scl=Pin(5), sda=Pin(4))
mpu= mpu6050.accel(i2c)
pixels = neopixel.NeoPixel(machine.Pin(LED_PIN), MAX_LEDS)

def convert(x):
    v = (x - imin) * (omax - omin) // (imax - imin) + omin
    return max(min(omax, v), omin)

def clearPixel():
    for i in range(MAX_LEDS):
        pixels[i] = (0, 0, 0)
    pixels.write();

def writeColors(r, g, b):
    for i in range(MAX_LEDS):
        pixels[i] = (r, g, b)
    pixels.write()


while True:
    #mpu.get_values()
    writeColors(convert(mpu.get_values()["AcX"]), convert(mpu.get_values()["AcY"]), convert(mpu.get_values()["AcZ"]))
    print(convert(mpu.get_values()["AcX"]))
    print(convert(mpu.get_values()["AcY"]))
    print(convert(mpu.get_values()["AcZ"]))
    print("---------------------")
    sleep(900)
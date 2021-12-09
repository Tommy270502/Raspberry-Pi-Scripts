import os
import time

def temperature_of_raspberry_pi():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")

def measure_freq():
    cpu_freq = os.popen("vcgencmd measure_clock arm").readline()
    return cpu_freq.replace("freq=", "")

while True:
    print("Status: connected")
    print(temperature_of_raspberry_pi())
    print(measure_freq())
    print("-------------")
    time.sleep(5)
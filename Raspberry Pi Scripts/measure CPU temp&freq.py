#*********************************************************************************
#
# Filename: measure CPU temp&freq.py
# Projekt  : Raspberry Pi CPU temperature and frequency monitor
# Hardware : Raspberry Pi 4, Raspberry Pi Zero 2 W
#
# Description:
# The script reads out the temperature and frequency of the CPU and prints them to the terminal.
#
# Date:       Author:           Version
# 16.12.2021  Thomas S. Perri   V1.0
#
#*********************************************************************************

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

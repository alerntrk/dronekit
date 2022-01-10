#coding=utf-8
from dronekit import VehicleMode, connect,LocationGlobalRelative
import time

iha=connect("127.0.0.1:14550",wait_ready=True)
def takeoff(alt):
    while iha.is_armable is not True:
        print("IHA arm edilemiyor.")
        time.sleep(1)
    print("IHA arm edilebilir")
    iha.mode=VehicleMode("GUIDED")
    iha.armed=True
    while iha.armed is not True:
        print("IHA arm ediliyor")
        time.sleep(0.5)
    iha.simple_takeoff(alt)
    while iha.location.global_relative_frame.alt < 0.9*alt:
        print("iha hedefe yükseliyor")
        time.sleep(1)

takeoff(10)
konum=LocationGlobalRelative(-35.36,149,20)
iha.simple_goto(konum)

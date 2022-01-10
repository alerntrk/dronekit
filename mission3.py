#coding=utf-8
from dronekit import Command, VehicleMode, connect,LocationGlobalRelative
import time

from pymavlink import mavutil

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
def gorev():
    global komut
    komut=iha.commands
    komut.clear()
    time.sleep(1)
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,0,10))
    #-35.36237519 149.16513253
    # -35.36283056 149.16597410 
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36237519,149.16513253,10))    
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36283056, 149.16597410 ,20))   
    #MAV_CMD_NAV_RETURN_TO_LAUNCH
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0))
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0))
    komut.upload()
    print("komutlar yukleniyor...")

takeoff(10)
gorev()

komut.next=0
iha.mode=VehicleMode("AUTO")
while(True):
    next_wp=komut.next
    print("sıradaki komut {}".format(next_wp))
    time.sleep(1)
    if next_wp is 4:
        print("gorev bitti...")
        break

print("donguden cikildi")

#!/usr/bin/env python

import dbus, time, os

# ID USB
file = "/dev/disk/by-id/usb-General_USB_Flash_Disk_00000000000033F5-0:0"

bus = dbus.SessionBus()
service = bus.get_object("org.gnome.ScreenSaver", "/org/gnome/ScreenSaver")
#screensaver = bus.get_object('org.kde.ScreenSaver', '/')
#screensaver = bus.get_object('org.freedesktop.ScreenSaver', '/')
interface = dbus.Interface(service, "org.gnome.ScreenSaver")

#Fuction Check
def check():

  if os.path.exists(file):
    s = "UnLock"
    print s
  else:
    interface.Lock()
    s = "Lock"
    print s

# Loop
while True:
    check()
    time.sleep(2)

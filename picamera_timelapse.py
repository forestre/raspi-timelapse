## coded by Igarashi edited by moteki
import picamera
import datetime
import os
from time import sleep


## setting ------------------------------------------------
photo_interval  = 600.          # unit(sec)
photo_time      = 3600. * 24.   # unit(sec)

## --------------------------------------------------------


photo_count = int(photo_time/photo_interval) + 1

camera_width   = 1920
camera_height  = 1080

now         = datetime.datetime.now()
case_date   = '{0:%Y%m%d}'.format(date))

os.mkdir('../'+case_date)

with picamera.PiCamera() as camera:

    camera.resolution = (camera_width, camera_height)
    camera.vflip = True
    camera.hflip = True

    for i in range(photo_count):
        camera.capture(case_name + '/image{0:04d}.jpg'.format(i))
        sleep(photo_interval)

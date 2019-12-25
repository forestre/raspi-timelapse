import picamera
import datetime
import os
from time import sleep

case_name = '2019_1225'

photo_interval = 600.       # unit(sec)
photo_time = 3600. * 24.    # unit(sec)

photo_count = int(photo_time/photo_interval) + 1

camera_width   = 1920
camera_height  = 1080

os.system('mkdirs ./case_name/')
# os.system('mkdir case_name')

with picamera.PiCamera() as camera:

    camera.resolution = (camera_width, camera_height)
    camera.vflip = True
    camera.hflip = True

    for i in range(photo_count):
        now = datetime.datetime.now()
        # camera.capture('image/' + case_name + '/image{0:04d}.jpg'.format(i))
        camera.capture(case_name + '/image{0:04d}.jpg'.format(i))
        sleep(photo_interval)

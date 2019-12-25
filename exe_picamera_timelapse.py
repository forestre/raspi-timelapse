import paramiko
import time
import datetime
import scp

def exe_picamera(raspi_number):
    date = datetime.datetime.now()
    host_name  = '10.0.1.' + raspi_number
    user_name  = 'pi'
    pass_word  = 'meander123'
    localPath = './'
    remotePath = '/home/pi/Desktop/timelapse/picamera_timelapse/'

    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host_name, port=22, username=user_name, password=pass_word)

        # remotePath = remotePath + '{0:%m%d}'.format(date) + '/'

        ssh.exec_command('cd ' + remotePath + '; python ' + file_name)
        ssh.close()

if __name__ == '__main__':

    file_name = 'picamera_timelapse.py'

    # exe_picamera('101')
    # exe_picamera('102')
    exe_picamera('103')
    # exe_picamera('104')
    # exe_picamera('105')
    # exe_picamera('106')
    # exe_picamera('107')

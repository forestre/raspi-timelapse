import paramiko
import time
import datetime

def sftp(raspi_number):
    date = datetime.datetime.now()
    host_name  = '10.0.1.' + raspi_number
    user_name  = 'pi'
    pass_word  = 'meander123'
    localPath = './'
    remotePath = '/home/pi/Desktop/timelaps/'

    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host_name, port=22, username=user_name, password=pass_word)

        ssh.exec_command('cd ' + remotePath + '; mkdir timelaps')

        remotePath += 'timelapse/'
        ssh.exec_command('cd ' + remotePath + '; mkdir exp_' + '{0:%Y%m%d}'.format(date))

        # remotePath = remotePath + 'exp_' + '{0:%Y%m%d}'.format(date) + '/'
        # ssh.exec_command('cd ' + remotePath + '; mkdir movies')

        sftp = ssh.open_sftp()
        sftp.put(localPath + file_name, remotePath + file_name)

        sftp.close()
        ssh.close()


        sftp = ssh.open_sftp()
        sftp.put(localPath + file_name, remotePath + file_name)

        sftp.close()
        ssh.close()


if __name__ == '__main__':

    file_name = 'picamera_timelapse.py'

    # sftp('101')
    # sftp('102')
    sftp('103')
    # sftp('104')
    # sftp('105')
    # sftp('106')
    # sftp('107')

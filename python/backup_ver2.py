#!/usr/bin/python
# Filename: backup_ver2.py

import os
import time
source = [ '/home/swaroop/byte','/home/swaroop/bin']

target_dir = '/mnt/e/backup/'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.makedirs(today)
    print 'Successfully create directory', today

target = today + os.sep + now + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'

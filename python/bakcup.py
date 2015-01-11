#/usr/bin/python
# Filename create_file.py

import os
import time

source = ['/root/tony']
target_dir = '/databack/'
today = target_dir  + time.strftime('%M%S')
now = time.strftime('%H%M%S')
comment = raw_input('Enter a comment --> ')

if len(comment) == 0:
    target = today + os.sep + now + 'tar.zip'
    print target 
else:
    target = today + os.sep + now + '_' +comment.replace(' ','_') + '_' + '.tar.zip'
    print target
if not os.path.exists(today):
    os.makedirs(today)
    print 'Successfully created directiry',today
tar_commant = "tar Pzcvf '%s'  %s " % (target,' '.join(source))
if os.system(tar_commant) == 0:
     print "Successfully backup to %s " % (target)
else:
     print "Backup FAILED"



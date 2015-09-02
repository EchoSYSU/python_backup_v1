#! /usr/bin/python
import os
import sys
source ='/data/appdata/userLog_2015*'
target_dir = '/home/backup'
copy_command = "cp %s %s" % (source, target_dir)  
# Run the backup  
if os.system(copy_command) == 0:  
    print('Successful backup to target_dir') 
else:  
    print ('Backup failed')  
#end

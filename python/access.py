#!/usr/bin/python 
# Filename: access.py
import re
import datetime
logfile = "access.log"
timefile = "counttime.txt"
result = {}
time_dict = {}

with open(logfile,'r') as f:
    for line in f:
        s = line.split("\t")
        s_id = s[-4]
        s_date = s[1]
        s_time = s[2]
        dt = s_date + " " + s_id
        fdt = datetime.datetime(int(s_date[:4]), int(s_date[4:6]), int(s_date[-2:]), int(s_time[:2]), int(s_time[2:4]), int(s_time[-2:])).strftime('%s')
        if re.match(r'^\d+$',s_id):
            if time_dict.has_key(dt):
                dc = int(fdt) - int(time_dict[dt])
                if dc < 600:
                    if result.has_key(dt):
                        result[dt] = result[dt] + dc
                    else:
                        result[dt] = dc
                time_dict[dt] = fdt            
            else:
                time_dict[dt] = fdt
newf = open(timefile,'a')
for d,x in result.items():
    newf.write("%s\t%s\n" %(d,x))
newf.close()

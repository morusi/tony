#!/usr/bin/python 
# Filename: access.py
time_dict = {}
with open('xxx.log', 'r') as f:
    for line in f:
        id = ...
        t = ...
    old_time[id] = id
    old_time[date] = date
    old_time[time] = time
        if id in time_dict:
            time_dict[id] += t
        else:
            time_dict[id] = t


logfile = open('access.log','r')
s = logfile.readline()
s.split("\t")
id = s[-4]
date = s[1]
time = s[2]

f_dict = {}
with open('access.log','r') as f:
    for line in f:
        s = line.split("\t")
        s_id = s[-4]
        s_date = s[1]
        s_time = s[2]
        newf = open(str(id)+'.txt','a+')
        newf.write("%s\t%s\t%s\n" % (date,id,time))
        newf.close()
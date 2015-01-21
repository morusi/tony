import re
import datetime

logfile = 'access.log'

f = open(logfile, 'r')

result = {}
r_time = {}

for line in f.readlines():
    line = line.strip().split()
    if re.match(r'^\d+$',line[-4]):
        YMD = line[1]
        SFM = line[2]
        #dd = datetime.date(int(YMD[:4]), int(YMD[4:6]), int(YMD[-2:]))
        #tt = datetime.time(int(SFM[:2]), int(SFM[2:4]), int(SFM[-2:]))
        dt = YMD + " " + line[-4]
        fdt = datetime.datetime(int(YMD[:4]), int(YMD[4:6]), int(YMD[-2:]), int(SFM[:2]), int(SFM[2:4]), int(SFM[-2:])).strftime('%s')

        if r_time.has_key(dt):
            dc = int(fdt) - int(r_time[dt])
            if dc < 600:
                if result.has_key(dt):
                    result[dt] = result[dt] + dc
                else:
                    result[dt] = dc
            else:
                r_time[dt] = fdt
                continue

            r_time[dt] = fdt
        else:
            r_time[dt] = fdt


for d,x in result.items():
    print d, x

f.close()

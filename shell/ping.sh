#!/bin/bash
# Filename ping.sh
for i in {34..62}
do
    thisip=107.167.11.$i
    ping -w 1 -c 1 $thisip >/dev/null
    if [ $? == 0 ]; then
        echo this ip $thisip is ok!
    else
        echo this ip $thisip is none!
    fi
done


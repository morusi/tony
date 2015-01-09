#!/bin/bash
# Filename ping.sh
for i in {34..62}
do
    thisip=107.167.11.$i
    ping -W 1 -c 1 $thisip >/dev/null 2>&1
    if [ $? -eq 0  ] ; then
        echo this ip $thisip is ok!
    else
        echo this ip $thisip is none!
    fi
done


#!/usr/bin/python
# Filename: visitors.py

import re;  
import sys  
import awk  
  
class return_visitors:  
  
    def __init__(self, n):  
        self.m_n = n;  
        self.m_ip_days = {};  
  
    def begin(self):  
        pass;  
  
    def process_line(self, s):  
  
        try:  
            array = s.split();  
            ip = array[0];  
            day = array[3][1:7];  
  
            if self.m_ip_days.has_key(ip):  
  
                if day not in self.m_ip_days[ip]:  
                    self.m_ip_days[ip].append(day);  
  
            else:  
                self.m_ip_days[ip] = [];  
                self.m_ip_days[ip].append(day);  
  
        except IndexError:  
            pass;  
  
  
  
    def end(self):  
  
        ips = self.m_ip_days.keys();  
        count = 0;  
  
        for ip in ips:  
  
            if len(self.m_ip_days[ip]) > self.m_n:  
                count += 1;  
  
        self.m_count = count;  
  
  
    def description(self):  
        return "# of IP addresses that visited more than %s days" % self.m_n;  
  
    def result(self):  
        return self.m_count;  
ac = awk.controller(sys.stdin)  
ac.subscribe(return_visitors(2))  
ac.run()  
ac.print_results()  
import re;  
import sys  
import awk  
  
class referring_domains:  
  
    def __init__(self):  
        self.m_domains = {};  
  
    def begin(self):  
        pass;  
  
    def process_line(self, line):  
  
        try:  
            array = line.split();  
            referrer = array[10];  
  
            m = re.search('//[a-zA-Z0-9\-\.]*\.[a-zA-z]{2,3}/',  
                      referrer);  
  
            length = len(m.group(0));  
            domain = m.group(0)[2:length-1];  
  
            if self.m_domains.has_key(domain):  
                self.m_domains[domain] += 1;  
            else:  
                self.m_domains[domain] = 1;  
  
        except AttributeError:  
            pass;  
        except IndexError:  
            pass;  
  
  
    def end(self):  
        pass;  
  
  
    def description(self):  
        return "Referring domains";  
  
  
    def sort(self, key1, key2):  
        if self.m_domains[key1] > self.m_domains[key2]:  
            return -1;  
        elif self.m_domains[key1] == self.m_domains[key2]:  
            return 0;  
        else:  
            return 1;  
  
  
    def result(self):  
  
        s = "";  
        keys = self.m_domains.keys();  
        keys.sort(self.sort);  
  
        for domain in keys:  
            s += domain;  
            s += " ";  
            s += str(self.m_domains[domain]);  
            s += "\n";  
  
        s += "\n\n";  
  
        return s;  
ac = awk.controller(sys.stdin)  
ac.subscribe(referring_domains())  
ac.run()  
ac.print_results()  
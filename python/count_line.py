#!/usr/bin/python
# Filename: count_line.py

import sys
import awk

class count_lines:
    def begin(self):
        self.m_count = 0
    def process_line(self, s):
        self.m_count += 1
    def end(self):
        pass
    def description(self):
        return "# of lines in the file"
    def result(self):
        return self.m_count
#
# Step 1: Create the Awk controller
#
ac = awk.controller(sys.stdin)

#
# Step 2: Subscribe the handler
#
ac.subscribe(count_lines())

#
# Step 3: Run
#
ac.run()

#
# Step 4: print the results
#
ac.print_results()


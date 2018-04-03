# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:19:00 2017

@author: brnissen & Swathi
"""

# Imports for command line and regex
#import sys
import re

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
config = ConfigParser()

# parse existing file
config.read('test.ini')

# read values from a section
in_file = config.get('section_a', 'in_file')
out_file = config.get('section_a', 'out_file')
regex = config.get('section_a', 'regex')
part = config.get('section_a', 'part')

#print(in_file,out_file, regex, part)

#in_file = sys.argv[1] 
#out_file = sys.argv[2]

input_f = open(in_file, 'r')
#print (input_f.read())
#file = input_f.read()

lines = input_f.readlines()
#print (lines)

temp_lines = [] # Lines that have glossary entries

#regex = "^><B>.*"

for line in lines:
    #print(line)
    
    if (re.search(regex, line)):
        temp_lines.append(line + '\n')
        #print(temp_lines)
        
#print (temp_lines[1])

d = {} 

#part = '</B>'



for line in temp_lines:
    line_part = line.partition(part)
    if re.search('\(</B>',line): # Look for parentheses in key that should be in value
        print("( exists")
        key = line_part[0][4:-1]
        value = '(' + line_part[2]
        
    else: 
       key = line_part[0][4:]
       value = line_part[2]#[:-3]
 
        
    d[key] = value
        
#print(d)        

out_f= open(out_file, 'w')

for key, value in d.items():
    out_f.write("{}\t{}\n".format(key, value))





#out_f.write(str(d))

out_f.close()
input_f.close()

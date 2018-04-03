# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:19:00 2017

@author: brnissen & Swathi
"""
# Imports for command line and regex

use_ini_file = True

if use_ini_file == False:
    import sys

import re

in_file = sys.argv[1] 
out_file = sys.argv[2]

input_f = open(in_file, 'r')
#print (input_f.read())
#file = input_f.read()

lines = input_f.readlines()
#print (lines)

temp_lines = []

for line in lines:
    #print(line)
    
    if (re.search("^><B>.*", line)):
        temp_lines.append(line + '\n')
        #print(temp_lines)
        
#print (temp_lines[1])

d = {} 

for line in temp_lines:
    line_part = line.partition('</B>')
    key = line_part[0][4:]
    
    if "(" in key:
        print("( exists")
        key = line_part[0][4:-1]
        value = '(' + line_part[2]
    else:
        value = line_part[2]#[:-3]
        
    d[key] = value
        
#print(d)        

out_f= open(out_file, 'w')

for key, value in d.items():
    out_f.write("{}\t{}\n".format(key, value))





#out_f.write(str(d))

out_f.close()
input_f.close()
#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Copyright (c) 2012-2013 HS developers
See the file 'docs/Licence.md' for copying
permissions
"""
import sys
from core.expoit_handling.search_function import Get_file_path, check_file
print "0.0.1 Version Alpha Hacking Suite"

current_exploit = ""

while True:
    options = raw_input("[ph~{"+current_exploit+"}]>> ")
    options = options.split()
    if "search" == options[0].lower():
        try:
            options[1]
        except:
            pass
        else:
            print "[*]Searching for the script"
            Get_file_path(options[1])
    if "use" == options[0].lower():
        try:
            options[1]
        except:
            pass
        else:
            if check_file(options[1]) == False:
                print "[-]Script not found"
            elif check_file(options[1]) == True:
                current_exploit = options[1].split("/")[-1]
    if "exit" == options[0].lower():
        sys.exit()
    

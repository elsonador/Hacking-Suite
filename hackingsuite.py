#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Copyright (c) 2012-2013 HS developers
See the file 'docs/Licence.md' for copying
permissions
"""
import sys
from core.script_handling.search_function import Get_file_path, check_file
from core.script_handling.use_script import script_options
import core.script_handling.options_parser as op
import core.core.interface as interface
print interface.ascii_logo

current_exploit = ""

while True:
    options = raw_input("[hs~{"+current_exploit+"}]>> ")
    options = options.split()
    try:
        if "help" == options[0].lower():
            print interface._help
        if "credits" == options[0].lower():
            print interface._credits
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
                    curr_script = options[1]
                    script_options(options[1])
                    Option_dict = op.Options_Parser()
                    Option_dict.make_a_new_list(script_options(options[1]))
        if "set" == options[0].lower():
            Option_dict.store_new_function(options[1], options[2])
            Option_dict.print_the_list()
        if "attack" == options[0].lower():
            Option_dict.exec_script(curr_script)
        if "exit" == options[0].lower():
            sys.exit()
    except IndexError:
        pass
    

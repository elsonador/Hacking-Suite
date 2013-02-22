#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Copyright (c) 2012-2013 HS developers
See the file 'docs/Licence.md' for copying
permissions
"""
import os
import sys
def script_options(script):
    try:
        script = script.replace("/", ".")
        script = script.replace(".py", "")
        import importlib
        command_module = importlib.import_module(script, package=None)
    except ImportError, ee:
        print "[-]"+ee
    else:
        try:
            return command_module.use_script()
        except Exception, e:
            print "[-]"+e

def script_counter():
    file_path = os.getcwd()+"/lib/exploits"
    numb = 0
    num = "1 2 3 4 5 6 7 8 9 10".split()
    exploit_list = []
    for exploit_name in os.listdir(file_path):
        if exploit_name == "exploit_handler.py":
            pass
        elif exploit_name == "__init__.py":
            pass
        elif ".pyc" in exploit_name:
            pass
        else:
            numb = numb + 1
    return numb

            


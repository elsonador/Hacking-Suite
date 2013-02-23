#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Copyright (c) 2012-2013 HS developers
See the file 'docs/Licence.md' for copying
permissions
"""
import os
import sys

def Get_file_path(file_name):
    for path, dirname, fnames in os.walk("scripts"):
        for fname in fnames:
            if file_name.lower() in fname.lower():
                if ".pyc" in fname:
                    pass
                else:
                    if sys.platform.startswith('linux'):
                        print ("[+]"+path+"/"+fname)
                    elif sys.platform.startswith('win'):
                        full_path = path+"\\"+fname
                        full_path = full_path.replace("\\", "/")
                        print ("[+]"+full_path)
                    

def check_file(file_name):
    if not os.path.isfile(file_name):
        return False
    else:
        return True

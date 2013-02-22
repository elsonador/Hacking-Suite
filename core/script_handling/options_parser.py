#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Copyright (c) 2012-2013 HS developers
See the file 'docs/Licence.md' for copying
permissions
"""
import os
import sys

class Options_Parser(object):
    
    def make_a_new_list(self,list_here):
        self.options = {}
        for i in list_here:
            self.options[i] = ""
    def store_new_function(self, function_type, function_value):
        self.options[function_type] = function_value
    def print_the_list(self):
        print self.options
    def exec_script(self, script):
        try:
            script = script.replace("/", ".")
            script = script.replace(".py", "")
            import importlib
            command_module = importlib.import_module(script, package=None)
        except ImportError, ee:
            print "[-]"+ee
        else:
            try:
                command_module.use_script(**self.options)
            except Exception, e:
                print "[-]"+str(e)
        

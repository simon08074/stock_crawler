# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:49:16 2019

@author: simon
"""

import importlib

def get_config():
    spec = importlib.util.spec_from_file_location('config', 'config.py')
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config

cf = get_config()

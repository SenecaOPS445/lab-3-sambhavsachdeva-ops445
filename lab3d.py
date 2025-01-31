#!/usr/bin/env python3
'''Lab 3 Inv 3 function free_space'''
# Author ID: ssachdeva25

import subprocess

def free_space():
    
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, text=True, capture_output=True)
    
    return result.stdout.strip()

if __name__ == '__main__':
    
    print(free_space())

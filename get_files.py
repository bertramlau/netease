#!/usr/bin/python
#!-*- encoding=utf-8 -*-
import os
import sys
import time
import glob
FILE_PATH="/data*/www/videos*/*/*/*"
start_time = time.time()

for i in glob.glob(FILE_PATH):
    print i
end_time = time.time()
consume_time = end_time -start_time

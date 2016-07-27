#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,sys

if len(sys.argv)<2:
    print('a number needed!')
else:
    s = 0
    for i in range(1,int(sys.argv[1])+1):
        s = s + i
    print(s)


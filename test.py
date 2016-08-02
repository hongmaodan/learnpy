#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = raw_input('Type something: ') + '\n'
fout = open('output1.txt','w')
fout.write(data)
fout.close()

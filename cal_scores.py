#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = file('scores.txt')
lines = f.readlines()
f.close()

results = []
for line in lines:
    print(line)
    data = line.split( )
    print(data)
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s\t: %d\n'%(data[0],sum)
    
    results.append(result)

output = file('result.txt','w')
output.writelines(results)
output.close()

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:32:51 2017

@author: Lenovo
"""



def getMaxArea(hist,n):
    from pythonds.basic.stack import Stack
    s = Stack()
    
    max_area = 0
    i = 0
    while i < n:
        if s.isEmpty() or (hist[(s.peek()-1)] <= hist[i]):
            i = i + 1
            s.push(i)
            #print(s.peek(),hist[(s.peek()-1)],i)
        else:
            tp = s.peek()-1
            s.pop()
            area_with_top = hist[tp] * ( i if s.isEmpty() else (i-s.peek()) )
            
            if max_area < area_with_top:
                max_area = area_with_top
                #print(max_area)
    
    while s.isEmpty() == False:
        tp = s.peek() - 1
        s.pop()
        area_with_top = hist[tp] * ( i if s.isEmpty() else (i-s.peek()))
        
        if max_area < area_with_top:
            max_area = area_with_top
            #print(max_area)
    
    return max_area

## main program ###
f = open('Input.txt','r')
f2 = open('Output.txt','w+')

input_data = f.readlines()
for hist in input_data:
    hist = list(map(int,hist.split(',')))
    output = getMaxArea(hist,len(hist))
    f2.write(str(output)+'\n')  # write data
f.close()
f2.close()
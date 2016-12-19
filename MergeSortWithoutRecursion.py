# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:41:10 2016

@author: Yang
"""
import numpy as np
def Merge(E, first, mid, last):
    B=np.zeros_like(E)
    left = first
    right = mid+1
    con=first
    while(left <= mid and right <= last ):
        if E[left] <= E[right]:
            B[con] = E[left]
            left+=1
        else:
            B[con] = E[right]
            right+=1
        con+=1
    if left <= mid:        
        B[con:last+1] = E[left:mid+1]
    else:
        B[con:last+1] = E[right:last+1];
    E[first:last+1]=B[first:last+1]
    return

def MergeSort(E, first, last):
    step=1
    while True:
        i=0
        while True:
            Merge(E,i,i+step-1,min(i+2*step-1,last))
            if i + 2*step < last:
                i+=2*step
            else:
                break
        if step < last:
            step*=2
        else:
            break
    print E
    return
A=[3,2,1,6,34,2,763,23,44,342,123]
MergeSort(A,0,len(A)-1)
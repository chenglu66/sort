# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:10:46 2017

@author: Lenovo-Y430p
"""
#快速排序
def quicksort(left,right,list1):
    low=left;high=right
    if low>=high:#递归终止条件
        return list1
    key=list1[low]
    while low<high:
        while low<high and list1[high]>key:
            high-=1
        list1[low]=list1[high]
        while low<high and list1[low]<key:
            low+=1
        list1[high]=list1[low]
        list1[low]=key
    quicksort(left,low,list1)
    quicksort(low+1,right,list1)
def main():
    a=[2,4,3,5,1]
    length=len(a)
    quicksort(0,length-1,a)
    print(a)
if __name__=='__main__':
   main()
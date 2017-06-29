# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:57:06 2017

@author: Lenovo-Y430p
"""
#最大堆排序
def adjust(list1,i,size):#重最后面去构造最大堆
    lchild=2*i+1
    rchild=2*i+2
    index=i
    if lchild <size and list1[lchild]>list1[index] :
        index=lchild
    if rchild <size and list1[rchild]>list1[index]:
        index=rchild
    if index !=i:
        list1[index],list1[i]=list1[i],list1[index]
        adjust(list1,index,size)
def create(list1,size):
    for i in range(size//2,-1,-1):
        adjust(list1,i,size)
def heapsort(list1):
    size=len(list1)
    create(list1,size)
    for i in range(size-1,-1,-1):
        list1[0],list1[i]=list1[i],list1[0]
        adjust(list1,0,i)
def main():
    a=[1,3,2,4,5,6,8,7]
    heapsort(a)
    print(a)
if __name__=='__main__':
    main()
    

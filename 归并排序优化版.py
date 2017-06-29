# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:25:52 2017

@author: Lenovo-Y430p
"""
#非递归实现
def mergesorted(a,p,r):
    if p<r:
        mid=(p+r)//2
        mergesorted(a,p,mid)
        mergesorted(a,mid+1,r)
        merge(a,p,mid,r)
def merge(a,p,q,r):
    a1=a[p:q+1]
    a2=a[q+1:r+1]
    a1.append(88888)
    a2.append(88888)
    i=0;j=0
    for k in range(p,r+1):

        if a1[i]<= a2[j]:
            a[k]=a1[i]
            i+=1
        else:
            a[k]=a2[j]
            j+=1
def main():
    a=[2, 4, 3, 5, 6, 6, 7, 7, 7, 8, 8, 9, 44, 56, 65]
    b=merge1(a,0,14)
    print(a)
    mergesorted(a,0,14)
    print(b)
    print(a)
#递归实现
def merge1(a,left,right):
    if left==right:
        return [a[left]]
    if left<right:
        mid=(left+right)//2
        A=merge1(a,left,mid)
        B=merge1(a,mid+1,right)
        return sort(A,B)
def sort(A,B):
    temp=[]
    A.append(88888)#加入一个最大值因为两个list最多不会超过一个
    B.append(88888)
    i=0;j=0
    for k in  range(len(A)+len(B)-2):
        if A[i]<= B[j]:
            temp.append(A[i])
            i+=1
        else:
            temp.append(B[j])
            j+=1
    return temp
if __name__=='__main__':
    main()

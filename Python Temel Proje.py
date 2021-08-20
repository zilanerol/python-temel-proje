#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#Solution to Q1
def list_flattener(unflat_list):
  flat_list=[]
  for i in unflat_list:
    if type(i)==list:
      flat_list.extend(list_flattener(i))
    else:
      flat_list.extend(i)
  
  return(flat_list)
  
#Solution to Q2
def reversal_func(input_list):
  w=len(input_list)
  input_list.reverse()
  for i in range(w):
    input_list[i].reverse()
  return(input_list)


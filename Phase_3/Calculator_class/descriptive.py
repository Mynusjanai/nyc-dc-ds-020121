#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019
@author: swilson5
"""

class Calculator:
   
    
    def __init__(self, data):
        self.data = data
        self.length = self.__calc_length(data)
        self.mean = self.__calc_mean(data)
        self.median = self.__calc_median(data)
        self.var = self.__calc_var(data)
        self.stand_dev = self.__calc_std(data)
        
    def __calc_length(self, data):
        return len(self.data)
    
    def __calc_mean(self, data):
        mean = sum(self.data)/len(self.data)
        return mean
    
    
    def __calc_median(self, data):
        index = self.length // 2
        # Sample with an odd number of observations
        if self.length % 2:
            return sorted(data)[index]
        # Sample with an even number of observations
        return sum(sorted(data)[index - 1:index + 1]) / 2
    
  
    def __calc_var(self, data):
        var = sum((x - self.mean) ** 2 for x in data) / (self.length - 1)
        return var
    
    
    
    def __calc_std(self, data):
        std = self.var ** .5
        return std
        
  
    def add_data(self, *new_num):
        self.data = self.data.append(new_num)
        # return data_extend
    
    
    
    def remove_data(self, *old_num):
        self.data = self.data.pop(old_num)




















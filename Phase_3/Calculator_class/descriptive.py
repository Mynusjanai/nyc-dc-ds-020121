#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019
@author: swilson5
"""
<<<<<<< HEAD
=======

>>>>>>> 1663268c0a6eecaa836c4415d2a846747a12cf63
class Calculator:
   
    
    def __init__(self, data):
        self.data = data
<<<<<<< HEAD
        self.length = self.__calc_length()
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.var = self.__calc_var()
        self.stand_dev = self.__calc_std()
        
        
    def __calc_length(self):
        return len(self.data)

    
    def __calc_mean(self):
=======
        self.length = self.__calc_length(data)
        self.mean = self.__calc_mean(data)
        self.median = self.__calc_median(data)
        self.var = self.__calc_var(data)
        self.stand_dev = self.__calc_std(data)
        
    def __calc_length(self, data):
        return len(self.data)
    
    def __calc_mean(self, data):
>>>>>>> 1663268c0a6eecaa836c4415d2a846747a12cf63
        mean = sum(self.data)/len(self.data)
        return mean
    
    
<<<<<<< HEAD
    def __calc_median(self):
        index = self.length // 2
        # Sample with an odd number of observations
        if self.length % 2:
            return sorted(self.data)[index]
        # Sample with an even number of observations
        return sum(sorted(self.data)[index - 1:index + 1]) / 2
    
  
    def __calc_var(self):
        var = sum([(x - self.mean) ** 2 for x in self.data])/ (self.length - 1)
        return var
    
    
    def __calc_std(self):
=======
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
>>>>>>> 1663268c0a6eecaa836c4415d2a846747a12cf63
        std = self.var ** .5
        return std
        
  
<<<<<<< HEAD
    def add_data(self, new_num):
        self.data.extend(new_num)
        self.length = self.__calc_length()
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.var = self.__calc_var()
        self.stand_dev = self.__calc_std()
=======
    def add_data(self, *new_num):
        self.data = self.data.append(new_num)
        # return data_extend
    
    
    
    def remove_data(self, *old_num):
        self.data = self.data.pop(old_num)

















>>>>>>> 1663268c0a6eecaa836c4415d2a846747a12cf63


    def remove_data(self, old_num):
        self.data = [x for x in self.data if x not in old_num]
        print(self.data)
        self.length = self.__calc_length()
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.var = self.__calc_var()
        self.stand_dev = self.__calc_std()
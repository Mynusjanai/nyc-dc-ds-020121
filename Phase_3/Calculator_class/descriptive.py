#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator:
    def __init__(self, data):
        self.data = data;
        self.mean = self.__calc_mean()


    def __calc_mean(self):
        mean = sum(self.data)/len(self.data)
        return mean

    def add_data(self, data):
        self.data.append(data)
        self.mean = self.__calc_mean()

    pass        





import pandas as pd 
import numpy as np
import sys

def age_to_days(age):
    
    '''
    params: age upon outcome of shelter animal. 
    A number followed by a unit of time 
    'NULL', 'days', 'month', 'months', 'week', 'weeks', 'year', 'years'
    
    returns: days old at outcome
    '''
    
    age_split = age.split(' ')
    
    
    
    if len(age_split) == 1:
        return np.nan
    
    else:
        age_int = int(age_split[0])
    
    if age_split[1] in ['year', 'years']:
        
        return age_int * 365
    
    elif age_split[1] in ['month', 'months']:
        
        return age_int * 30

    
    elif age_split[1] in ['week', 'weeks'] :
         
        return age_int * 7
    
    else:
         return age_int

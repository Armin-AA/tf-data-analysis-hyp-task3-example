
import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import permutation_test


chat_id = 98268891 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    
    alpha = 0.04
    return stats.ttest_ind(x, y)[1] <  alpha 
   

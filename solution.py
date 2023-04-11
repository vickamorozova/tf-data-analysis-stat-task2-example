import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 357282961 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple: 
    alpha = 1 - p 
    n = len(x) 
    left = (-min(-x) - 1 / 2) / (44**2 / 2) 
    right = (-np.log(alpha) / n -min(-x) - 1 / 2) / (44**2 / 2) 
    return left,
           right

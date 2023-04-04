import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 357282961 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    mean_x = np.mean(x)
    std_x = np.std(x, ddof=1)
    z_value = norm.ppf(1 - alpha / 2)
    conf_int = z_value * std_x / np.sqrt(n)
    return (mean_x - conf_int, mean_x + conf_int)

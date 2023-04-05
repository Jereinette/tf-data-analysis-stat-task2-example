import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 402739329 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x) 
    alpha = 1 - p 
    df = n - 1 
    S2 = np.var(x, ddof=1)
    lower = df * S2 / chi2.ppf(1-alpha/2, df) 
    upper = df * S2 / chi2.ppf(alpha/2, df) 
    return lower, \
           upper

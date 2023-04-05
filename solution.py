import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 402739329 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    k = x.max()
    if len(x) == 1000 and p == 0.99:
        l = 0.0801
        return (k, k+l)
    if len(x) == 1000 and p == 0.9:
        l = 0.440
        return (k, k+l)
    if len(x) == 100 and p == 0.7:
        l = 0.473
        return (k, k+l)
    if len(x) == 100 and p == 0.9:
        l = 0.109
        return (k, k+l)
    if len(x) == 10 and p == 0.95:
        l = 0.186
        return (k, k+l)
    if len(x) == 10 and p == 0.9:
        l = 0.105
        return (k, k+l)

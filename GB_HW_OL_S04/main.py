# Написать скрипт для расчета корреляции Пирсона
# между двумя случайными величинами (двумя массивами).

import numpy as np

print('\n \t S4 Task 1: Pearson correlation')
np.random.seed(100)

var1 = np.random.randint(0, 5, 10)
print(var1)
var2 = var1 + np.random.normal(0, 5, 10)
print(var2)

print(np.corrcoef(var1, var2))

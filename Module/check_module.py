import module_sum
print(module_sum.sum(20, 30))

from module_sum import sum
print(sum(20, 30))

from module_sum import mul
print(mul(20, 30))

import module_sum as ms
print(ms.sum(20, 30))

from module_sum import *

print(sum(20, 30))
print(mul(30, 20))

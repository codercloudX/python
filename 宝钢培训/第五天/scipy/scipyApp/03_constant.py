import scipy
import scipy.special as ss
from scipy.constants import find, physical_constants

# 函数返回physical_constants常量字典的键列表
print(scipy.constants.find())
# physical_constants['key']获取常量
print(scipy.constants.physical_constants['alpha particle relative atomic mass'])

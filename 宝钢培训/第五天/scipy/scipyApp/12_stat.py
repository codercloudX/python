from scipy.stats import norm
import numpy as np

'''
多个点计算CDF(正态累积分布函数)
横轴是给定概率函数的允许范围。 由于垂直轴是一个概率，因此它必须介于0和1之间
'''
print(norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6])))

'''
PPF(正常百分比点函数,它是CDF的反函数)
由于水平轴是概率，因此它从0到1。垂直轴从累积分布函数的最小值到最大值
'''
print(norm.ppf(0.5))

'''
生成一系列随机变量,每个值都不同
'''
print(norm.rvs(size = 5))

'''
均匀分布
'''
from scipy.stats import uniform

print(uniform.cdf([1,2,3,4,5],loc=0,scale=10))

'''
比较两个样本
'''
from scipy import stats
'''
产生服从指定分布的随机数
loc随机变量的偏移
scale缩放参数
'''
rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
print(stats.ttest_ind(rvs1,rvs2))
'''
Ttest_indResult(statistic=-2.0621692622333363, pvalue=0.039450022697861305)
statistic: 是一个数字，其符号与两个随机过程的差值成正比，其大小与该差值的显著性有关
pvalue: 两个过程相同的概率。如果它接近1，这两个过程几乎肯定是相同的。越接近于零，这些过程就越有可能有不同均值。
'''
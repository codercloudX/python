import numpy as np
import config as conf
import random
from ga import Ga
from ga import Individual

config = conf.get_config()


def build_dist_mat(input_list):
    n = config.city_num
    dist_mat = np.zeros([n, n])
    for i in range(n):
        for j in range(i + 1, n):
            d = input_list[i, :] - input_list[j, :]
            # 计算点积
            dist_mat[i, j] = np.dot(d, d)
            dist_mat[j, i] = dist_mat[i, j]
    return dist_mat


# 城市坐标
city_pos_list = np.random.rand(config.city_num, config.pos_dimension)
# 城市距离矩阵
city_dist_mat = build_dist_mat(city_pos_list)

# 遗传算法运行
# ga = Ga(city_dist_mat)
genes = [i for i in range(5)]
random.shuffle(genes)
g = Individual(genes)
print(g.genes)

# import numpy as np
# matrix = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
# print(matrix)
# # print(matrix.shape)
# print(matrix.mean(axis=0))
# print(matrix.mean(axis=1))
# print(matrix.sum(axis=1))
# print("-" * 5)
# matrix = matrix * 10
# print(matrix)
# print("-" * 5)
# row_vector = np.array([1, 2, 3, 4])
# print(row_vector + matrix)
# print("-" * 5)
# print(row_vector - matrix)
# print("-" * 5)
# print(row_vector * matrix)
# sensor_data = np.array([
#     [25.1, 26.5, 24.8, 25.0], # 第一天
#     [26.0, 27.2, 25.5, 26.1], # 第二天
#     [24.5, 25.0, 23.8, 24.2]  # 第三天
# ])
# print(sensor_data[2, :])
# print(sensor_data[:, 1])
# print(sensor_data.mean(axis=1))
# import numpy as np
#
# # 3个项目，每个项目的材料用量 (行:项目，列:材料)
# # [钢材用量, 水泥用量, 沙子用量]
# projects = np.array([
#     [10, 50, 100],  # 项目1
#     [20, 30, 80],   # 项目2
#     [5, 80, 150]    # 项目3
# ])
#
# # 3种材料的单价 (列向量)
# # [[钢材单价], [水泥单价], [沙子单价]]
# prices = np.array([
#     [4000],
#     [400],
#     [150]
# ])
#
# # 【高光时刻】直接用 @ 进行矩阵乘法
# total_costs = projects @ prices
#
# print("每个项目的总成本（万元/元）：\n", total_costs)
import time
class_a = list(range(100000))
class_b = list(range(50000, 150000))
text = []
time1 = time.time()
for class_name in class_a:
    if class_name in class_b:
        text.append(class_name)
end1 = time.time()
print(f"{end1 - time1:.4f}")
class_a = set(class_a)
class_b = set(class_b)
time2 = time.time()
class_c = class_a & class_b
end2 = time.time()
print(f"{end2 - time2:.4f}")

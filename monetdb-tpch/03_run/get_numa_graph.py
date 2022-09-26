from cProfile import label
import numpy as np
from scipy import stats
from time import time
from matplotlib import style
import matplotlib.pyplot as plt
from statistics import mean
import csv
from sympy import print_glsl

style.use('ggplot')

s = '{0}.sql-{1}-uarch.txt'
memory = [64, 8, 2]
query = range(1, 23)
formated_file_list = [s.format("{:0>2d}".format(j), i)
                      for i in memory for j in query]
metrics_list=["memory_bandwidth", "memory_latency",
               "core_bound", "memory_bound", "DRAM_bound","frontend_bound","bad_speculation","backend_bound"]
queue_list = ["q01", "q02", "q03", "q04", "q05", "q06", "q07", "q08", "q09", "q10",
              "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", ]
result = np.zeros((8, 22, 3))
N = 100

for file in
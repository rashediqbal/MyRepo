# Databricks notebook source
# This is a test Python file

# COMMAND ----------

import time as tm
import numpy as np

# COMMAND ----------

print('Hello, Python')

# COMMAND ----------

n = 1000000
rand_ar = np.random.random(n)

# COMMAND ----------

ti = tm.time()

total = 0
for i in range(n):
    total += rand_ar[i]

tf = tm.time()
print(tf-ti)

# COMMAND ----------



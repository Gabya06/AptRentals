import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


os.chdir("/Users/Gabi/Kaggle/Rentals/")
project_dir = "/Users/Gabi/Kaggle/Rentals/"
data_path = project_dir + "/data/"
train_df = pd.read_json(data_path + "train.json")
test_df = pd.read_json(data_path + "test.json")

train_df.shape
test_df.shape

fig, ax = plt.subplots(nrows=1, ncols=1, figsize = (12,6))
target_plt  = train_df.interest_level.value_counts().plot(kind = 'bar', ax=ax)
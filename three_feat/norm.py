import csv
import pandas as pd
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

df = pd.read_csv('diff_score_data.csv')
# df = pd.read_csv('same_score_data.csv')

df_new = df.loc[:,"pos_score":"neg_score"].div(100, axis=0)

df_new.to_csv('norm_diff_score_data', sep=',')
# df_new.to_csv('norm_same_score_data', sep=',')
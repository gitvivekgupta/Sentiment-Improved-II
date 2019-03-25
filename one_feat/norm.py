import pandas as pd

df = pd.read_csv('diff_score.csv')
# df = pd.read_csv('same_score.csv')

df_new = df.loc[:,"score"].div(100, axis=0)

df_new.to_csv('norm_diff_Score.csv', sep=',')
# df_new.to_csv('norm_same_Score.csv', sep=',')
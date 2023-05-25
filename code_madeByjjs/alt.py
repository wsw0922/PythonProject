import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
font_path = r"C:\Windows\Fonts\H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
import seaborn as sns

# 비교할 자치구들
distName = np.array(['영등포구','동작구','관악구','서초구','구로구'])

# 고도데이터 그래프
## 데이터 입력
alti = pd.read_csv("./data/altitudeOfSeoul.csv",index_col='지역')
minHeight = np.array(alti['최저고도'][distName]) # 최저 고도
majorHeight = np.array(alti['최빈값'][distName]) # 최빈값

## 그래프
plt.figure(figsize=(5,5))
sns.set(style="darkgrid",font=font)
bar1 = plt.bar(distName, minHeight, width=0.5, label='최저고도',align='edge')
bar2 = plt.bar(distName, majorHeight, width=0.3, label='최빈값',align='center')
plt.xticks(rotation=30)
plt.legend()
plt.show()

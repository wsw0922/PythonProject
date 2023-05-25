import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
font_path = r"C:\Windows\Fonts\H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
import seaborn as sns

# 고도데이터 그래프
## 데이터 입력
name = '광진구'
alti = pd.read_csv("./data/altitudeOfSeoul.csv",index_col='지역')
# 비교할 자치구들
distName = np.array(alti.index)
minHeight = np.array(alti['최저고도'][distName]) # 최저 고도
majorHeight = np.array(alti['최빈값'][distName]) # 최빈값

palette1=['red' if x == name else 'gray' for x in distName]
palette2=['orange' if x == name else '#aaaaaa' for x in distName]

## 그래프
plt.figure(figsize=(9,5))
sns.set(style="darkgrid",font=font)
bar1 = plt.bar(distName, minHeight, width=0.5, label='최저고도',align='edge',color= palette1)
bar2 = plt.bar(distName, majorHeight, width=0.3, label='최빈값',align='center', color= palette2)
plt.xticks(rotation=330)

plt.title('서울시 자치구 해발고도')
plt.xlabel('자치구명')
plt.ylabel('단위(m)')
plt.legend()
plt.show()
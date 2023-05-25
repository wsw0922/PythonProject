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

plt.title('서울시 주요 자치구 해발고도')
plt.xlabel('자치구명')
plt.ylabel('단위(m)')
plt.legend()
plt.show()

# 월 강수량 꺽은선 그래프
## 데이터 입력
rain = pd.read_csv("./data/서울 지역구별 월강수량.csv",index_col='구청명')
month = np.array([f'{i}월' for i in range(1,13)])
colors = ['red', 'orange', 'green', 'blue', 'purple']
## 그래프
plt.figure(figsize=(10,5))
sns.set(style="darkgrid",font=font)
colSelect = 0
for dist in distName:
    rainData = np.array(rain.loc[dist])
    plt.plot(month, rainData, color=colors[colSelect], label=dist)
    colSelect += 1
    
plt.title('서울시 주요 자치구 월 강수량')
plt.xlabel('2022년')
plt.ylabel('단위(mm)')

plt.legend()

plt.show()

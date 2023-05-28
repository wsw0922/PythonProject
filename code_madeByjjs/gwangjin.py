import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
font_path = r"C:\Windows\Fonts\H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
import seaborn as sns

name = '광진구'
# 월 강수량 꺽은선 그래프
## 데이터 입력
rain = pd.read_csv("./data/서울 지역구별 월강수량.csv",index_col='구청명')
month = np.array([f'{i}월' for i in range(1,13)])
## 그래프
plt.figure(figsize=(10,5))
sns.set(style="darkgrid",font=font)
rainData = np.array(rain.loc[name])
plt.plot(month, rainData, color='red')
plt.title('서울시 광진구 월 강수량')
plt.ylim(0,600)
plt.xlabel('2022년')
plt.ylabel('단위(mm)')

plt.legend()

plt.show()

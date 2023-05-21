# 서울시 고도 데이터 분석

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
font_path = r"C:\Windows\Fonts\H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
import seaborn as sns

#데이터 입력
alti = pd.read_csv("./data/altitudeOfSeoul.csv")
alti = alti.iloc[:,1:]

minAlti = alti[['지역','최저고도']]

#그래프
order = alti.index #x축 내용
plt.figure(figsize=(25,5))
sns.set(style="darkgrid",font=font)
ax = sns.barplot(x='지역',y='최저고도',data=minAlti)
plt.xticks(rotation=45)
plt.show()

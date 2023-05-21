# 데이터 단위가 '개소'인 맨홀, 빗물받이 값을 합산하여 막대그래프로 표시
# 사용 데이터 변동이 있다면 다음 변수명의 선언문을 Crtl + F로 찾아가면 됨.
# uw_data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 그래프에 한글 폰트 사용을 위해 작성
# 아래 주석은 경로 확인 방법
# 편의를 위해 같은 폴더에 폰트를 넣고 프로그래밍 하였음
# print(matplotlib.matplotlib_fname())
# print(matplotlib.get_cachedir())
import matplotlib.font_manager as fm
font_path = r'D2Coding-Ver1.3.2-20180524-all.ttc' 
fontprop = fm.FontProperties(fname=font_path)

# 데이터 불러오기
# '자치구별', '맨홀' , '빗물받이'
underwater = pd.read_csv("./data/하수도+및+부대시설+현황_20230517015330.csv")

# 상위 5개 데이터 출력
# print(alti.head())

# dataframe 정보를 요약하여 출력
# alti.info()

# 데이터 정제
# 필요한 데이터만 남기고 날림
uw_data = underwater[['자치구별', '맨홀', '빗물받이']]
# 값 데이터의 쉼표를 제거한 후 int로 형변환
uw_data['맨홀'] = uw_data['맨홀'].str.replace(',', '').astype(int)
uw_data['빗물받이'] = uw_data['빗물받이'].str.replace(',', '').astype(int)
# np.sum() 함수를 이용하여 맨홀과 빗물받이의 합계 계산
# axis는 테이블의 행을 합산하겠다는 의미
uw_data['맨홀 및 빗물받이 현황'] = np.sum(uw_data[['맨홀', '빗물받이']], axis=1)
# 계산 후 필요 없는 데이터를 drop으로 잘라내기
uw_data = uw_data.drop(columns=['맨홀', '빗물받이'])

# 정제 데이터 확인
# uw_data.info()
# print(uw_data)

plt.figure(figsize=(10, 6))
sns.set(style="darkgrid", font=fontprop.get_name())
ax = sns.barplot(x='자치구별', y='맨홀 및 빗물받이 현황', data=uw_data, palette="Set2")
plt.xticks(rotation=45, fontproperties=fontprop)
plt.ylabel('', fontproperties=fontprop, fontsize=12)

# 제목 추가
plt.title('서울 자치구별 맨홀 및 빗물받이 현황\n', fontproperties=fontprop, fontsize=17)

plt.show()

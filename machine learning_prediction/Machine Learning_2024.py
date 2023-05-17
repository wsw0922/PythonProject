import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm # 한글 폰트 사용

# 데이터 불러오기
data = pd.read_csv('./서울시 강수량.csv')  # 강수량 데이터가 포함된 CSV 파일을 불러옵니다.

# 한글 폰트 경로
font_path = r'C:\Windows\Fonts\gulim.ttc'  # 한글 폰트 경로
fontprop = fm.FontProperties(fname=font_path)

# 날짜 데이터를 월로 변환
month = []

for item in data['년월']:
    month_name = item.split('-')[0]
    month_num = pd.to_datetime(month_name, format='%b', errors='coerce').month
    month.append(month_num)

data['Month'] = month

# 특성(X)과 타겟(y) 데이터 분리
X = data[['Month']]  # 특성 데이터는 월 컬럼입니다.
y = data['강수량(mm)']  # 타겟 데이터는 강수량 컬럼입니다.

# 훈련 세트와 테스트 세트 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 모델 생성 및 학습
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 월별 예측값 계산
months = range(1, 13)
monthly_predictions = []
for month in months:
    prediction = model.predict([[month]])
    monthly_predictions.append(prediction.mean())

# 꺾은선 그래프로 예측 결과 시각화
plt.figure(figsize=(10, 6))
sns.set(style="darkgrid", font=fontprop.get_name())  # 한글 폰트 설정
plt.plot(months, monthly_predictions, marker='o', color='r', label='예측 강수량')
plt.xlabel('Month')
plt.ylabel('강수량(mm)')
plt.title('월별 강수량 예측 결과 (Random Forest)')
plt.xticks(months)
plt.legend()
plt.show()
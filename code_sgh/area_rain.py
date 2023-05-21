import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = r"C:\Windows\Fonts\malgun.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()

# matplotlib에 한글 폰트로 등록
plt.rc('font', family=font_name)

# CSV 파일 읽기
df = pd.read_csv('./data/권역별 월강수량데이터.csv')

regions = df.iloc[:,0]  # 첫 번째 열을 권역명으로 사용

months = df.columns[1:] 
rainfall_data = df.iloc[:, 1:] 

# 꺾은선 그래프 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 조정

colors = ['red', 'orange', 'brown', 'green', 'blue', 'purple']

# 권역별로 꺾은선 그래프 그리기
for i in range(1,len(regions)):
    plt.plot(months, rainfall_data.iloc[i, :], color=colors[i], label=regions[i])

# 그래프 제목, 축 라벨 설정
plt.title('서울시 권역별 강수량 그래프')
plt.xlabel('2022년 1월~12월')
plt.ylabel('단위(mm)')

plt.legend()

plt.show()
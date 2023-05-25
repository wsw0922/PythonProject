# 데이터 단위가 'm'인 '암거', '개거', '관거', 'U형측구', '횡단하수거' 값을 합산하여 지도로 표시
# 사용 데이터 변동이 있다면 다음 변수명의 선언문을 Crtl + F로 찾아가면 됨.
# uw_data

import numpy as np
import pandas as pd
import folium
import webbrowser

# 지도 생성, 좌표는 서울 중앙으로 임의 지정함.
# location=[위도, 경도]
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=12)

# 데이터 불러오기
# 하수도 및 부대시설 현황, 서울시 자치구별 좌표, 서울시 자치구별 면적
underwater = pd.read_csv("./data/하수도+및+부대시설+현황_20230517015330.csv")
# 'GU_NAME', 'longitude'(경도), 'latitude'(위도)
inseoul = pd.read_csv("./data/SeoulMapping.csv")
# '구청명', '면적'
sarea = pd.read_csv("./data/서울시 지역구 면적.csv", encoding='euc-kr')


# 데이터 정제
# 단위가 '개소'인 데이터 삭제
# '맨홀' , '빗물받이', '보급률'
uw_data = underwater.drop(columns=['맨홀', '빗물받이', '보급률'])

# 데이터 값 형변환하기
# '자치구별' 컬럼을 제외하기 위해 변수 지정
col_data = uw_data.columns[~uw_data.columns.isin(['자치구별'])]

# '-' 값을 '0'으로 대체, 쉼표 제거 및 숫자로 변환
# regex=True는 정규표현식을 사용한다는 의미. 이 부분이 없으면 오류 발생.
uw_data[col_data] = uw_data[col_data].replace('-', '0').replace(',', '', regex=True).astype(float)

# 변환된 데이터 확인
# print(uw_data[col_data])

# 각 행을 합산한 값을 새로운 컬럼으로 생성.
# sum 함수에 axis=1 인자 추가 : 각 행별로 합계를 계산
uw_data['하수도 및 횡단하수거 현황'] = uw_data[col_data].sum(axis=1)

# 하수도 및 부대시설 현황과 지역구 면적 merge
uw_data = pd.merge(uw_data, sarea, left_on='자치구별', right_on='구청명')

# np.divide() 함수를 이용하여 면적 당 하수시설 길이 계산
uw_data['1㎡당 하수시설 현황'] = np.divide(uw_data['하수도 및 횡단하수거 현황'], uw_data['면적'])

# 필요한 데이터를 제외하고 삭제
uw_data = uw_data[['자치구별','1㎡당 하수시설 현황']]

# print(uw_data)

# set 함수 이용하여 '하수도 및 부대시설' 데이터에서 지역 뽑아내기
for item in set(uw_data['자치구별']):
    # 해당 지역의 데이터를 uw_data에서 뽑아내기
    is_data = uw_data[uw_data['자치구별'] == item]

    count = is_data['1㎡당 하수시설 현황'].values[0]

    # 지역마다 원형 마커 생성
    marker = folium.CircleMarker(
        location=inseoul[inseoul['GU_NAME'] == item][['latitude', 'longitude']].values[0],
        radius=count/500,
        color='#3186cc',
        fill_color='#3186cc',
        popup=''.join((item, str(count), 'm')))

    # 생성한 원형마커를 지도에 추가
    marker.add_to(map_osm)

# 지도를 HTML 파일로 저장
map_osm.save('map_div.html')

# 웹 브라우저에서 HTML 파일 열기
webbrowser.open('map_div.html')


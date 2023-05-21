# U형측구 길이, 빗물받이 개수를 합산하여 지도에 표시
# 사용 데이터 변동이 있다면 다음 변수명의 선언문을 Crtl + F로 찾아가면 됨.
# uw_data

import pandas as pd
import folium
import webbrowser

# 지도 생성, 좌표는 서울 중앙으로 임의 지정함.
# location=[위도, 경도]
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=11)

# 데이터 불러오기
# '자치구별', 'U형측구', '빗물받이'
underwater = pd.read_csv("./data/하수도+및+부대시설+현황_20230517015330.csv")
# 'GU_NAME', 'longitude'(경도), 'latitude'(위도)
inseoul = pd.read_csv("./data/SeoulMapping.csv")    # 자치구 별 좌표값(지도 위 표시 위함)

# 데이터에서 필요한 부분만 저장
uw_data = underwater[['자치구별', 'U형측구', '빗물받이']]

# set 함수 이용하여 '하수도 및 부대시설' 데이터에서 지역 뽑아내기
for item in set(uw_data['자치구별']):
    # 해당 지역의 데이터를 uw_data에서 뽑아내기
    is_data = uw_data[uw_data['자치구별'] == item]

    # 빗물받이와 U형측구의 합계 계산'
    # 쉼표를 없애고, '-' 값을 NaN 데이터로 처리
    count = is_data['빗물받이'].str.replace(',', '').astype(int).sum() + is_data['U형측구'].str.replace(',', '').replace('-', '0').astype(int).sum()

    # 지역마다 원형 마커 생성
    marker = folium.CircleMarker(
        location=inseoul[inseoul['GU_NAME'] == item][['latitude', 'longitude']].values[0],
        radius=count/800+10,
        color='#3186cc',
        fill_color='#3186cc',
        popup=''.join((item, str(count),'개(m)')))

    # 생성한 원형마커를 지도에 추가
    marker.add_to(map_osm)

# 지도를 HTML 파일로 저장
map_osm.save('map.html')

# 웹 브라우저에서 HTML 파일 열기
webbrowser.open('map.html')

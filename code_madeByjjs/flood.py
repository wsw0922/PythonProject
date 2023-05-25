# 서울시 침수흔적도
import pandas as pd
import folium

# 서울시 침수흔적도
floot = pd.read_excel("./data/서울시_2022_침수흔적도.xlsx")
floot = floot.drop(columns=['OBJECTID','TYPE'])

#서울시 위도경도
crs = pd.read_csv("./data/SeoulMapping.csv")

#지도 생성
seoul = folium.Map(location=[37.557945, 126.99419], zoom_start=11)
#건수가 1000건이 넘는 구
tomuch = ('영등포구','동작구','관악구','서초구','구로구')
#기본값
basicDv = 25
basicColor = '#3186cc'
#1000건이 넘는 구에 적용되는 값
tomuchDv = 100
tomuchColor = '#ed6f63'

# 지역 정보를 set 함수를 사용하여 25개의 고유 지역 뽑기
for region in set(crs['GU_NAME']):
    dv = basicDv
    color = basicColor
    # 건수가 많은 지역일때 원크기와 색상 조정
    if(region in tomuch):
        dv = tomuchDv
        color = tomuchColor
    # 해당 지역의 데이터 개수를 count에 저장
    count = len(floot[floot['GU_NAM'] == region])
    # 해당 지역의 데이터를 CRS에서 뽑기
    CRS_region = crs[crs['GU_NAME'] == region]
    #circleMarker를 사용하여 지역마다 원형마커를 생성
    iframe = folium.IFrame(region + '<br>' + str(count)+'건')
    marker = folium.CircleMarker([CRS_region['latitude'],CRS_region['longitude']], #위치
                                radius=count/dv + 5, #원 크기
                                color = color,      #선색상
                                fill_color = color, #면색상
                                popup=folium.Popup(iframe, min_width=100, max_width=100)) #팝업
    marker.add_to(seoul)
    
seoul.save('./code_madeByjjs/seoul.html') # html에 저장

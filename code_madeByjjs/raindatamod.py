import pandas as pd
#지역별 월 강우량 데이터 생성
# 현재 data\2022 서울 지역구별 월 강우량 by pandas에 있는 파일을 만드는 프로그램입니다.
'''
서울시 강우량 정보 n월에서 구청명 10분우량 자료수집 시각 (yyyy-MM-dd hh:mm) -> 월별 지역별 총 강수량
구청명을 기준으로 10분 우량을 다 더함 하지만 10분우량 데이터에 문제가 있어서 일별 서울시 총 강수량 데이터를 가지고 1/x를 만들어서

구청명을 기준으로 다 더할 때 해당 일자의 1/x값을 곱해줌

데이터 *  1 / x = 일별강수량
1/x = 일별강수량 / 데이터

그리고 나온 결과가 해당월 지역구에 내린 강우량 / 서울시 면적 
-> 그래서 나온 결과에 서울시 면적 곱함
'''

# 기준이 될 해당년도 일별 강수량 파일
refValue = pd.read_csv("./data/2022년 강수량 (일별).csv", index_col="일").fillna(0) # NAN을 다 0으로
EndMonth = [31,28,31,30,31,30,31,31,30,31,30,31] # 각월의 말일
distSquare = pd.read_csv("./data/서울시 지역구 면적.csv",index_col='구청명',encoding='cp949')
distName = list(distSquare.index)
data = {
        '구청명' : distName
    }
#지역별 일 강수량 데이터
for mon in ["01","02","03","04","05","06","07","08","09","10","11","12"]:    
    #데이터
    rainData = pd.read_csv(f"./data/2022 서울 강우량/서울시_강우량_정보_2022년{mon}월.csv",encoding='cp949')
    #해당월 비교값
    monthlyRain = refValue[mon + '월']
    
    #날짜 문자열
    
    day = []
    for dayNum in range(EndMonth[int(mon) - 1]):
        if(dayNum < 9) :
            day.append(f"2022-{mon}-0" + str(dayNum + 1))
        else:
            day.append(f"2022-{mon}-" + str(dayNum + 1))

    #일별 강우량을 다 더한값
    dailyRain = []
    value = []
    for d in day:
        temp = rainData.loc[rainData['자료수집 시각'].str[:10] == d, ['10분우량']]
        dailyRain.append(temp["10분우량"].sum())
    print(mon,'월')
    #print(dailyRain)
    #나눌값 구하기
    for v in range(len(dailyRain)):
        if(monthlyRain[v] == 0):
                value.append(0) # monthlyRain 값이 기준이기에 이상값이 있으면 무시하기 위해 0 입력
        else:
            if(dailyRain[v] != 0):
                value.append(round(monthlyRain[v] / dailyRain[v],4))
            else:
                value.append(0) # 무시를 위해 0
    # 데이터 출력
    #print(value)
    '''print(pd.DataFrame({
        '강수량' : dailyRain,
        '보정값' : value
    }))'''
    amount = []
    for dist in distName:
        temp = rainData.loc[rainData['구청명']==dist,['자료수집 시각','10분우량']]
        for i in range(len(value)):
            if(value[i] >= 0 ):
                temp.loc[temp['자료수집 시각'].str[:10] == day[i],['10분우량']] = temp['10분우량'] * value[i] * 25
                #print(temp.loc[(temp['자료수집 시각'].str[8:10] == str(i + 1).zfill(2)) & temp['10분우량'] > 0,['10분우량']])
                #print(temp.loc[temp['10분우량'] > 0])
        amount.append(round(temp['10분우량'].sum(),0))
    data[f'{mon}월강수량'] = amount
rainData = pd.DataFrame(data)    
rainData.to_csv(f'./data/서울 지역구별 월강수량.csv',encoding='utf-8-sig')
print("완료")
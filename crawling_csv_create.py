import pandas as pd

# 식당 데이터 임포트하기
df = pd.read_csv('crawling\MarketData_20230930\Gyeonggi_202309.csv', encoding='utf-8-sig')
# 정부데이터 활용: https://www.data.go.kr/data/15083033/fileData.do -> 소상공인시장진흥공단_상가(상권)정보

# 음식점 데이터만 쓰기
df = df.loc[df['상권업종대분류명'] == '음식']  

# 다음과 같은 칼럼만 있으면 됨
df = df[['상호명', '상권업종중분류명', '상권업종소분류명', '표준산업분류명', '행정동명', '위도', '경도']]

print(df)

# 데이터 용량 줄여서 새로 저장하기
df.to_csv("Gyeonggi_2309.csv", index=False)

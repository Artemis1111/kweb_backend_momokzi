import pandas as pd
from geopy.distance import geodesic
import random

#CSV 파일 로드
#df = pd.read_csv('store_seoul.csv', sep=',', encoding='utf-8-sig')
df = pd.read_csv('anam.csv', sep=',', encoding='utf-8-sig')

print(df.columns)

#임의의 사용자 위치 설정 -> 나중엔 받아오기
user_location = (37.5826497929824, 127.028844976742)

#거리 계산 및 필터링
def filter_restaurants(row):
    restaurant_location = (row['위도'], row['경도'])
    return geodesic(user_location, restaurant_location).meters <= 500

#500m 이내의 식당만 필터링
nearby_restaurants = df[df.apply(filter_restaurants, axis=1)]

#랜덤으로 식당 추천
if not nearby_restaurants.empty:
    recommended_restaurant = random.choice(nearby_restaurants.to_dict('records'))
    print(f"추천 식당: {recommended_restaurant['상호명']}, 행정동명: {recommended_restaurant['행정동명']}")
else:
    print("500m 이내의 식당이 없습니다.")

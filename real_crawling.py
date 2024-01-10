import pandas as pd
from geopy.distance import geodesic
import random
from bs4 import BeautifulSoup as bs
import requests

#임의의 사용자 위치 설정 -> 나중엔 받아오기
user_location = (37.5826497929824, 127.028844976742)

#어떤 좌표에서 음식점을 검색했을 때의 정보 구하기
url = 'https://map.naver.com/p/api/search/allSearch?query=%%EC%%9D%%8C%%EC%%8B%%9D%%EC%%A0%%90&type=all&searchCoord=%s%%3B%s&boundary=' % (user_location[1], user_location[0])
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    data = data["result"]["place"]["list"]
    nearby_restaurants = []
    for original_data in data:
        # 여기 쓰여진 정보만 가져오기
        keys_to_extract = ["index", "id", "name", "category", "businessStatus", "y", "x", "reviewCount", "placeReviewCount"]
        new_restaurant = {key: original_data[key] for key in keys_to_extract if key in original_data}
        nearby_restaurants.append(new_restaurant)
else:
    print("요청 실패:", response.status_code)

#거리 계산 및 필터링
def filter_restaurants(row):
    restaurant_location = (row['y'], row['x'])
    return geodesic(user_location, restaurant_location).meters <= 500

#dataFrame으로 만들기
df = pd.DataFrame(nearby_restaurants)

#review 합치기
df["reviewCount"] += df["placeReviewCount"]
df.drop("placeReviewCount", axis=1, inplace=True)

#운영시간 정보 추출
df["businessStatus"] = df["businessStatus"].apply(lambda x: x['businessHours'])

#500m 이내의 식당만 필터링
nearby_restaurants = df[df.apply(filter_restaurants, axis=1)]


print(nearby_restaurants["businessStatus"])




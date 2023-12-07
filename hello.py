import requests # requests 라이브러리 설치 필요
from pprint import pprint

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for row in rows:
    print(row['MSRSTE_NM'],row['IDEX_MVL'])

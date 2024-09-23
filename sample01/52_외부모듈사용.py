# 파이썬에서는 기본적으로 제공하는 표준 라이브러리 이외에도 다양한 외부 모듈을 제공함
# 외부 모듈은 pip install로 설치 이후 import 해서 사용
# Beautiful Soup : HTML 또는 XML 파일에서 데이터를 추출하기 위해 사용하는 파이브러리
# 웹페이지를 크롤링 할 때 사용
# Requests : 서버에 HTTP 요청을 보내고 응답을 받는데 사용하는 라이브러리
# GET, POST, PUT, DELETE 등의  방식을 지원
import requests
from bs4 import BeautifulSoup
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

# HTTP GET 요청
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

for loc in soup.select("location"):
    print("도시 : ", loc.select_one("city").string)
    print("날씨 : ", loc.select_one("wf").string)
    print("최저기온 : ", loc.select_one("tmn").string)
    print("최고기온 : ", loc.select_one("tmx").string)
    print("-" * 20)
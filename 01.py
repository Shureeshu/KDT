'''
## 01. 인기 영화 조회

> 인기 영화 목록 개수 출력

-   requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
-   응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.
'''

import requests
from dotenv import dotenv_values
api_key = dotenv_values(".env").get('API_KEY')

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.
    # api_key = dotenv_values(".env").get('API_KEY')
    url = str(f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}')
    res = requests.get(url=url).json()
    # print(res.keys())
    # ['page', 'results', 'total_pages', 'total_results']
    return len(res.get('results'))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
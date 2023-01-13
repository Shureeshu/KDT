import requests
from pprint import pprint

'''
## 05. 영화 조회 및 추천 영화 조회

> 영화 제목으로 영화를 검색하고, 해당 영화의 추천 영화 조회

-   requests 라이브러리를 활용하여 TMDB에서 제목으로 영화를 검색(Search Movies)합니다.
-   응답 받은 결과 중 첫번째 영화의 `id` 를 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
-   추천 영화 목록을 리스트로 반환하는 함수를 작성합니다.
'''

from dotenv import dotenv_values
api_key = dotenv_values(".env").get('API_KEY')

def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    language = 'ko-KR'
    query = title
    include_adult = True
    
    url = str(f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language={language}&query={query}&include_adult={include_adult}')
    res = requests.get(url=url).json()

    total_pages = 1 # res.get('toal_pages')

    for page in range(1, total_pages+1):
      url = str(f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language={language}&query={query}&page={page}&include_adult={include_adult}')
      results = requests.get(url=url).json().get('results')
      movie_id = 0
      for movie in results:
        if movie.get('title') == title:
            # print(movie.get('title'), movie.get('id'))
            movie_id = movie.get('id') # integer
            break
    
    results.clear()
    if movie_id:
        url = str(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=ko-KR&page=1')
        res = requests.get(url=url).json()
        total_pages = 1 # res.get('toal_pages')
            
        for page in range(1, total_pages+1):
          url = str(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=ko-KR&page=1')
          results += requests.get(url=url).json().get('results')
        
        return [x['title'] for x in results]
    else:
        return
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

import requests
from pprint import pprint

'''
## 06. 출연진 및 연출진 데이터 조회
> 제목으로 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록 출력

-   requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
-   응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
-   출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
-   `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.
'''
from dotenv import dotenv_values
api_key = dotenv_values(".env").get('API_KEY')

def credits(title):
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
        url = str(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko-KR')
        res = requests.get(url=url).json()
        # print(res.keys())
        # dict_keys(['id', 'cast', 'crew'])
        cast = res.get('cast')
        crew = res.get('crew')
        # print(cast[0].keys())
        # dict_keys(['adult', 'gender', 'id', 'known_for_department', 'name', 'original_name', 'popularity', 'profile_path', 'cast_id', 'character', 'credit_id', 'order'])
        # print(crew[0].keys())
        # dict_keys(['adult', 'gender', 'id', 'known_for_department', 'name', 'original_name', 'popularity', 'profile_path', 'credit_id', 'department', 'job'])
        # print([ x['name'] for x in cast if x['cast_id'] < 10])
        # print([ x['name'] for x in crew if x['department'] == 'Directing'])
        cast = [ x['name'] for x in cast if x['cast_id'] < 10]
        crew = [ x['name'] for x in crew if x['department'] == 'Directing']
        return {'cast': cast, 'crew': crew}
    else:
        return

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

import requests
from pprint import pprint

from dotenv import dotenv_values
api_key = dotenv_values(".env").get('API_KEY')

def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    url = str(f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}')
    res = requests.get(url=url).json()
    # print(res.keys())
    # ['page', 'results', 'total_pages', 'total_results']
    total_pages = 1 # res.get('toal_pages')
    language = 'ko-KR'
    query = title
    include_adult = True
    movie_list = []
    for page in range(1, total_pages+1):
      url = str(f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language={language}&query={query}&page={page}&include_adult={include_adult}')
      results = requests.get(url=url).json().get('results')
      for movie in results:
        if movie.get('title') == title:
            # print(movie.get('title'), movie.get('id'))
            return movie.get('id')
    # for movie in movie_list:
    #   print(movie['title'], movie['vote_average'])
    return


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None

import requests
import constants
import datetime


def api_req(url, search):
    try:
        if(search):
            response = requests.get(url, params={'query': search})
            response.raise_for_status()
        else:
            response = requests.get(url)
            response.raise_for_status()
    except Exception as err:
        print('Other error occurred: ', err)
    else:
        data = response.json()
        return data


def genres_maker(genre_ids):

    genresDictionary = {}

    genres = []
    genreUrl = 'https://api.themoviedb.org/3/genre/movie/list?api_key=034f1dbe849aa92919d3b0f6d601ce76&language=en-US'

    genresRequest = api_req(genreUrl, None)

    for i in genresRequest['genres']:
        genresDictionary[i['id']] = i['name']

    for i in genre_ids:
        genres.append(genresDictionary[i])

    return genres


def get_list(request, resultsNumber, type):
    i = 0
    complete = []
    element = {
        "title": [],
        "release_date": [],
        "genres": [],
        "overview": [],
        # "poster_path": []
    }
    values = []
    if(type == "movie"):

        while i < len(request['results']) and i < resultsNumber:

            try:
                title = request['results'][i]['title']

                release_date = datetime.datetime.strptime(
                    request['results'][i]['release_date'], '%Y-%m-%d').strftime('%d/%m/%Y')
                genre_ids = request['results'][i]['genre_ids']
                overview = request['results'][i]['overview']
                # poster_path = constants.POSTER_URL + \
                #  request['results'][i]['poster_path']
            except:
                print("Error at", i)

            genres = genres_maker(genre_ids)

            element["title"].append(title)
            element["release_date"].append(release_date)
            element["genres"].append(genres)
            element["overview"].append(overview)
            # element["poster_path"].append(poster_path)

            i += 1
        return element

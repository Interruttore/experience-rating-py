import requests
import tools
import constants
import addToExcel


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


def getList(request, resultsNumber, type):
    i = 0
    complete = []
    element = {
        "title": [],
        "release_date": [],
        "genres": [],
        "overview": [],
        "poster_path": []
    }
    values = []
    if(type == "movie"):

        while i < len(request['results']) and i < resultsNumber:
            title = request['results'][i]['title']
            release_date = request['results'][i]['release_date']
            genre_ids = request['results'][i]['genre_ids']
            overview = request['results'][i]['overview']
            poster_path = constants.POSTER_URL + \
                request['results'][i]['poster_path']

            genres = genres_maker(genre_ids)

            element["title"].append(title)
            element["release_date"].append(release_date)
            element["genres"].append(genres)
            element["overview"].append(overview)
            element["poster_path"].append(poster_path)

            i += 1
        return element


def printItem(request, resultsNumber, type):
    i = 0
    if(type == "movie"):
        print(len(request['results']),
              " Results found, showing max: ", resultsNumber)

        while i < len(request['results']) and i < resultsNumber:
            title = request['results'][i]['title']
            release_date = request['results'][i]['release_date']
            genre_ids = request['results'][i]['genre_ids']

            genres = genres_maker(genre_ids)

            complete = tools.joiner(title, release_date, genres)
            print('[', i+1, ']', complete)
            i += 1


def movieSearch(searchTerm):

    movieUrl = 'https://api.themoviedb.org/3/search/movie?api_key=034f1dbe849aa92919d3b0f6d601ce76&language=en-US&page=1&include_adult=false'
    arg = -2
    movieRequest = None
    resultsNumber = 0

    while arg != 0:
        if(arg == 2):
            movieRequest = api_req(movieUrl, searchTerm)
            tools.clear()
            printItem(movieRequest, resultsNumber, "movie")
            arg = -1
        elif(arg == -1):
            while (arg == -1):
                tools.print_menu("movie_search")
                arg = input()
                check = tools.check_input(arg, 0, 3)
                arg = check

            if(arg == 2):
                resultsNumber += 5
            elif(arg == 3 and movieRequest != None):
                addToExcel.addMovie(movieRequest)
                arg = -1

        else:
            tools.clear()
            resultsNumber = constants.DEAFULT_RESULT_NUMBER
            searchTerm = input("Enter movie name:")
            movieRequest = api_req(movieUrl, searchTerm)
            arg = -1

            tools.clear()
            printItem(movieRequest, resultsNumber, "movie")

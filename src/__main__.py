import api
import constants
import excel_functions
import modules
import PySimpleGUIQt as sg

# TODO Check for bugs


def main():

    main_elements = [
        [
            sg.Frame("Search", modules.search_column,
                     background_color="transparent"),
            # sg.VSeperator(),
            sg.Frame("Poster", modules.poster_column,
                     background_color="transparent"),
            sg.Frame("Info", modules.item_column,
                     background_color="transparent")

        ]
    ]

    tools_elements = [
        [
            sg.Column(modules.tools_column),
            sg.VSeperator(),
            sg.Column(modules.tools_info_column)
        ]
    ]

    main_tab = [
        [
            sg.Tab("Main", main_elements),
            sg.Tab("Tools", tools_elements),
            # sg.Tab("Options", otpions_elements)
        ]
    ]

    layout = [
        [
            sg.TabGroup(main_tab, "top", title_color=("black"))

        ]
    ]
    sg.theme('Dark Blue 12')
    window = sg.Window("Experience Rating", layout)

    resultNumber = constants.DEAFULT_RESULT_NUMBER

    elements = None
    genre_list = None
    info = {
        "name": "",
        "release_date": "",
        "genre": "",
        "vote": "",

    }
    while(True):

        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Search":
            if not values["-SEARCH_BAR-"] or values["-SEARCH_BAR-"].isspace():
                print("Empty search string")
            else:
                movieRequest = api.api_req(
                    constants.MOVIE_URL, values["-SEARCH_BAR-"])
                elements = api.get_list(
                    movieRequest, resultNumber, "movie", window)

                window["-ITEM_LIST-"].update(elements["title"])

        if event == "-ITEM_LIST-":

            try:

                index = elements["title"].index(window["-ITEM_LIST-"].get()[0])

                window["-ITEM_NAME-"].update(elements["title"][index])
                window["-ITEM_DATE-"].update(elements["release_date"][index])

                #! TODO MAXIMUM 2
                i = 0
                for x in elements["genres"][index]:
                    if not genre_list:
                        genre_list = x
                    elif i < 1:
                        genre_list += "/" + x
                        i += 1

                window["-ITEM_GENRE-"].update(genre_list)
                window["-ITEM_OVERVIEW-"].update(elements["overview"][index])
                window["-POSTER-"].update(data=elements["poster"][index])
                genre_list = None
            except:
                print("Skipped one cycle")

        if event == "Add movie":

            window["-ERROR-"].update("Adding...", text_color="black")
            filename = window["-EXCEL_INPUT-"].get()
            info["name"] = window["-ITEM_NAME-"].DisplayText
            info["release_date"] = window["-ITEM_DATE-"].DisplayText
            info["genre"] = window["-ITEM_GENRE-"].DisplayText
            info["vote"] = values["-VOTE-"]
            try:
                excel_functions.add_movie(info, filename)
                window["-ERROR-"].update("Success!", text_color="green")
            except:
                window["-ERROR-"].update("Error!", text_color="red")

        if event == "Clean duplicates":
            excel_functions.remove_duplicate(filename)


#! Testing purposes
main()

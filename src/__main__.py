import api
import constants
import add_excel
import PySimpleGUIQt as sg

# TODO Check for bugs


def main():
    search_column = [
        [
            sg.In(size=(25, 1), enable_events=True,
                  key="-SEARCH_BAR-", focus=True, ),
            sg.Submit(size=(10, 1), button_text="Search")
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(36, 10), key="-ITEM_LIST-"
            )
        ],
        [
            sg.In(size=(25, 1), enable_events=True,
                  key="-EXCEL_INPUT-"),
            sg.FileBrowse(file_types=(("Excel Files ", "*.xlsx"),)),
        ]
    ]

    poster_column = [
        [
            sg.Image(filename="", key="-POSTER-")
        ],
    ]

    item_column = [
        [
            sg.Text(size=(6, 1),
                    text="Name:"),
            sg.Text(size=(30, 1),
                    key="-ITEM_NAME-"),

        ],
        [
            sg.Text(size=(6, 1),
                    text="Date:"),
            sg.Text(size=(30, 1),
                    key="-ITEM_DATE-"),

        ],
        [
            sg.Text(size=(6, 1),
                    text="Genre:"),
            sg.Text(size=(30, 1),
                    key="-ITEM_GENRE-"),

        ],
        [
            sg.Text(size=(6, 1),
                    text="Overview:"),
            sg.Multiline(size=(30, 10), disabled=True,
                         key="-ITEM_OVERVIEW-"),

        ],
        [
            sg.Spin(values=constants.VOTE_VALUES,
                    enable_events=True, key="-VOTE-", size=(5, 1)),
            sg.Submit(size=(10, 1), button_text="Add movie"),
            sg.Text(size=(15, 1), key="-ERROR-", font=('Courier', 10))

        ]

    ]

    layout = [
        [
            sg.Column(search_column),
            sg.VSeperator(),
            # sg.Column(poster_column),
            sg.Column(item_column)
        ]
    ]
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

            movieRequest = api.api_req(
                constants.MOVIE_URL, values["-SEARCH_BAR-"])
            elements = api.get_list(
                movieRequest, resultNumber, "movie")

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
                # window["-POSTER-"].update(data=poster)
                # TODO FIX POSTER
                genre_list = None
            except:
                print("Skipped one cycle")

        if event == "Add movie":

            filename = window["-EXCEL_INPUT-"].get()
            info["name"] = window["-ITEM_NAME-"].DisplayText
            info["release_date"] = window["-ITEM_DATE-"].DisplayText
            info["genre"] = window["-ITEM_GENRE-"].DisplayText
            info["vote"] = values["-VOTE-"]
            try:
                add_excel.add_movie(info, filename)
                window["-ERROR-"].update("Success!", text_color="green")
            except:
                window["-ERROR-"].update("Error!", text_color="red")


#! Testing purposes
main()

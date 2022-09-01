import PySimpleGUIQt as sg
import constants

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
                text="Name:", background_color="transparent"),
        sg.Text(size=(30, 1),
                key="-ITEM_NAME-", background_color="transparent"),

    ],
    [
        sg.Text(size=(6, 1),
                text="Date:", background_color="transparent"),
        sg.Text(size=(30, 1),
                key="-ITEM_DATE-", background_color="transparent"),

    ],
    [
        sg.Text(size=(6, 1),
                text="Genre:", background_color="transparent"),
        sg.Text(size=(30, 1),
                key="-ITEM_GENRE-", background_color="transparent"),

    ],
    [
        sg.Text(size=(6, 1),
                text="Overview:", background_color="transparent"),
        sg.Multiline(size=(30, 10), disabled=True,
                     key="-ITEM_OVERVIEW-", background_color="transparent", text_color="white"),

    ],
    [
        sg.Spin(values=constants.VOTE_VALUES,
                enable_events=True, key="-VOTE-", size=(5, 1)),
        sg.Submit(size=(10, 1), button_text="Add movie"),
        sg.Text(size=(15, 1), key="-ERROR-", font=('Courier', 10),
                background_color="transparent")

    ],
    [
        sg.ProgressBar(100, key="-PROGRESS_BAR-", bar_color=("green", "white"))
    ]

]

tools_column = [
    [
        sg.Button("Clean duplicates")
    ],
]

tools_info_column = [
    [
        sg.Multiline(size=(50, 10), disabled=True,
                     key="-INFO_TOOLS-"),
    ]
]

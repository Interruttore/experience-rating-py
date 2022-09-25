import PySimpleGUI as sg
import constants

sg.theme('DarkTeal4')

search_column = [
    [
        sg.In(size=(25, 1), enable_events=True,
              key="-SEARCH_BAR-", focus=True, ),
        sg.Submit(size=(10, 1), button_text="Search")
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(36, 10), key="-ITEM_LIST-", expand_x=True, expand_y=True, )
    ],
    [
        sg.In(size=(25, 1), enable_events=True,
              key="-EXCEL_INPUT-"),
        sg.FileBrowse(file_types=(("Excel Files ", "*.xlsx"),)),
    ]
]

poster_column = [
    [
        sg.Image(filename="", key="-POSTER-", expand_x=True, expand_y=True)
    ],
]

item_column = [
    [
        sg.Text(size=(6, 1),
                text="Name:",),
        sg.Text(size=(30, 1),
                key="-ITEM_NAME-",),

    ],
    [
        sg.Text(size=(6, 1),
                text="Date:",),
        sg.Text(size=(30, 1),
                key="-ITEM_DATE-",),

    ],
    [
        sg.Text(size=(6, 1),
                text="Genre:",),
        sg.Text(size=(30, 1),
                key="-ITEM_GENRE-",),

    ],
    [
        sg.Text(size=(6, 1),
                text="Overview:",),
        sg.Multiline(size=(30, 10), disabled=True,
                     key="-ITEM_OVERVIEW-", text_color="white", expand_x=True, expand_y=True),

    ],
    [
        sg.Spin(values=constants.VOTE_VALUES,
                enable_events=True, key="-VOTE-", size=(5, 1)),
        sg.Submit(size=(10, 1), button_text="Add movie"),
        sg.Text(size=(15, 1), key="-ERROR-", font=('Courier', 10),)

    ],
    [
        sg.ProgressBar(100, key="-PROGRESS_BAR-",
                       bar_color=("green", "white"), border_width=1, expand_x=True, size=(0, 15))
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

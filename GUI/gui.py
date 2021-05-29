import PySimpleGUI as sg
from BACKEND import process

lewo = [

    [
        sg.Text("Sciezka do obrazu: "),

        sg.In(size=(25, 1), enable_events=True, key="DIRECTORY"),

        # sg.filedialog.askopenfilename(),
        sg.Button(button_text="CHOSE A FILE", key="FILE", auto_size_button=True, ),
        # sg.Button(button_text="OK", key="FIRE", auto_size_button=True)

    ],
]

prawo = [

    [sg.Text(size=(50, 1), key="PATH")],

    [sg.Image(key="IMAGE"),

    sg.Image(key="IMAGE_1")],

    [sg.Text(size=(50, 2), key="PROB")]

]

layout = [

    [
        sg.Column(lewo),
        sg.Column(prawo)
    ]

]

window = sg.Window("Rozpoznawanie znakow", layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "FILE":
        try:
            filename = sg.filedialog.askopenfilename()
            result = process.recognize(filename)
            window["IMAGE"].update(filename=filename)

            if not result:
                window["PATH"].update("Błąd w formacie obrazu")
                window["PROB"].update("")
                window["IMAGE_1"].update()
                continue

            # filename = '...' + filename.split('GitHub')[1]
            window["DIRECTORY"].update(filename)
            window["PATH"].update(result[0])

            if result[2] >= 20:
                window["PROB"].update("zgodnosc: " + str(result[2]) + "%")
                window["IMAGE_1"].update(str(result[1]))
            else:
                window["PROB"].update("zgodnosc z: " + str(result[0]) + " w: " + str(result[2]) + "%")
                window["PATH"].update("Nie wykryto znaku")
                window["IMAGE_1"].update(str(result[1]))

        except:
            pass

window.close()

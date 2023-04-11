import PySimpleGUI as sg
from pathlib import Path

smileys = [
    'Happy', [':)','xD',':D','<3'],
    'Sad', [':('],
    'Other', [':|']
]

menu = [
       ['File',['Open','Save As','---','Exit','New']],
       ['Tools',['Word count and character count']],
       ['Add',smileys]
]
def Editor_function():
    sg.theme('GrayGrayGray')
    layout = [
        [sg.Menu(menu)],
        [sg.Text('Untitled',key = '-DOCNAME-',enable_events = True)],
        [sg.Multiline(size = (40,30),no_scrollbar = True,key = '-MULTILINE-')]
    ]
    return  sg.Window('Text editor',layout)

window = Editor_function()
save = ''

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Word count and character count":
        char = values['-MULTILINE-'].replace(' ','')
        char_count = len(char)
        char_count_display = f'The character count is {char_count}'
        word = values['-MULTILINE-'].split()
        word_count = len(word)
        word_count_display = f'The word count is {word_count}'
        sg.popup(char_count_display + '\n' + word_count_display)

    if event in (smileys[1]+smileys[3]+smileys[5]):
        new_event = values['-MULTILINE-'] + '' + event
        window['-MULTILINE-'].update(new_event)

    if event == 'Open':
        file_path = sg.popup_get_file("Open file",no_window = True)
        if file_path:
            file = Path(file_path)
            file_content = file.read_text()
            window['-MULTILINE-'].update(file_content)
            window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Save As':
        if len(values['-MULTILINE-']) < 1:
            save = False
            sg.popup('File is empty')
        else:
            save = True

        if save == True:
        # A window should appear that would contain the file path,by default
        # Setting no_window to true would make the window invisible but everything would still be okay
        # Setting save path to true would make it act like a savable file
            save_path = sg.popup_get_file('Save As', no_window=True, save_as=True) + '.txt'
            savable_path = Path(save_path)
            saved_path = savable_path.write_text(values['-MULTILINE-'])
            window['-DOCNAME-'].update(save_path.split('/')[-1])

    if event == 'New':
        window = Editor_function()



window.close()
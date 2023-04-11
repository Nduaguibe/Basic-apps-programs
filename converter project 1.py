
import PySimpleGUI as sg
# the window is going to contain a title and a layout
#the indices of the list represents the rows of the layout
sg.theme('DarkAmber')
layout= [
    [sg.Input(key = '-INPUT-'),sg.Spin(['km to mile','kg to pound','sec to min','min to sec',
    'centimeter cube to decimeter cube','decimeter cube to centimeter cube'],key = '-UNITS-'),
     sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('Output', key = '-OUTPUT-')]
    ]
window = sg.Window('Converter',layout)

while True:
# window.read would would return a tuple
    event,values = window.read()
# event is an action that is triggered by other elrments
# values are simply anything on the layout that stores any kind of value
    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
            # Matching the code below to km to mile
                case 'km to mile':
                    output = round(float(input_value)*0.6214,2)
                    output_string = f'{input_value} km is equal to {output} miles'
                case 'kg to pound':
                    output = round(float(input_value) * 2.205, 2)
                    output_string = f'{input_value} kg is equal to {output} pounds'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} sec is equal to {output} mins'
                case 'min to sec':
                    output = round(float(input_value) * 60, 2)
                    output_string = f'{input_value} min is equal to {output} secs'
                case 'centimeter cube to decimeter cube':
                    output = round(float(input_value) * 1000, 2)
                    output_string = f'{input_value} centimeter cube  is equal to {output} decimeter cube'
                case 'decimeter cube to centimeter cube':
                    output = round(float(input_value) / 1000, 3)
                    output_string = f'{input_value} decimeter cube is equal to {output} centimeter cube'
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number')



window.close()

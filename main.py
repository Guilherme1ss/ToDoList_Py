import PySimpleGUI as sg

def initial_window ():
    sg.theme('DarkBlue4')
    line = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    wLayout = [
        [sg.Frame('Tarefas', layout=line, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('To-Do List', layout=wLayout, finalize=True)

window = initial_window()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        window.extend_layout(window['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        window.close()
        window = initial_window()
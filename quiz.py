import textwrap
import PySimpleGUI as sg      
import csv

with open("questions.csv") as file:
    read = csv.reader(file)
    for idx, row in enumerate(read):
        if (idx != 0):
            # Extract the question, answer and explanation from each row
            [question, solution, explanation] = row
            question = textwrap.fill(question, 80)
            explanation = textwrap.fill(explanation, 60)
            sg.theme('BluePurple')

            # Create simple quiz interface
            layout = [[sg.Text(question, size=(80, None))],
                    [sg.Input(key='-IN-')],
                    [sg.Text(key='-OUTPUT-')],
                    [sg.Button('Check Answer'), sg.Button('Next question')]]

            window = sg.Window('CodeCo Quiz', layout).Finalize()
            window.Maximize()

            # If there are still questions left, prompt the user
            while True:
                event, values = window.read()
                answer = values['-IN-']
                if event == sg.WIN_CLOSED or event == 'Next question':
                    break
                if event == 'Check Answer':
                    if (answer.lower() == solution.lower()):
                        window['-OUTPUT-'].update("CORRECT!!!")
                        print("Correct")
                    else:
                        window['-OUTPUT-'].update(f"INCORRECT {explanation}")
                        print("Incorrect")
            window.close()

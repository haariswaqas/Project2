import PySimpleGUI as sg
import pyttsx3

# Creating/Initializing a text-to-speech engine
txt_to_speech_engine = pyttsx3.init()

# Defining a speak function to actually convert typed text to speech
def speak(text, voice_id):
    # Setting the rate and volume properties of the text-to-speech-engine
    txt_to_speech_engine.setProperty('rate', 150)
    txt_to_speech_engine.setProperty('volume', 0.8)
    voices = txt_to_speech_engine.getProperty('voices')

    # Conditional statement to determine the voice (male or female based on voice_id..male is 0, female is 1)
    if voice_id == 0:
        txt_to_speech_engine.setProperty('voice', voices[0].id)
    else:
        txt_to_speech_engine.setProperty('voice', voices[1].id)

    # converting input text to speech
    txt_to_speech_engine.say(text)
    txt_to_speech_engine.runAndWait()

# define the layout of the GUI using the PySimpleGui library
layout = [
    [sg.Text('Enter text to Speak:', font=('Helvetica', 12, 'bold'), text_color='black', background_color='lightgrey')],
    [sg.InputText(key='-INPUT-', size=(40, 1), font=('Helvetica', 12), background_color='white', text_color='black')],
    [sg.Text('Select voice type: ', font=('Helvetica', 12, 'bold'), text_color='black', background_color='lightgrey')],
    [sg.Radio('Male', 'RADIO1', default=True, key='-MALE-', font=('Helvetica', 12, 'bold'), text_color='black', background_color='lightgrey'),
     sg.Radio('Female', 'RADIO1', key='-FEMALE-', font=('Helvetica', 12, 'bold'), text_color='black', background_color='lightgrey', pad=(20, 0))],
    [sg.Button('Speak', button_color=('white', 'green'), font=('Helvetica', 12, 'bold'), size=(10,1), pad=((50,10),(10,10))),
     sg.Button('Exit', button_color=('white', 'firebrick'), font=('Helvetica', 12, 'bold'), size=(10,1), pad=((0,50),(10,10)))]
]



# create the window
window = sg.Window('Text-to-Speech Application', layout, size=(600, 250), background_color='lightgrey', resizable=True, element_justification='center', finalize=True)




# create an event loop to process events and update the GUI
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Speak':
        text = values['-INPUT-']
        if text:
            if values['-MALE-']:
                voice_id = 0
            else:
                voice_id = 1
            speak(text, voice_id)

# close the window and exit the program
window.close()

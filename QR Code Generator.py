# Import the necessary libraries
import PySimpleGUI as sg
import qrcode

# Set the theme for the UI
sg.theme('GreenMono')

# Define the layout for the app
layout = [    [sg.Text('Enter Text: ', font=('Helvetica', 12, 'bold')), sg.InputText(font=('Helvetica', 12), size=(30,1))],
    [sg.Button('Create', font=('Helvetica', 12), button_color=('white', '#007F00')),      sg.Button('Exit', font=('Helvetica', 12), button_color=('white', 'firebrick'))],
    [sg.Image(key='-IMAGE-', size=(200, 150))]
]


# Create the window
window = sg.Window('QR Code Generator', layout)

# Event loop for the app
while True:
    # Read events and values from the window
    event, values = window.read()
    
    # If the Exit button or window is closed, exit the app
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    # If the Create button is clicked, generate the QR code image
    if event == 'Create':
        # Get the text input from the user
        data = values[0]
        # If the text input is not empty, generate the QR code
        if data:
            # Generate the QR code image
            img = qrcode.make(data)
            # Save the QR code image to a file
            img.save('qrcode.png')
            # Update the image in the UI
            window['-IMAGE-'].update(filename='qrcode.png')

# Close the window and exit the app
window.close()
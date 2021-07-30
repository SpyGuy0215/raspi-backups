import PySimpleGUI as sg 
import os

layout = [[sg.Text("KeyBindr")], [sg.Button("OK")], [sg.Button("Launch Terminal")]]

sg.theme('DarkBlue')
window = sg.Window("Hello World", layout)

while True:
	event, values = window.read()
	if event == 'OK' or event == sg.WIN_CLOSED:
		break
	if event == "Launch Terminal":
		os.system("lxterminal")
		
window.close()
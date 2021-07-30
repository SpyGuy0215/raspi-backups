import PySimpleGUI as sg 
import os
import keyboard

numOfKeybinds = 0
numOfSavedKeybinds = 0

layout = [
	[sg.Text("KeyBindr - Make keybinds easy!")], 
	[sg.Text('Keybind #1'), sg.Input(default_text="keybind", enable_events=True), sg.Input(default_text="Command to run", enable_events=True)],
	[sg.Button('Add Keybind'), sg.Button('Save Changes')]
]
sg.theme('DarkBlue')
window = sg.Window("KeyBindr", layout)

keyboard.add_hotkey('ctrl + alt + t', lambda: os.system('gnome-terminal &'))

while True:
	event, values = window.read()
	print(values)
	if event == sg.WIN_CLOSED:
		break
	if event == 'Save Changes':
		numOfBindsAdded = numOfKeybinds - numOfSavedKeybinds
		for i in range(numOfBindsAdded - 1):
			print(values)
			print('value: ' + values[numOfSavedKeybinds + i])
	if event == 'Add Keybind':
		numOfKeybinds = numOfKeybinds + 1
		
window.close()
import os
import subprocess as sp

# create a dictionary with software as name and path as value
paths = {
    'VS Code': "/usr/share/applications/code.desktop",
    'Calculator': "/usr/share/raspi-ui-overrides/applications/galculator.desktop",
    'Notepad': "/usr/share/raspi-ui-overrides/applications/mousepad.desktop",
}

# Opens VS Code
def open_vs_code():
    os.startfile(paths['VS Code'])

# Opens Calculator
def open_calc():
    os.startfile(paths['Calculator'])

# Opens Notepad
def open_notepad():
    os.startfile(paths['Notepad'])

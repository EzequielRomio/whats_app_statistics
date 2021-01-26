import codecs
from tkinter import filedialog

import str_helpers
import show_results_script

def load_chat_file():
    chat_file = filedialog.askopenfilename()

    if not chat_file: # If user press cancel or Escape
        invalid_chat('cancel')

    return chat_file


def calculate_msgs(chat_file):
    with codecs.open(chat_file, 'r', encoding='utf-8', errors='ignore') as f:
        msgs_result = str_helpers.line_reader(f)
    
    return msgs_result


def button_action(window, start_button):
    chat_file = load_chat_file()
    msgs_results = calculate_msgs(chat_file)
    group_name = window.textinput(
    'Nombre de Grupo',
    'Ingrese un nombre para el GRUPO\n'
    )
    
    if group_name is None: #if user press cancel or Escape
        group_name = 'Grupo sin nombre'

    sorted_msgs = sorted(msgs_results.items(), key=lambda x: x[1], reverse=True)
    
    show_results_script.show_results(sorted_msgs, group_name)


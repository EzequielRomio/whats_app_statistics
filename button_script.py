import codecs
from tkinter import messagebox
from tkinter import filedialog

import str_helpers
import show_results_script


def load_chat_file():
    chat_file = filedialog.askopenfilename(filetypes=[('Archivos de Texto', '.txt')])

    return chat_file


def wrong_file_format_alert():
    message = "El archivo seleccionado no posee formato de chat de WhatsApp"
    messagebox.showwarning(title="Ocurrió un problema", message=message)


def show_multimedia_warning():
    message = "Los archivos multimedia tales como audios o videos fueron omitidos."
    messagebox.showinfo(title="Archivos Multimedia", message=message)


def calculate_msgs(chat_file):
    with codecs.open(chat_file, 'r', encoding='utf-8', errors='ignore') as f:
        msgs_result = str_helpers.line_reader(f)
    
    return msgs_result


def check_contact_list(msgs_result):
    names_to_delete = []
    
    for name in msgs_result.keys():
        if msgs_result[name] < 10:
            answer = messagebox.askquestion(
                title="Contactos dudosos", 
                message="Es '{}' un contacto real del grupo?".format(name)
            )
            if answer == 'no':
                names_to_delete.append(name)            

    for name in names_to_delete:
        del msgs_result[name]

    return msgs_result


def button_action(window, start_button):
    chat_file = load_chat_file()
    
    if not chat_file:
        return None # Cancels button_script's execution

    msgs_results = calculate_msgs(chat_file)

    if not msgs_results:
        wrong_file_format_alert()
        return None # Cancels button_script's execution


    group_name = window.textinput(
    'Nombre de Grupo',
    'Ingrese un nombre para el GRUPO\n'
    )
    
    if group_name is None: #if user press cancel or Escape
        group_name = 'Grupo sin nombre'


    msgs_results = check_contact_list(msgs_results)
    show_multimedia_warning()

    sorted_msgs = sorted(msgs_results.items(), key=lambda x: x[1], reverse=True)
    
    show_results_script.show_results(sorted_msgs, group_name)


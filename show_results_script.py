import matplotlib.pyplot as plt
import numpy as np

from models import PATH


def join_up_smaller_values(msgs_results):
    total_values = 0
    for msgs in msgs_results:
        total_values += msgs[1]

    percents = [(msgs[1] * 100) / total_values for msgs in msgs_results]
    
    names = ''
    value = 0
    result_list = []
    low_percent_flag = False

    for ix in range(len(msgs_results)):
        if percents[ix] <= 5:
            names += msgs_results[ix][0] + '\n'
            value += msgs_results[ix][1]
            low_percent_flag = True
        else: 
            result_list.append(msgs_results[ix])

    if low_percent_flag:    
        result_list.append((names, value))

    return result_list


def get_bar_labels_and_sizes(msgs_results):
    bar_labels = []
    bar_sizes = []
    for element in msgs_results:
        bar_labels.append(element[0])
        bar_sizes.append(element[1])

    return bar_labels, bar_sizes


def get_pie_labels_and_sizes(msgs_results): 
    pie_results = join_up_smaller_values(msgs_results)

    pie_labels = []
    pie_sizes = []
    for element in pie_results:
        pie_labels.append(element[0])
        pie_sizes.append(element[1])

    return pie_labels, pie_sizes


def show_results(msgs_results, group_name):
    bar_labels, bar_sizes = get_bar_labels_and_sizes(msgs_results)
    pie_labels, pie_sizes = get_pie_labels_and_sizes(msgs_results)

    #explode = get_explode(msgs_result) #
    explode = [0.03 for _ in range(len(pie_sizes))]  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    fig1.canvas.set_window_title(group_name)
    ax1.pie(pie_sizes, explode=explode,labels=pie_labels, autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_iconbitmap(PATH + 'images/favicon.ico')

    np.random.seed(19680801)
    plt.rcdefaults()
    fig2, ax = plt.subplots()
    fig2.canvas.set_window_title(group_name)

    bar_labels = [result[0] + ':  ' + str(result[1]) + '  ' for result in msgs_results]

    y_pos = np.arange(len(bar_labels))

    ax.barh(y_pos, bar_sizes, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(bar_labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Mensajes')
    ax.set_title(group_name)


    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_iconbitmap(PATH + 'images/favicon.ico')

    plt.show()


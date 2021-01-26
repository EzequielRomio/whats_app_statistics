import matplotlib.pyplot as plt
import numpy as np

from models import PATH


def show_results(msgs_result, group_name):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = [result[0] for result in msgs_result]
    sizes = [result[1] for result in msgs_result]
    explode = [0.03 for _ in range(len(sizes))]  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    fig1.canvas.set_window_title(group_name)
    ax1.pie(sizes, explode=explode,labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_iconbitmap(PATH + 'images/favicon.ico')

    np.random.seed(19680801)
    plt.rcdefaults()
    fig2, ax = plt.subplots()
    fig2.canvas.set_window_title(group_name)

    labels = [result[0] + ':  ' + str(result[1]) + '  ' for result in msgs_result]

    y_pos = np.arange(len(labels))

    ax.barh(y_pos, sizes, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Mensajes')
    ax.set_title('Gráfico de Barras')


    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_iconbitmap(PATH + 'images/favicon.ico')

    plt.show()


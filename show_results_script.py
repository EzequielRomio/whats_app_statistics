import matplotlib.pyplot as plt
import numpy as np

def show_results(msgs_result, group_name):
     
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = [result[0] for result in msgs_result]
    sizes = [result[1] for result in msgs_result]
    explode = [0.03 for _ in range(len(sizes))]  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode,labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()

    labels = [result[0] + ':  ' + str(result[1]) + '  ' for result in msgs_result]

    y_pos = np.arange(len(labels))

    ax.barh(y_pos, sizes, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Valores')
    ax.set_title('Cantidad de mensajes')


    plt.show()


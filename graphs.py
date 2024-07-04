import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

windowWidth = 1200
windowHeight = 700
pad = 10

# width=(3*windowWidth/4 - 6*pad) / 2, height=(windowHeight-5*pad) / 2

def igGraph():
    my_dpi = 200
    df = pd.read_csv("DataPoints.csv", index_col=False)
    x = df.Date
    y = df.IGFollowers
    fig, ax = plt.subplots()
    fig.set_size_inches((3*windowWidth/4 - 6*pad) / 2 / my_dpi, (windowHeight-5*pad) / 2 / my_dpi)
    ax.scatter(x,y)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
    return fig
    
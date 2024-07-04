import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from datetime import datetime

windowWidth = 1200
windowHeight = 700
pad = 10
my_dpi = 227

# width=(3*windowWidth/4 - 6*pad) / 2, height=(windowHeight-5*pad) / 2

def bigGraph():
    df = pd.read_csv("DataPoints.csv", index_col=False)
    x = pd.to_datetime(df.Date)
    yIG = df.IGFollowers
    yYT = df.YTSubscribers
    ySP = df.SPMonthly
    yAP = df.APMonthly
    plt.rcParams.update({
        "xtick.major.size": 2,
        "ytick.major.size": 2,
        "xtick.major.width": 0.3,
        "ytick.major.width": 0.3,
        "xtick.major.pad": 1,
        "ytick.major.pad": 1,
        "xtick.labelsize": 2,
        "lines.linewidth": 2,
        'axes.linewidth': 0.25,
        'font.size': 2,
        'axes.titlepad': 1.0
})
    print(plt.rcParams)

    lw = 0.5
    date_format = '%b %Y' # "%Y-%m-%d %H:%M:%S.%f"

    fig, axs = plt.subplots(2, 2, dpi=my_dpi, figsize=((0.75*windowWidth - 2*pad)/ (2*my_dpi), (windowHeight-2*pad) / (2*my_dpi)))
    axs[0,0].plot(x,yIG, linewidth=lw, color='yellow')
    axs[0,0].xaxis.set_major_locator(plt.MaxNLocator(6))
    axs[0,0].xaxis.set_major_formatter(mdates.DateFormatter(date_format))
    axs[0,0].set_title("Instagram Followers")

    axs[0,1].plot(x,yYT, linewidth=lw, color='red')
    axs[0,1].xaxis.set_major_locator(plt.MaxNLocator(6))
    axs[0,1].xaxis.set_major_formatter(mdates.DateFormatter(date_format))
    axs[0,1].set_title("YouTube Subscribers")

    axs[1,0].plot(x,ySP, linewidth=lw, color='green')
    axs[1,0].xaxis.set_major_locator(plt.MaxNLocator(6))
    axs[1,0].xaxis.set_major_formatter(mdates.DateFormatter(date_format))
    axs[1,0].set_title("Spotify Monthly Listeners")

    axs[1,1].plot(x,yAP, linewidth=lw, color='pink')
    axs[1,1].xaxis.set_major_locator(plt.MaxNLocator(6))
    axs[1,1].xaxis.set_major_formatter(mdates.DateFormatter(date_format))
    axs[1,1].set_title("Apple Music Monthly Listeners")
    

    plt.subplots_adjust(left=0.06, right=0.96, bottom=0.06, top=0.96, wspace=0.15, hspace=0.2)
    # ax.set_title("Instagram Followers")
    # ax.set_ylabel("Followers")
    # ax.set_xlabel("Time")

    
    
    return fig
    
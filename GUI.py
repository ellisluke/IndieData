import customtkinter
import dataFetch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import graphs

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("1200x700")
windowWidth = 1200
windowHeight = 700
pad = 10

def buildScreen():

    def refresh():
        dataFetch.refreshData(instagramField.get(), youtubeField.get(), spotifyField.get(), appleField.get())
        

    #### ---- BUILD THE SCREEEN ---- ####
   
    # Fetch and populate data from ScrapeLinks.csv and DataPoints.csv
    linkData = pd.read_csv("ScrapeLinks.csv", index_col=False)

    ### LEFT FORM FRAME ###
    mainFrameL = customtkinter.CTkFrame(master=app, width=windowWidth/4, height=windowHeight-2*pad)
    mainFrameL.grid(row=1, column=1, padx=pad, pady=pad)
    mainFrameL.pack_propagate(0)

    # Header label
    formHeaderLabel = customtkinter.CTkLabel(mainFrameL, text="Data Sources", fg_color="transparent", font=("Helvetica", 30))
    formHeaderLabel.pack(pady=48, padx=10)

    # Fields to enter/edit links where scraper should look
    instagramFieldLabel = customtkinter.CTkLabel(mainFrameL, text="Instagram Handle", fg_color="transparent", font=("Helvetica", 20))
    instagramFieldLabel.pack(pady=6, padx=10)
    instagramField = customtkinter.CTkEntry(mainFrameL, placeholder_text="Instagram Handle", width=250)
    instagramField.pack(pady=0, padx=10)
    instagramField.insert(0, linkData.loc[linkData.Platform == 'Instagram']['Link'].values[0])

    spacerLabel1 = customtkinter.CTkLabel(mainFrameL, text=" ", fg_color="transparent", font=("Helvetica", 20))
    spacerLabel1.pack(pady=6, padx=0)

    youtubeFieldLabel = customtkinter.CTkLabel(mainFrameL, text="YouTube Channel", fg_color="transparent", font=("Helvetica", 20))
    youtubeFieldLabel.pack(pady=6, padx=10)
    youtubeField = customtkinter.CTkEntry(mainFrameL, placeholder_text="Link to YouTube Channel", width=250)
    youtubeField.pack(pady=0, padx=10)
    youtubeField.insert(0, linkData.loc[linkData.Platform == 'YouTube']['Link'].values[0])

    spacerLabel2 = customtkinter.CTkLabel(mainFrameL, text=" ", fg_color="transparent", font=("Helvetica", 20))
    spacerLabel2.pack(pady=6, padx=0)

    spotifyFieldLabel = customtkinter.CTkLabel(mainFrameL, text="Spotify Artist Page", fg_color="transparent", font=("Helvetica", 20))
    spotifyFieldLabel.pack(pady=6, padx=10)
    spotifyField = customtkinter.CTkEntry(mainFrameL, placeholder_text="Link to Spotify Artist Page", width=250)
    spotifyField.pack(pady=0, padx=10)
    spotifyField.insert(0, linkData.loc[linkData.Platform == 'Spotify']['Link'].values[0])

    spacerLabel3 = customtkinter.CTkLabel(mainFrameL, text=" ", fg_color="transparent", font=("Helvetica", 20))
    spacerLabel3.pack(pady=6, padx=0)

    appleFieldLabel = customtkinter.CTkLabel(mainFrameL, text="Apple Artist Page", fg_color="transparent", font=("Helvetica", 20))
    appleFieldLabel.pack(pady=6, padx=10)
    appleField = customtkinter.CTkEntry(mainFrameL, placeholder_text="Link to Apple Music Artist Page", width=250)
    appleField.pack(pady=0, padx=10)
    appleField.insert(0, linkData.loc[linkData.Platform == 'Apple Music']['Link'].values[0])

    submitButton = customtkinter.CTkButton(mainFrameL, text="Refresh", command=refresh, width=250)
    submitButton.pack(pady=48, padx=10)

    ### RIGHT GRAPH FRAME ###
    mainFrameR = customtkinter.CTkFrame(master=app, width=3*windowWidth/4 - 3*pad, height=windowHeight-2*pad)
    mainFrameR.grid(row=1, column=2, pady=pad, padx=0)
    mainFrameR.grid_propagate(0)

    ## SubFrames for 4 Graphs ##

    # Top left frame
    subframeTL = customtkinter.CTkFrame(master=mainFrameR, width=(3*windowWidth/4 - 6*pad) / 2, height=(windowHeight-5*pad) / 2)
    subframeTL.grid(row=1, column=1, pady=pad, padx=pad)
    canvas = FigureCanvasTkAgg(graphs.igGraph(), master=subframeTL)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.0, rely=0.0)

    # Top right frame
    subframeTR = customtkinter.CTkFrame(master=mainFrameR, width=(3*windowWidth/4 - 6*pad) / 2, height=(windowHeight-5*pad) / 2)
    subframeTR.grid(row=1, column=2, pady=pad, padx=0)

    # Bottom left frame
    subframeBL = customtkinter.CTkFrame(master=mainFrameR, width=(3*windowWidth/4 - 6*pad) / 2, height=(windowHeight-5*pad) / 2)
    subframeBL.grid(row=2, column=1, pady=0, padx=pad)

    # Bottom right frame
    subframeBR = customtkinter.CTkFrame(master=mainFrameR, width=(3*windowWidth/4 - 6*pad) / 2, height=(windowHeight-5*pad) / 2)
    subframeBR.grid(row=2, column=2, pady=0, padx=0)

    app.mainloop()

    

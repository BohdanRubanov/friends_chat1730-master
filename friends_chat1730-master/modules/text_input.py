import customtkinter as ctk
import modules.screen_app as m_app

width_input = 400
height_input = 50
width_search = 128
height_search = 50

font_size = ctk.CTkFont(
    family= "Arial",
    size= 20,
    weight= "bold"
)

text = ctk.StringVar()
text_search = ctk.StringVar()

text_input = ctk.CTkEntry(
    master= m_app.main_app.FRAME1,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text
)

text_input.place(relx = 0.413, rely = 0.935, anchor = ctk.CENTER)

text_search = ctk.CTkEntry(
    master= m_app.main_app.FRAME2,
    width= width_search,
    height= height_search,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text_search
)

text_search.place(relx = 0.5, rely = 0.12, anchor = ctk.CENTER)
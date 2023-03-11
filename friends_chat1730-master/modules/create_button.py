import customtkinter as ctk
import modules.screen_app as m_app
# import modules.create_frame as m_frame
font_size = ctk.CTkFont(
    family= "Arial",
    size= 25,
    weight= "bold"
)
font_size_status = ctk.CTkFont(
    family= "Arial",
    size= 15,
    weight= "bold"
)
def set_name(text, status_text, status_color, offline = None):
    x = 0.1
    if offline:
        x = 0.18
    # print(1111)
    button_label = ctk.CTkLabel(
        master = m_app.main_app.FRAME3, 
        text = text,
        font = font_size
    )
    button_label.place(relx = 0.1, rely = 0.3, anchor = ctk.CENTER)
    button_label_status = ctk.CTkLabel(
        master = m_app.main_app.FRAME3, 
        text = status_text,
        font = font_size_status,
        fg_color=None,
        text_color= status_color
    )
    
    button_label_status.place(relx = x, rely = 0.7, anchor = ctk.CENTER)
# 
def create_button(master, text, width = 120, height= 50, corner_radius = 5):
    button = ctk.CTkButton(master = master,
                           width = width,
                           height = height,
                           corner_radius = corner_radius,
                           text = text,
                           fg_color = "blue"
    )
    return button

bt1 = create_button(master=m_app.main_app.FRAME,
                    text='Чати'
                )
bt1.place(relx = 0.02, rely= 0.11, anchor=ctk.NW)

bt2 = create_button(master = m_app.main_app.FRAME,
                    text = "Контакти"
                )
bt2.place(relx = 0.02, rely=0.2, anchor=ctk.NW)

bt3 = create_button(master = m_app.main_app.FRAME,
                    text = "Налаштування"   
                )
bt3.place(relx = 0.02, rely = 0.29, anchor = ctk.NW)

chat_button = ctk.CTkButton(
    master = m_app.main_app.FRAME2, 
    text ="Микола",
    width = 128,
    height = 50,
    fg_color = "blue",
    command= lambda: set_name("Микола", "У мережі", "blue")
)
chat_button.place(relx = 0.5, rely = 0.21, anchor = ctk.CENTER)
chat_button1 = ctk.CTkButton(
    master = m_app.main_app.FRAME2, 
    text ="Богдан",
    width = 128,
    height = 50,
    fg_color = "blue",
    command= lambda: set_name("Богдан", "Був 4 хвилини тому", "grey", offline = 1)
)
chat_button1.place(relx = 0.5, rely = 0.3, anchor = ctk.CENTER)
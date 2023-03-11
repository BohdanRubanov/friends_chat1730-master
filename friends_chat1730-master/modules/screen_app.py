import customtkinter
import modules.create_frame as m_frame


class App(customtkinter.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        #
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.resizable(False, False)
        self.title("Головне вікно програми")
        self.FRAME = m_frame.My_Frame(master = self, width= 130, height= app_height - 20, border_width= 5)
        self.FRAME1 = m_frame.My_Frame(master = self, width= 500, height= app_height - 90, border_width= 5)
        self.FRAME2 = m_frame.My_Frame(master = self, width= 150, height= app_height - 20, border_width= 5)
        self.FRAME3 = m_frame.My_Frame(master = self, width= 500, height= 70, border_width= 5)
        # self.FRAME = customtkinter.CTkFrame(master=self, width=300, height= app_height)
        
        self.FRAME.place(relx = 0.01, rely = 0.02, anchor = customtkinter.NW)
        self.FRAME1.place(relx = 0.3605, rely = 0.137, anchor = customtkinter.NW)
        self.FRAME3.place(relx = 0.3605, rely = 0.02, anchor = customtkinter.NW)
        self.FRAME2.place(relx = 0.173, rely = 0.02, anchor = customtkinter.NW)
        # self.FRAME.pack(padx= 10, pady = 10, expand = True)
        # self.FRAME.place(relx = 0, rely= 0)

main_app = App(800, 600)
font_size = customtkinter.CTkFont(
    family= "Arial",
    size= 20,
    weight= "bold"
)
button_label = customtkinter.CTkLabel(main_app.FRAME, text="Friendly", font = font_size)
button_label1 = customtkinter.CTkLabel(main_app.FRAME, text="Chat", font = font_size)
button_label2 = customtkinter.CTkLabel(main_app.FRAME2, text="Чати", font = font_size)
button_label.place(relx = 0.05, rely = 0.02, anchor = customtkinter.NW)
button_label1.place(relx = 0.55, rely = 0.065, anchor = customtkinter.NW)
button_label2.place(relx = 0.35, rely = 0.02, anchor = customtkinter.NW)
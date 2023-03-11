import customtkinter as ctk
import modules.screen_app as m_app
import modules.text_input as m_input
import modules.text_frame as m_form
button_width = 85
button_height = 50
margin_left = 50
button_color = "blue"
message_y = 20
counter = 1

def send_message():
    global message_y
    global counter

    if counter == 2:
        msg_frame = m_form.MessageFrame(text= m_input.text.get(), font= m_input.font_size, username= "Микола", master= m_app.main_app.FRAME1, width= 200, height= 60, border_width= 3)
        msg_frame.place_left()
        msg_frame.place(x=10,y=message_y)
        message_y += 60
        counter = 1
    else:
        msg_frame = m_form.MessageFrame(text= m_input.text.get(), font= m_input.font_size, username= "Дмитро", master= m_app.main_app.FRAME1, width= 200, height= 60, border_width= 3)
        msg_frame.place_right()
        msg_frame.place(x=288,y=message_y)
        message_y += 60
        counter = 2

send_button = ctk.CTkButton(
    master = m_app.main_app.FRAME1, 
    text ="->",
    width = button_width,
    height = button_height,
    fg_color = button_color,
    command= send_message
)

send_button.place(
    relx = 0.899, rely = 0.935,
    anchor = ctk.CENTER
)



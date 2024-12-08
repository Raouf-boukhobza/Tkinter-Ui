import customtkinter as ctk


def create_entry(window , text , textVariable):
    
    #create the frame of the weidget
    frame = ctk.CTkFrame(window  , width=500 , fg_color="white" )
    bold_font = ctk.CTkFont(family="Courier New", size=18, weight="bold")
    label = ctk.CTkLabel(frame , text=text , bg_color="white" , text_color="#565656", anchor='w', font=bold_font)
    label.pack( fill = 'x' , padx =6)
    entry = ctk.CTkEntry(frame , textvariable=textVariable, height=20, bg_color="white"  , border_width=0 , font=("Courier New" , 16)  )
    entry.pack(fill = 'x' , pady = 5)
      # Create a separator for the horizontal line at the bottom
    separator = ctk.CTkFrame(frame, height=3, fg_color="#7393B3")
    separator.pack(padx = 6)
    return frame


    
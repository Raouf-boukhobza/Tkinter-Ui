import customtkinter as ctk
from PIL import Image


def create_entry(window , text , textVariable):
    #create the frame of the weidget
    frame = ctk.CTkFrame(window  , width=500 , fg_color="white" )
    bold_font = ctk.CTkFont(family="Courier New", size=18, weight="bold")
    label = ctk.CTkLabel(frame , text=text , bg_color="white" , text_color="#808080", anchor='w', font=bold_font)
    label.pack( fill = 'x' , padx =6)
    entry = ctk.CTkEntry(frame , textvariable=textVariable, height=20, bg_color="white"  , border_width=0 , font=("Courier New" , 16)  )
    entry.pack(fill = 'x' , pady = 5)
      # Create a separator for the horizontal line at the bottom
    separator = ctk.CTkFrame(frame, height=3, fg_color="#7393B3")
    separator.pack(padx = 6)
    return frame
  
  
def create_lable(window):
  frame = ctk.CTkFrame(master=window , fg_color="white")
  #display the image 
  image = ctk.CTkImage(Image.open("images1.png"), size=(40, 40))
  image_label = ctk.CTkLabel(master=frame, image=image, text="")
  image_label.pack(side  ='left' , padx = 10 )
  
  #display the text 
  title_label = ctk.CTkLabel(master=frame, text="Registration Form", text_color="#5D3FD3" , font=("Courier New", 40, "bold"))
  title_label.pack(side = "left")
  return frame




def create_list(list_option , window , textvar  , text , textOption) :
  frame = ctk.CTkFrame(window  , width=500 , fg_color="white" )
  bold_font = ctk.CTkFont(family="Courier New", size=18, weight="bold")
  label = ctk.CTkLabel(frame , text=text , bg_color="white" , text_color="#808080", anchor='w', font=bold_font)
  label.pack( fill = 'x' , padx =6)
  # Define a function to capture the selected value
  def on_select(choice):
     textvar = choice
     print(choice)

  frame1 = ctk.CTkFrame(frame  , width=500 , fg_color="white" , border_width=1 , border_color="red" )
  # Create a modern drop-down menu
  options = list_option
  dropdown = ctk.CTkOptionMenu(
    master=frame1, 
    values=options, 
    command=on_select,  
    width=200,
    height=35,
    font=("Arial", 16 ),
    text_color="grey",
    bg_color="#7393B3" ,
    fg_color="White", 
    corner_radius=0,
  
    button_color="#5D3FD3", 
    button_hover_color="#372C84"
 )
# Set the default value
  dropdown.set(textOption)
  
  dropdown.pack()
  frame1.pack(fill = 'x' , pady = 5 )
  
  return frame



  

 
  
  
  


    
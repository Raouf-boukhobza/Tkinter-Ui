import customtkinter as ctk
from db_connectino import create_connection as connect_to_db
import pymysql
from widgets import *
from PIL import Image
from tkinter import messagebox
import pillow_avif

# Insert data into the database
def insert_data():
    name = entry_name.get()
    prenom = entry_prenom.get()
    email = entry_email.get()
    numero_telephone = entry_numero_telephone.get()
    date_naissance = entry_date_naissance.get()
    nin = entry_nin.get()  
    ville = entry_ville.get()
    commune = entry_commune.get()
    type_appartement = entry_type.get()
    
    
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = "INSERT INTO users (nom , prenom , email , NumeroDeTelephone ,dateDeNaissance , NIN, ville , commenu , type) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s )"
            cursor.execute(query, (name, prenom, email ,numero_telephone,date_naissance, nin, ville ,commune, type_appartement))
            conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except pymysql.MySQLError as e :
            messagebox.showerror("Insert Error", f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


window  =ctk.CTk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("1400x750")





window.configure(fg_color="white")
entry_name = ctk.StringVar()
entry_prenom = ctk.StringVar()
entry_email = ctk.StringVar()
entry_numero_telephone= ctk.StringVar()
entry_nin = ctk.StringVar()
entry_ville = ctk.StringVar()
entry_date_naissance= ctk.StringVar()
entry_commune = ctk.StringVar()
entry_type= ctk.StringVar()
#display the image 

inputs_frame = ctk.CTkFrame(window  , width=750 , fg_color="white" )
create_lable(window=inputs_frame , text="Regestration Form" , image="images1.png").grid(row = 0 , column =0 , columnspan =2, pady = (10 , 20) ,padx = (0 , 100) )
create_entry(window=inputs_frame , text="Nom : " , textVariable=entry_name).grid(row =1 , column = 0 , pady = 20 )
create_entry(window=inputs_frame , text="Prénom : " , textVariable=entry_prenom).grid(row =2 , column = 0 , pady =20)
create_entry(window=inputs_frame , text="N°Téléphone: " , textVariable=entry_numero_telephone).grid(row =3 , column = 0 , pady  =20 )
create_entry(window=inputs_frame , text="Email : " , textVariable=entry_email).grid(row =4 , column = 0  , pady = 20)
create_entry(window=inputs_frame , text="NIN : " , textVariable=entry_nin).grid(row =1 , column = 1 , pady = 20  , padx =(75 ,0) )
create_entry(window=inputs_frame , text="Date Naissance : " , textVariable=entry_date_naissance).grid(row =2 , column = 1 , pady = 20 , padx =(75 , 0))
create_list(window=inputs_frame , text="Ville : ", textOption="choisie la ville", textvar=entry_ville, list_option=["jijel" , "oran" , "setif"]).grid(row = 3 , column = 1 , padx = (75 , 0) )
create_entry(window=inputs_frame , text="Commune : " , textVariable=entry_commune).grid(row =4 , column = 1 , pady = 20, padx =(75 , 0))
create_list(window=inputs_frame , text="Type : ",  textvar=entry_type ,textOption="choisie le type " , list_option=["f3" , "f2" , "f4"]).grid(row = 5 , column = 0 )
button = ctk.CTkButton(master=inputs_frame , fg_color="#5D3FD3" , command= insert_data , text="Submit" ,text_color="white", height=40,width=200)
button.grid(row = 5 , column = 1 , padx = (75 , 0) , pady = (15 , 0))
inputs_frame.pack( side='left', padx =100,pady = 50 , fill = 'both')

  #display the image 
image = ctk.CTkImage(Image.open("lastt.jpg"), size=(700, 700)  )
image_label = ctk.CTkLabel(master=window,corner_radius=50 ,image=image, text="")
image_label.pack(side  ='left'  , fill = "both", padx = 20 , pady = 10 )




window.mainloop()
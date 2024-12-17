import customtkinter as ctk
from tkinter import Canvas, Scrollbar
from db_connectino import create_connection as connect_to_db
from tkinter import messagebox
from widgets import create_entry, create_list, create_lable

def display_result(row):
    result_card = ctk.CTkFrame(
        scrollable_frame,  # Use the scrollable frame for displaying results
        fg_color="white",
        corner_radius=15,
        height=150,

        border_width=2,
        border_color="#5D3FD3"
    )
    result_card.pack(padx=20, pady=15, fill="x")

    fields = ["ID", "Nom", "Email", "Prénom", "Date de Naissance", "Téléphone", "NIN", "Ville", "Commune", "Type"]
    for i, value in enumerate(row):
        field_label = ctk.CTkLabel(
            result_card,
            text=f"{fields[i]}:",
            text_color="#5D3FD3",
            font=("Arial", 14, "bold")
        )
        field_label.grid(row=i//3, column=(i%3)*2, sticky="w", padx=(20, 10), pady=5)
        value_label = ctk.CTkLabel(
            result_card,
            text=f"{value}",
            text_color="#333333",
            font=("Arial", 14)
        )
        value_label.grid(row=i//3, column=(i%3)*2+1, sticky="w", padx=(0, 20), pady=5)

def search_data():
    ville = entry_ville.get()
    commune = entry_commune.get()
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM users WHERE ville = %s AND commenu = %s"
            cursor.execute(query, (ville, commune))
            rows = cursor.fetchall()

            # Clear previous results
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            if rows:
                for row in rows:
                    display_result(row)
            else:
                messagebox.showinfo("No Results", "No records found for the specified criteria.")
        except conn.Error as e:
            messagebox.showerror("Search Error", f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Create the search window
search_window = ctk.CTk()
search_window.geometry("1200x700")
search_window.title("Search Form")
search_window.configure(fg_color="#F0F0F0")

entry_ville = ctk.StringVar()
entry_commune = ctk.StringVar()

# Input Frame
inputs_frame = ctk.CTkFrame(
    search_window,
    width=1400,
    fg_color="white",
    border_width=2,
    border_color="#D4D4D4",
    corner_radius=10
)
create_lable(window=inputs_frame , text="search Form" , image="download.png").grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=(100, 100))

create_list(
    window=inputs_frame,
    text="Ville:",
    textOption="Choisissez la ville",
    textvar=entry_ville,
    list_option=["jijel", "oran", "setif"]
).grid(row=1, column=0, pady=20)

create_entry(
    window=inputs_frame,
    text="Commune:",
    textVariable=entry_commune
).grid(row=1, column=1, pady=20, padx=(75, 0))

search_button = ctk.CTkButton(
    master=inputs_frame,
    fg_color="#5D3FD3",
    hover_color="#4C2DAF",
    text="Rechercher",
    text_color="white",
    height=50,
    width=300,
    font=("Arial", 18, "bold"),
    command=search_data
)
search_button.grid(row=2, column=0, columnspan=2, pady=(15,50))

inputs_frame.pack(pady=50)

# Scrollable Results Frame
container_frame = ctk.CTkFrame(
    search_window,
    width=1200,
    fg_color="white",
    border_width=2,
    border_color="#D4D4D4",
    corner_radius=10
)
container_frame.pack(pady=20, fill="both", expand=True)

canvas = Canvas(container_frame, bg="white", highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(container_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

scrollable_frame = ctk.CTkFrame(canvas, fg_color="white")
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

search_window.mainloop()

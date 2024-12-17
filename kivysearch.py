from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
import pymysql
from db_connectino import create_connection as connect_to_db


# Function to fetch data from the database based on Ville and Commune
def search_data(ville, commune):
    results = []
    try:
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            query = "SELECT nom, prenom, email, NumeroDeTelephone FROM users WHERE ville=%s AND commenu=%s"
            cursor.execute(query, (ville, commune))
            results = cursor.fetchall()
        else:
            print("Database connection failed.")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return results


# Function to insert data into the database
def insert_data(data):
    try:
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            query = """
            INSERT INTO users (nom, prenom, email, NumeroDeTelephone, dateDeNaissance, NIN, ville, commenu, type) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, data)
            conn.commit()
            print("Data inserted successfully!")
        else:
            print("Database connection failed.")
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# The main Kivy Layout
class RegistrationForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="horizontal", spacing=20, padding=20, **kwargs)
        self.size_hint = (1, 1)

        # --- Left Side: Form Entries ---
        left_layout = BoxLayout(orientation="vertical", spacing=10)
        self.labels = [
            "Nom", "Prénom", "N°Téléphone", "Email", "NIN", "Date Naissance", "Commune", "Ville", "Type"
        ]
        
        self.inputs = {}
        form_layout = GridLayout(cols=2, spacing=10, size_hint=(0.7, None))
        form_layout.bind(minimum_height=form_layout.setter('height'))

        # Create Input Fields
        for label in self.labels:
            form_layout.add_widget(Label(text=f"{label}:", font_size=18, color=(0.5, 0.5, 0.5, 1)))
            if label in ["Ville", "Type"]:
                spinner = Spinner(
                    text="Select Option",
                    values=["jijel", "oran", "setif"] if label == "Ville" else ["f3", "f2", "f4"],
                    size_hint=(1, None),
                    height=40
                )
                self.inputs[label] = spinner
                form_layout.add_widget(spinner)
            else:
                text_input = TextInput(size_hint=(1, None), height=40)
                self.inputs[label] = text_input
                form_layout.add_widget(text_input)

        # Submit Button
        submit_button = Button(
            text="Submit",
            size_hint=(0.5, None),
            height=50,
            background_color=(0.36, 0.24, 0.83, 1),
            color=(1, 1, 1, 1)
        )
        submit_button.bind(on_press=self.submit_form)

        # Search Section: Ville and Commune
        search_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=50, spacing=10)

        self.ville_spinner = Spinner(
            text="Select Ville",
            values=["jijel", "oran", "setif"],
            size_hint=(0.5, None),
            height=40
        )
        self.commune_input = TextInput(
            hint_text="Enter Commune",
            size_hint=(0.5, None),
            height=40,
            multiline=False
)
        search_button = Button(
            text="Search",
            size_hint=(0.3, None),
            height=40,
            background_color=(0.36, 0.24, 0.83, 1),
            color=(1, 1, 1, 1)
        )
        search_button.bind(on_press=self.search_form)

        search_layout.add_widget(self.ville_spinner)
        search_layout.add_widget(self.commune_input)
        search_layout.add_widget(search_button)

        # Add Form to Left Layout
        left_layout.add_widget(Label(text="Registration Form", font_size=30, color=(0.36, 0.24, 0.83, 1)))
        left_layout.add_widget(search_layout)
        left_layout.add_widget(form_layout)
        left_layout.add_widget(submit_button)

        # --- Right Side: Image Display ---
        right_layout = BoxLayout(size_hint=(0.5, 1))
        image = Image(source="lastt.jpg", size_hint=(1, 1))
        right_layout.add_widget(image)

        # Add to Main Layout
        self.add_widget(left_layout)
        self.add_widget(right_layout)

    def submit_form(self, instance):
        # Collect data from inputs
        data = [
            self.inputs["Nom"].text,
            self.inputs["Prénom"].text,
            self.inputs["Email"].text,
            self.inputs["N°Téléphone"].text,
            self.inputs["Date Naissance"].text,
            self.inputs["NIN"].text,
            self.inputs["Ville"].text,
            self.inputs["Commune"].text,
            self.inputs["Type"].text
        ]
        print("Submitting Form Data:", data)
        insert_data(data)

    def search_form(self, instance):
        ville = self.ville_spinner.text
        commune = self.commune_input.text
        if ville != "Select Ville" and commune != "Select Commune":
            results = search_data(ville, commune)
            content = BoxLayout(orientation="vertical", padding=10, spacing=10)
            if results:
                for result in results:
                    content.add_widget(Label(text=f"{result[0]} {result[1]} - {result[2]} - {result[3]}", font_size=16))
            else:
                content.add_widget(Label(text="No results found.", font_size=16, color=(1, 0, 0, 1)))

            close_button = Button(text="Close", size_hint=(1, None), height=40)
            popup = Popup(title="Search Results", content=content, size_hint=(0.8, 0.5))
            close_button.bind(on_press=popup.dismiss)
            content.add_widget(close_button)
            popup.open()
        else:
            print("Please select both Ville and Commune.")


class RegistrationApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return RegistrationForm()


if __name__ == "__main__":
    RegistrationApp().run()

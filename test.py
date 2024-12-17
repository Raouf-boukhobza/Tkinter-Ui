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
import pymysql
from db_connectino import create_connection as connect_to_db


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

        # Add Form to Left Layout
        left_layout.add_widget(Label(text="Registration Form", font_size=30, color=(0.36, 0.24, 0.83, 1)))
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


class RegistrationApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return RegistrationForm()


if __name__ == "__main__":
    RegistrationApp().run()

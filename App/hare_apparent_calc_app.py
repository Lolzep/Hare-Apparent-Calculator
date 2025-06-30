# main.py
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.core.window import Window

# Set a background color for the app window
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class HareApparentCalculator(App):

    def build(self):
        # --- Main Layout ---
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # --- Input Section ---
        input_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=270)
        
        # Define input fields and store them as instance variables
        self.apparents_input = TextInput(multiline=False, input_type='number', hint_text='e.g., 1')
        self.total_input = TextInput(multiline=False, input_type='number', hint_text='e.g., 1')
        self.flicker_input = TextInput(multiline=False, input_type='number', hint_text='e.g., 1')
        self.hare_repeats_input = TextInput(multiline=False, input_type='number', hint_text='e.g., 0')
        self.preston_repeats_input = TextInput(multiline=False, input_type='number', hint_text='e.g., 0')
        self.preston_switch = Switch(active=False)

        # Add labels and widgets to the input grid
        input_grid.add_widget(Label(text='Non-Token Hares to Flicker:'))
        input_grid.add_widget(self.apparents_input)
        input_grid.add_widget(Label(text='Total Hares in Play:'))
        input_grid.add_widget(self.total_input)
        input_grid.add_widget(Label(text='Times to Flicker:'))
        input_grid.add_widget(self.flicker_input)
        input_grid.add_widget(Label(text='Hare Apparent Repeat Triggers:'))
        input_grid.add_widget(self.hare_repeats_input)
        input_grid.add_widget(Label(text='Preston Repeat Triggers:'))
        input_grid.add_widget(self.preston_repeats_input)
        input_grid.add_widget(Label(text='Is Preston in Play?'))
        input_grid.add_widget(self.preston_switch)

        self.root.add_widget(input_grid)

        # --- Calculate Button ---
        calc_button = Button(text='Calculate', size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.8, 1))
        calc_button.bind(on_press=self.calculate_triggers)
        self.root.add_widget(calc_button)

        # --- Results Section ---
        self.status_label = Label(text='Enter values and press calculate.', size_hint_y=None, height=40)
        self.root.add_widget(self.status_label)

        results_grid = GridLayout(cols=3, size_hint_y=None, height=40)
        self.rabbits_label = Label(text='Rabbits: 0')
        self.copies_label = Label(text='Copies: 0')
        self.etbs_label = Label(text='ETBs: 0')
        results_grid.add_widget(self.rabbits_label)
        results_grid.add_widget(self.copies_label)
        results_grid.add_widget(self.etbs_label)
        self.root.add_widget(results_grid)

        # --- Log Section (Scrollable) ---
        log_header = Label(text='Trigger Log', size_hint_y=None, height=30, font_size='18sp')
        self.root.add_widget(log_header)
        
        # The grid for the log content
        self.log_grid = GridLayout(cols=5, spacing=5, size_hint_y=None)
        self.log_grid.bind(minimum_height=self.log_grid.setter('height')) # Allows scrolling
        
        # Add headers to the log grid
        headers = ["Flicker", "Repeat", "Source", "Buns/Copies", "Math"]
        for header in headers:
            self.log_grid.add_widget(Label(text=header, bold=True, size_hint_y=None, height=40))

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.log_grid)
        self.root.add_widget(scroll_view)

        return self.root

    def calculate_triggers(self, instance):
        # Clear previous results and log
        self.log_grid.clear_widgets()
        headers = ["Flicker", "Repeat", "Source", "Buns/Copies", "Math"]
        for header in headers:
            self.log_grid.add_widget(Label(text=header, bold=True, size_hint_y=None, height=40))

        # --- 1. Get and Validate Inputs ---
        try:
            apparents_start = int(self.apparents_input.text)
            total = int(self.total_input.text)
            flicker = int(self.flicker_input.text)
            hare_repeats = int(self.hare_repeats_input.text)
            preston_repeats = int(self.preston_repeats_input.text)
            preston = self.preston_switch.active
            
            if apparents_start < 0 or total < 0 or flicker < 0 or hare_repeats < 0 or preston_repeats < 0:
                raise ValueError("Negative numbers are not allowed.")
            
            if apparents_start > total:
                raise ValueError("Hares to flicker cannot exceed total hares.")

        except ValueError as e:
            self.status_label.text = f"Invalid Input: {e}"
            return

        self.status_label.text = "Calculation complete."
        
        # --- 2. Core Calculation Logic (from original script) ---
        # make all lists, each is a column in the final log table
        log_rows = []

        # Initial values
        rabbits = 0
        copies = 0
        etbs = 0
        
        apparents = apparents_start
        illusions = total - apparents
        real_apparents = apparents_start

        # Flicker X amount of times
        for i in range(flicker):
            # ETB trigger from flicker
            etbs += real_apparents
            log_rows.append((f"Flicker {i+1}", "Original", "HA ETBs", f"{real_apparents} ETBs", f"{real_apparents}"))

            # Hare Apparent's own trigger
            for j in range(hare_repeats + 1):
                c_rabbits = real_apparents * (apparents + illusions - 1)
                rabbits += c_rabbits
                etbs += c_rabbits
                log_rows.append((f"Flicker {i+1}", f"Repeat {j}" if j > 0 else "Original", "HAs", f"{c_rabbits} Buns", f"{real_apparents}*({apparents}+{illusions}-1)"))

            # Preston's trigger (if applicable)
            c_copies = 0
            if preston:
                for k in range(preston_repeats + 1):
                    c_copies_instance = apparents_start
                    copies += c_copies_instance
                    etbs += c_copies_instance
                    log_rows.append((f"Flicker {i+1}", f"Repeat {k}" if k > 0 else "Original", "Preston", f"{c_copies_instance} Copies", f"{apparents_start}"))
                
                    # New copies from Preston also trigger Hares
                    apparents += c_copies_instance # This line is a simplification. The logic could be very complex depending on stack order.
                                        # Assuming all preston copies are made before their ETBs are resolved.
                for j in range(hare_repeats + 1):
                    new_rabbits_from_copies = (c_copies_instance * (apparents + illusions - 1))
                    rabbits += new_rabbits_from_copies
                    etbs += new_rabbits_from_copies
                    log_rows.append((f"Flicker {i+1}", f"Repeat {j}" if j > 0 else "Original", "Copies ETB", f"{new_rabbits_from_copies} Buns", f"{c_copies_instance}*({apparents}+{illusions}-1)"))


        # --- 3. Update UI with Results ---
        self.rabbits_label.text = f"Rabbits: {rabbits}"
        self.copies_label.text = f"Copies: {copies}"
        self.etbs_label.text = f"ETBs: {etbs}"
        
        for row_data in log_rows:
            for item in row_data:
                self.log_grid.add_widget(Label(text=str(item), size_hint_y=None, height=30))


if __name__ == '__main__':
    HareApparentCalculator().run()
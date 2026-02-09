import customtkinter as ctk

# Set the initial appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CustomTkinterDemo(ctk.CTk):
    """
    A comprehensive demo class to showcase various customtkinter widgets and features.
    """

    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("CustomTkinter Comprehensive Demo")
        self.geometry("1100x680")
        
        # Configure main grid layout (4 columns)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # --- Sidebar Frame (left) ---
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Sidebar", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Appearance mode control
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                               command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))

        # Color theme control
        self.theme_label = ctk.CTkLabel(self.sidebar_frame, text="Color Theme:", anchor="w")
        self.theme_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.theme_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["blue", "green", "dark-blue"],
                                                  command=self.change_theme_event)
        self.theme_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # --- Main Frame (right) ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, rowspan=4, columnspan=3, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(3, weight=1)

        self.main_label = ctk.CTkLabel(self.main_frame, text="CustomTkinter Widget Showcase", font=ctk.CTkFont(size=24, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # --- Button Frame ---
        self.button_frame = ctk.CTkFrame(self.main_frame)
        self.button_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)

        self.button_1 = ctk.CTkButton(self.button_frame, text="Normal Button", command=lambda: print("Button 1 clicked"))
        self.button_1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.button_2 = ctk.CTkButton(self.button_frame, text="Disabled", state="disabled")
        self.button_2.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.button_3 = ctk.CTkButton(self.button_frame, text="Custom Color", fg_color="red", hover_color="darkred")
        self.button_3.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # --- Checkbox and Switch Frame ---
        self.toggle_frame = ctk.CTkFrame(self.main_frame)
        self.toggle_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.toggle_frame.grid_columnconfigure(0, weight=1)
        self.toggle_frame.grid_columnconfigure(1, weight=1)
        
        self.checkbox_1 = ctk.CTkCheckBox(self.toggle_frame, text="Checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=10)

        self.checkbox_2 = ctk.CTkCheckBox(self.toggle_frame, text="Checkbox 2", corner_radius=5)
        self.checkbox_2.grid(row=0, column=1, padx=10, pady=10)

        self.switch_1 = ctk.CTkSwitch(self.toggle_frame, text="Switch")
        self.switch_1.grid(row=1, column=0, padx=10, pady=10)

        # --- Entry, Combobox, and OptionMenu Frame ---
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=1)
        self.input_frame.grid_columnconfigure(2, weight=1)

        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="CTkEntry")
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.combobox = ctk.CTkComboBox(self.input_frame, values=["Option 1", "Option 2", "Option 3"])
        self.combobox.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.optionmenu = ctk.CTkOptionMenu(self.input_frame, values=["Light", "Dark", "System"])
        self.optionmenu.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # --- Slider, ProgressBar, and Radiobuttons ---
        self.progress_frame = ctk.CTkFrame(self.main_frame)
        self.progress_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        self.progress_frame.grid_columnconfigure(0, weight=1)
        self.progress_frame.grid_columnconfigure(1, weight=1)
      

        self.slider = ctk.CTkSlider(self.progress_frame, from_=0, to=100, command=self.slider_event)
        self.slider.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="ew")

        self.progressbar = ctk.CTkProgressBar(self.progress_frame, orientation="horizontal")
        self.progressbar.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="ew")
        self.progressbar.set(0)

        # Radiobuttons
        self.radiobutton_frame = ctk.CTkFrame(self.main_frame)
        self.radiobutton_frame.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        self.radiobutton_var = ctk.IntVar(value=1)
        self.radiobutton_1 = ctk.CTkRadioButton(self.radiobutton_frame, text="Radiobutton 1", variable=self.radiobutton_var, value=1)
        self.radiobutton_2 = ctk.CTkRadioButton(self.radiobutton_frame, text="Radiobutton 2", variable=self.radiobutton_var, value=2)
        self.radiobutton_1.pack(side="left", padx=10, pady=10)
        self.radiobutton_2.pack(side="left", padx=10, pady=10)


        # --- Textbox and Scrollable Frame ---
        self.text_frame = ctk.CTkFrame(self.main_frame)
        self.text_frame.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")
        self.text_frame.grid_columnconfigure(0, weight=1)
        self.text_frame.grid_rowconfigure(0, weight=1)
        
        self.textbox = ctk.CTkTextbox(self.text_frame, wrap="word", width=400)
        self.textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.textbox.insert("end", "This is a CTkTextbox.\n\nYou can insert multiline text here.\n")
        self.textbox.insert("end", "\nFeel free to type in it.")


        # --- Functions for interaction ---
    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Changes the entire application's theme (light/dark/system)."""
        ctk.set_appearance_mode(new_appearance_mode)

    def change_theme_event(self, new_theme: str):
        """Changes the default color theme for the entire application."""
        ctk.set_default_color_theme(new_theme)

    def slider_event(self, value: float):
        """Updates the progress bar when the slider is moved."""
        self.progressbar.set(value / 100)

import customtkinter as ctk

class ToplevelWindow(ctk.CTkToplevel):
    """
    A simple example of a top-level (pop-up) window.
    It can communicate back to its parent window.
    """
    def __init__(self, master=None):
        super().__init__(master=master)
        
        self.title("Toplevel Window")
        self.geometry("300x200")
        
        # Set a protocol handler for when the user clicks the 'x' button
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # A label to show this is a separate window
        self.label = ctk.CTkLabel(self, text="This is the Toplevel Window!", font=("Arial", 16))
        self.label.pack(pady=20, padx=20)

        # Button to close the Toplevel window
        self.close_button = ctk.CTkButton(self, text="Close", command=self.on_closing)
        self.close_button.pack(pady=10)

        # Button to update a widget in the main window
        self.update_button = ctk.CTkButton(self, text="Update Main Window", command=self.update_main_label)
        self.update_button.pack(pady=10)

        # Keep the Toplevel window on top of the main window
        self.grab_set()

    def update_main_label(self):
        """
        Updates the label in the master (main) window.
        self.master is the reference to the MainApp instance passed in __init__.
        """
        self.master.main_label.configure(text="Label updated from Toplevel window!")

    def on_closing(self):
        """
        Custom close function to un-grab the window and destroy it.
        """
        self.grab_release()
        self.destroy()

class MainApp(ctk.CTk):
    """
    The main application window.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Main Application")
        self.geometry("500x300")
        
        # A label to be updated by the Toplevel window
        self.main_label = ctk.CTkLabel(self, text="Hello! Click the button to open a new window.", font=("Arial", 16))
        self.main_label.pack(pady=20, padx=20)
        
        # Button to open the Toplevel window
        self.open_button = ctk.CTkButton(self, text="Open Toplevel Window", command=self.open_toplevel_window)
        self.open_button.pack(pady=10)
        
        # A variable to hold the reference to the Toplevel window
        # This prevents it from being garbage collected
        self.toplevel_window = None

    def open_toplevel_window(self):
        """
        Creates and shows the Toplevel window.
        Checks if a Toplevel window is already open.
        """
        # Prevents opening multiple Toplevel windows
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            
        else:
            self.toplevel_window.focus() # If window already exists, focus on it


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()


if __name__ == "__main__2":
    app = CustomTkinterDemo()
    app.mainloop()
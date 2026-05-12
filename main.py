import tkinter as tk
import utils


class App:
    def __init__(self):

        # Create actual Tk window
        self.main_window = tk.Tk()

        # Window size and position
        self.main_window.geometry("1200x520+350+100")

        # Login button
        self.login_button_main_window = utils.get_button(
            self.main_window,
            'Login',
            'green',
            self.login
        )

        self.login_button_main_window.place(x=750, y=300)

        # Register button
        self.register_button_main_window = utils.get_button(
            self.main_window,
            'Register New User',
            'gray',
            self.register,
            fg='black'
        )

        self.register_button_main_window.place(x=750, y=400)

    def start(self):
        self.main_window.mainloop()

    def login(self):
        print("Login clicked")

    def register(self):
        print("Register clicked")


if __name__ == "__main__":
    app = App()
    app.start()
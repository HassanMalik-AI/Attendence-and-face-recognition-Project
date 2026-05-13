import tkinter as tk
import utils
import cv2
from PIL import Image, ImageTk


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

        # Create a label to display webcam feed
        self.webcam_label = tk.Label(self.main_window,  bg='gray')
        self.webcam_label.place(x=20, y=20,height=480,width=640)
        self.add_webcam(self.webcam_label)
    
        # Label for instructions
        self.instruction_label = tk.Label(
            self.main_window,
            text="Webcam feed will appear here. Use the buttons below to Login or Register.",
            font=('Helvetica', 12),
            bg='#F0F0F0',
            pady=10
        )
        self.instruction_label.place(x=50, y=560, width=600)

        # Add placeholder for video stream (optional for now)


    def add_webcam(self, label):
        self.cap=cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not open webcam")
            return
        ret, frame=self.cap.read()
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


        self._label = label
        self.update_frame()

    def process_webcam(self):
        ret,frame=self.cap.read()
        self.most_recent_gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        self.frame=cv2.resize(frame,(224,224))
        self.frame = cv2.resize(frame, (640, 480))
        return frame , self.most_recent_gray_frame

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        self.most_recent_gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.frame = cv2.resize(frame, (640, 480))
        img_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        self._photo = ImageTk.PhotoImage(image=img_pil)
        self._label.config(image=self._photo)
        self._label.after(10, self.update_frame)
        

            #convert frame to PhotoImage

    def start(self):
        self.main_window.mainloop()

    def login(self):
        print("Login clicked")

    def register(self):
        print("Register clicked")


if __name__ == "__main__":
    app = App()
    app.start()
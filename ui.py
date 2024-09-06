from tkinter import Tk

THEME_COLOR = "#375362"


class Quiz:

     def __init__(self):
        self.window = Tk()
        self.window.title("quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #self.canvas =Canvas

        self.window.mainloop()

#quiz_interface = Quiz()

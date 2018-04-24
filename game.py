from tkinter import Tk, TRUE


class Main:

    def __init__(self, frame):
        self.frame = frame
        frame.title("Guess The Word")
        frame.resizable(width=TRUE, height=TRUE)
        frame.geometry('{}x{}'.format(450, 450))
        frame.configure(background="black")


app = Tk()
my_gui = Main(app)
app.mainloop()

import tkinter
import tkinter.ttk as ttk

class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tkinter.Text(self)
        self.place(rely=0.45)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.place(rely=0.45)
        self.txt['yscrollcommand'] = scrollb.set

root = tkinter.Tk()

text = TextScrollCombo(root)
text.pack(fill="both", expand=True)
text.config(width=800, height=900)

text.txt.config(font=("consolas", 12), undo=True, wrap='word')
text.txt.config(borderwidth=3, relief="sunken")

style = ttk.Style()
style.theme_use('clam')

root.mainloop()
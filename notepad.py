from tkinter import *
from gtts import gTTS
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename


def audio():
    global fl
    if fl == None:
        fl = asksaveasfilename(initialfile="Unsaved.txt", defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
        if fl == "":
            fl = None
        else:
            f = open(fl, "w")
            f.write(TxtArea.get(1.0, END))
            f.close()

            note.title(os.path.basename(fl) + " -Notepad")
            print("File Saved")
    else:
        f = open(fl, "w")
        f.write(TxtArea.get(1.0, END))
        f.close()
    fh = open(fl, "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)

    output.save("output.mp3")
    fh.close()

    os.system("start output.mp3")

def Open():
    global fl
    fl = askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])

    if fl == "":
        fl = None
    else:
        note.title(os.path.basename(fl)+" - Notepad")
        TxtArea.delete(1.0, END)
        f = open(fl, "r")
        TxtArea.insert(1.0, f.read())
        f.close()

def Save():
    global fl
    if fl == None:
        fl = asksaveasfilename(initialfile="Unsaved.txt", defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
        if fl == "":
            fl = None
        else:
            f=open(fl, "w")
            f.write(TxtArea.get(1.0, END))
            f.close()

            note.title(os.path.basename(fl)+" -Notepad")
            print("File Saved")
    else:
        f=open(fl, "w")
        f.write(TxtArea.get(1.0, END))
        f.close()

def Exit():
    note.destroy()

def about():
    showinfo("Notepad", "Notepad by Mahfuzur Rahman")

def New():
    global fl
    note.title("Unsaved - Notepad")
    fl = None
    TxtArea.delete(1.0, END)


if __name__ == '__main__':
    note = Tk()
    note.title("Unsaved - Notepad")
    note.wm_iconbitmap("1.ico")
    note.geometry("650x744")

    TxtArea = Text(note, font="arial 12")
    fl = None
    TxtArea.pack(expand=True, fill=BOTH)

    menu = Menu(note)
    Filemenu = Menu(menu)

    Filemenu.add_command(label="New", command=New)

    Filemenu.add_command(label="open", command = Open)

    Filemenu.add_command(label="Save", command = Save)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit", command=Exit)
    menu.add_cascade(label="File", menu=Filemenu)

    TextSpeech = Menu(menu)
    TextSpeech.add_command(label="Play Audiobook", command=audio)
    menu.add_cascade(label="Text-To-Speech", menu=TextSpeech)

    help = Menu(menu)
    help.add_command(label="About", command=about)
    menu.add_cascade(label="Help", menu=help)

    note.config(menu=menu)

    note.mainloop()

from tkinter import *
import tkinter.font as tkFont
import os,sys, subprocess

from widgets import Title, TextConteiner, StandardButton, FontStyle
from widgets import PyLaTex_generator

# Represents all the second window
class Window2:
    def __init__ (self, master, root, path):

        self.master = master
        self.root = root
        self.path = path
        
        # Zenith's logo render
        self.zenithLabelRender = PhotoImage(file=os.path.join(os.path.dirname(__file__), "DEPENDENCES/IMAGES/zenith-faixa.png"))
        
        # All widgets definition
        ButtonFinish = StandardButton (frame=self.master, text="Gerar", command= self.PyLaTex_function)
        ZenithLabel  = Label (self.master, image= self.zenithLabelRender, highlightthickness=0, borderwidth=0)

        self.MainTitle =    Title (master, "Título" , 1)
        self.SectionName1 = Title (master, "Seção 1", 2)
        Conteiner1 = Frame(master)
        self.SectionText1 = TextConteiner(Conteiner1, master)

        self.SectionName2 = Title (master, "Seção 2", 4)
        Conteiner2 = Frame(master)
        self.SectionText2 = TextConteiner(Conteiner2, master)

        self.SectionName3 = Title (master, "Seção 3", 6)
        Conteiner3 = Frame(master)
        self.SectionText3 = TextConteiner(Conteiner3, master)

        ''' Sets a boolean variable to indicate the state of the CheckButton. From the beginning, the box is checked and val_checkbox returns 
        True. If the box is unchecked, val_checkbox returns False.'''

        self.valCheckBox = BooleanVar(value=True)
        self.CheckBox = Checkbutton(master, 
                                    text="Inserir Imagens",
                                    variable = self.valCheckBox,
                                    font = FontStyle.get(),
                                    bg= "Black",
                                    fg= "White",
                                    selectcolor="Black")

        # Positioning all widgets in the master root
        ZenithLabel.grid   (row=0, column=0, padx=0 , pady=0 , columnspan=2)
        Conteiner1.grid    (row=3, column=1, padx=10)
        Conteiner2.grid    (row=5, column=1)
        Conteiner3.grid    (row=7, column=1)
        ButtonFinish.grid  (row=8, column=1, padx=20, pady=10, sticky=E)
        self.CheckBox.grid (row=8, column=0, padx=20)

    # Function to generates a LaTex file with the written text
    def PyLaTex_function (self):
        maintitle      = self.MainTitle.get_title()
        section1_title = self.SectionName1.get_title()
        section2_title = self.SectionName2.get_title()
        section3_title = self.SectionName3.get_title()

        section1_text  = self.SectionText1.get_text()
        section2_text  = self.SectionText2.get_text()
        section3_text  = self.SectionText3.get_text()

        PyLaTex_generator (maintitle, section1_text, section1_title, section2_text, section2_title, section3_text, section3_title, self.path, self.valCheckBox.get())

        self.root.destroy()
        # os.startfile(self.path)
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, self.path])
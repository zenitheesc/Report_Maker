from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
import tkinter.font as tkFont
import os

import statistics
from dataparser import DataParser
from widgets import StandardButton, FontStyle
from widgets import switch_frame
from window2 import Window2
import json


class Window1:

    def __init__(self, master, root):

        self.master = master
        self.root = root

        # Zenith's logo render
        self.zenithLabelRender = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "DEPENDENCES/IMAGES/zenith-faixa.png"))

        content = Frame(master, width=450, height=650, background="black")

        # frame = ttk.Frame(content, relief="sunken", width=800, height=600)

        # Variables
        self.tokenSeparator = StringVar(value=",")
        self.logFilename = StringVar()
        self.cuttedFilename = StringVar(value="<arquivo log>")
        self.folderName = StringVar()
        self.cuttedFoldername = StringVar(value="<pasta destino>")
        self.parserString = StringVar()
        self.fieldString = StringVar()
        self.fields_list = StringVar()
        l = ('a1:integer', 'a2:integer', 'latitude:float', 'longitude:float',
             'a5:integer', 'a6:integer', 'a7:integer', 'a8:integer', 'a9:integer',
             'a0:float', 'a10:float', 'a12:integer', 'a13:integer', 'altitude:float',
             'a15:integer', 'a16:integer', 'a17:float', 'a18:integer', 'a19:integer',
             'a20:integer', 'a21:integer', 'a22:integer', 'a23:integer', 'a24:str')
        self.fields_list.set(())  # ('a:integer', 'b:float', 'c:str'))

        # Component Creation
        ZenithLabel = Label(
            self.master, image=self.zenithLabelRender, highlightthickness=0, borderwidth=0)

        titleBrowse = LabelFrame(content, bg="Black", fg="White", font=FontStyle.get(
        ), width=340, text="1. Selecione o arquivo")
        logBrowse = ttk.Label(
            titleBrowse, textvariable=self.cuttedFilename, background="black", foreground="white")
        logBtnBrowse = StandardButton(
            frame=titleBrowse, text="Browse", command=self.browseLog)
        folderBrowse = ttk.Label(
            titleBrowse, textvariable=self.cuttedFoldername, background="black", foreground="white")
        fldBtnBrowse = StandardButton(
            frame=titleBrowse, text="Browse", command=self.browseFolder)

        titleField = LabelFrame(content, bg="Black", fg="White", font=FontStyle.get(
        ), text="2. Organize a ordem dos tipos de dados")
        txtAddField = ttk.Entry(
            titleField, textvariable=self.fieldString, width=50)
        btnAddField = StandardButton(
            frame=titleField, text="Add", command=self.addField)
        btnJsonField = StandardButton(
            frame=titleField, text="From JSON", command=self.fromJson)
        self.lbxFields = Listbox(
            titleField, selectmode="SINGLE", listvariable=self.fields_list, width=50)
        btnMovDnField = StandardButton(
            frame=titleField, text="Move Down", command=self.moveDn)
        btnMovUpField = StandardButton(
            frame=titleField, text="Move Up", command=self.moveUp)
        btnRemField = StandardButton(
            frame=titleField, text="Remover", command=self.removeField)
        btnEdtField = StandardButton(
            frame=titleField, text="Editar", command=self.editField)

        titleSeparator = LabelFrame(content, bg="Black", fg="White", font=FontStyle.get(
        ), text="3. Selecione o token de separação")
        txtSeparator = ttk.Entry(
            titleSeparator, textvariable=self.tokenSeparator, width=50)
        btnParse = StandardButton(
            frame=titleSeparator, text="Parse", command=self.parse)

        btnCancel = StandardButton(
            frame=content, text="Sair", command=self.root.destroy)

        # Place the two differents Frames
        ZenithLabel.pack(side=TOP)
        content.pack(side=TOP, fill=Y)

        # Place components in content's grid
        titleBrowse.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        logBrowse.grid(column=0, row=0, padx=19, pady=10)
        logBtnBrowse.grid(column=1, row=0, padx=20, pady=10)
        folderBrowse.grid(column=0, row=1, padx=19, pady=10)
        fldBtnBrowse.grid(column=1, row=1, padx=20, pady=10)

        titleField.grid(column=0, row=1, padx=10, pady=10, columnspan=2)
        txtAddField.grid(column=0, row=0, padx=10, pady=10)
        btnAddField.grid(column=1, row=0, padx=20, pady=10)
        btnJsonField.grid(column=2, row=0, padx=20, pady=10)
        self.lbxFields.grid(column=0, row=1, pady=10, rowspan=4)
        btnMovUpField.grid(column=1, row=1, padx=20, pady=5)
        btnMovDnField.grid(column=1, row=2, padx=20, pady=5)
        btnEdtField.grid(column=1, row=3, padx=20, pady=5)
        btnRemField.grid(column=1, row=4, padx=20, pady=5)

        titleSeparator.grid(column=0, row=2, padx=10, pady=10, columnspan=2)
        txtSeparator.grid(column=0, row=0, padx=10, pady=10)
        btnParse.grid(column=1, row=0, padx=20, pady=10)
        btnCancel.grid(column=0, row=3, padx=20, pady=10, sticky=E)

    def browseLog(self, *args):
        filename = filedialog.askopenfilename()
        if not filename == "":
            self.logFilename.set(filename)
            self.cuttedFilename.set(filename[0:44]+'...')

    def browseFolder(self, *args):
        foldername = filedialog.askdirectory()
        if not foldername == "":
            self.folderName.set(foldername)
            self.cuttedFoldername.set(foldername[0:44]+'...')

    def addField(self):
        value = self.fieldString.get()
        self.lbxFields.insert(0, value)

    def fromJson(self):
        json_file = filedialog.askopenfilename()
        with open(json_file, 'r') as myfile:
            data = myfile.read()
        d = (json.loads(data))
        print(d)
        idx = 0
        # self.lbxFields.clear(())
        for i in d.keys():
            self.lbxFields.insert(idx, (i + ":" + d[i]))
            idx = idx + 1

    def editField(self):
        index = int(self.lbxFields.curselection()[0])
        newStr = simpledialog.askstring(title="Edit", prompt="New Value:")
        self.lbxFields.insert(index, newStr)
        self.lbxFields.delete(index+1)

    def removeField(self):
        idx = self.lbxFields.curselection()
        self.lbxFields.delete(idx)

    def moveUp(self):
        idx = self.lbxFields.curselection()[0]
        if idx == 0:
            return None
        above = idx-1
        abv_txt = self.lbxFields.get(above)
        self.lbxFields.delete(above)
        self.lbxFields.insert(idx, abv_txt)

    def moveDn(self):
        idx = self.lbxFields.curselection()[0]
        if idx == self.lbxFields.size()-1:
            return None
        txt = self.lbxFields.get(idx)
        self.lbxFields.delete(idx)
        self.lbxFields.insert(idx+1, txt)

    def dictFromListBox(self, strTupleFields):
        fields = strTupleFields.get()[1:-1].split(',')  # removes parantheses
        if fields[1] == '':
            fields = fields[:-1]  # removes empty item when size is 1
        output = dict()
        for field in fields:
            field = field.strip().strip('\'')  # removes spaces and single quotes
            name = field.split(':')[0]
            datatype = field.split(':')[1]
            output[name] = datatype
        return output

    def parse(self):
        struct = self.dictFromListBox(self.fields_list)
        struct["separator"] = self.tokenSeparator.get()
        parser = DataParser(struct)
        with open(self.logFilename.get(), 'r') as logfile:
            testline = logfile.readline()
            data = parser.parse_line(testline)
            if data == None:
                messagebox.showerror(
                    title="Error", message="Could not match line structure to the log's [first] line")
                return None
        all_data = parser.parse_file(self.logFilename.get())
        self.generateStatistics(all_data)

    def generateStatistics(self, all_data):
        while(True):
            dialogScript = "Escolha os gráficos que você deseja inserir no relatório.\n\
                (a) Para gerar um gráfico 'x' versus 'y', digite: x,y\n\
                digite 'x,y,M,N' para limitar o grafico entre o intervalo M...N\n\
                (b) Para gerar um mapa, digite: latitude,longitude\n\
                    Para ir para próxima janela, deixe o campo vazio."

            strPlots = simpledialog.askstring(
                title="Graph", prompt=dialogScript)
            if strPlots == '':
                self.window1_to_window2()
                break
            plots = strPlots.split(',')
            lowerbound = -214748364
            upperbound = 2*214748364

            if len(plots) > 2:
                lowerbound = plots[2]

            if len(plots) == 4:
                upperbound = plots[3]
            # print(len(all_data[plots[0]]),len(all_data[plots[1]]))
            if not len(all_data[plots[0]]) or not len(all_data[plots[1]]):
                print("no data ")
                continue
            if "latitude" in plots and "longitude" in plots:
                if plots[0] == "latitude":
                    statistics.generate_map(map(lambda x: x/10000, all_data[plots[0]]), map(
                        lambda x: x/10000, all_data[plots[1]]), self.folderName.get())
                else:
                    statistics.generate_map(
                        all_data[plots[1]], all_data[plots[0]], self.folderName.get())
            else:
                def bound(x): return x if (x > float(lowerbound)
                                           and x < float(upperbound)) else 0
                print('upper: ', upperbound, ' lower: ', lowerbound)
                y = list(map(bound, all_data[plots[1]]))
                print(len(y))
                g = statistics.generate_data_x_data(
                    y, all_data[plots[0]], plots[1], plots[0], self.folderName.get())
                print(g)

    def window1_to_window2(self):
        window2Frame = Frame(self.root, bg="Black")
        switch_frame(self.master, window2Frame)
        window2 = Window2(window2Frame, self.root, self.folderName.get())

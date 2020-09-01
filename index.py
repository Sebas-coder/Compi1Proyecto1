from tkinter import ttk
from tkinter import * 
from tkinter import scrolledtext 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Button

# Analizers class
from HtmlAnalizer.AnalizadorHtml import Analizador as AHtml

# index class 
class Product:
    # main constructor
    def __init__(self, window):
            # Initializations 
            self.wind = window
            self.wind.title('Proyecto 1')
            self.wind.geometry('1200x900')
            self.wind.configure(bg = '#2A363B')
            self.wind.resizable(0,0)

            # Creating menu options 
            menubar = Menu(self.wind)
            self.wind.config(menu = menubar) 
            
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo")
            filemenu.add_command(label="Abrir", command = self.openFile)
            filemenu.add_command(label="Guardar")
            filemenu.add_command(label="Guardar como")
            
            helpmenu = Menu(menubar, tearoff=0)
            helpmenu.add_command(label="Ayuda")
            helpmenu.add_command(label="Acerca de...")
            helpmenu.add_separator()
            helpmenu.add_command(label="Salir", command=self.wind.quit)

            menubar.add_cascade(label="Archivo", menu=filemenu)
            menubar.add_cascade(label="Ayuda", menu=helpmenu)
                         
            # Creating componente main window 
            ''' self.title = Label(self.wind, text = 'Titulo',fg='white', pady = 10,bg = '#2A363B',font=("Arial Bold", 25))
            self.title.place(x = 25, y = 1) '''
            
            self.txtEntry = scrolledtext.ScrolledText(self.wind, width = 141 , height = 23 )
            self.txtEntry.place(x=25, y = 50)
            
            ''' self.title1 = Label(self.wind, text = 'Titulo',fg='white', pady = 10,bg = '#2A363B',font=("Arial Bold", 25))
            self.title1.place(x = 25, y = 440) '''
            
            self.txtConsole = scrolledtext.ScrolledText(self.wind, width = 141 , height = 23, bg = 'black', fg = '#99B898')
            self.txtConsole.place(x=25, y = 480)
            
            self.typeAnalizervar = StringVar()
            self.typeAnalizer = ttk.Combobox(self.wind, textvariable = self.typeAnalizervar, state = "readonly")
            self.typeAnalizer['values'] = ('.html', '.css', '.js','.rmt')
            self.typeAnalizer.place(x = 995, y = 12)
            self.typeAnalizer.current(1)
            
            self.button = ttk.Button(self.wind,text = 'Analizar',command = self.Analize)
            self.button.place(x = 900, y = 12)
    
    # methods of menu      
    def openFile(self):
        nameFile = filedialog.askopenfilename(title = "Seleccione archivo",filetypes = (("js files","*.js"), ("html files","*.html"),("css files","*.css"),("All Files","*.*"),("rmt files","*.rmt")))
        if nameFile!='':
            archi1 = open(nameFile, "r", encoding="utf-8")
            contenido = archi1.read()
            archi1.close()
            self.txtEntry.delete("1.0", END) 
            self.txtEntry.insert("1.0", contenido)

    def Analize(self):
        cadena = self.txtEntry.get("1.0", END)  
        if cadena.strip() == "":
            messagebox.showinfo('Projecto 1', 'Cadena vacia')
        else:
            if self.typeAnalizer.get() == '.js':
                print("JavaScript")
                
                
            elif(self.typeAnalizer.get() == '.html'):
                ''' a = AHtml()
                b = a.lexer(cadena) '''
                
            elif(self.typeAnalizer.get() == '.css'):
                print("CSS")
                
            elif(self.typeAnalizer.get() == '.rmt'):
                print("RMT")
            
            
        ''' retorno = lexerHtml(cadena)
        self.txtConsole.delete("1.0", END)
        self.txtConsole.insert("1.0", retorno)
        messagebox.showinfo('Project 1', 'Analysis Finished') '''
    
if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
# Librerias para tkinter
from tkinter import ttk
from tkinter import * 
from tkinter import scrolledtext 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Button

# librerias extra
from graphviz import Digraph
import os
import webbrowser
import time
from Errores.Error import Tipo as TE

# Analizers class
from HtmlAnalizer.AnalizadorHtml import Analizador as AHtml
from CssAnalizer.AnalizadorCss import Analizador as ACss
from JsAnalizer.AnalizadorJs import Analizador as AJs
from RmtAnalizer.AnalizadorRmt import Analizador as ARmt
from RmtAnalizer.ScannerRmt import Scanner as ScannerRmt

# Tokens
from JsAnalizer.Token import Token as TokenJs
from JsAnalizer.Token import Tipo as TTJs

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
                vaJs = AJs()
                vaJs.lexer(cadena)
                bJs = vaJs.bandera
                pthJS = vaJs.Path
                ltJs = vaJs.lista_tokens
                
                if bJs == True:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - Sin errores')
                else:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - La cadena tiene errores')
                    lJs = vaJs.lista_errores
                    self.ImpresionTokens(lJs)
                    webbrowser.open_new_tab(os.path.dirname(__file__) +"/errores.html")
                try:
                    archivo = open(pthJS + "/archivo.js",'w')
                    archivo.write(vaJs.cadenaCorrecta)
                except Exception:
                    messagebox.showinfo('Project 1', 'Error con la ruta de guardado') 
                
            elif(self.typeAnalizer.get() == '.html'):
                print("HTML")
                vaHtml = AHtml()
                vaHtml.lexer(cadena)
                bHtml = vaHtml.bandera
                pthHtml = vaHtml.Path
                
                if bHtml == True:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - Sin errores')
                else:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - La cadena tiene errores')
                    lHtml = vaHtml.lista_errores
                    self.ImpresionTokens(lHtml)
                    webbrowser.open_new_tab(os.path.dirname(__file__) +"/errores.html")
                try:
                    archivo = open(pthHtml + "/archivo.html",'w')
                    archivo.write(vaHtml.cadenaCorrecta)
                except Exception:
                    messagebox.showinfo('Project 1', 'Error con la ruta de guardado')
                         
            elif(self.typeAnalizer.get() == '.css'):
                print("CSS")
                vaCss = ACss()
                vaCss.lexer(cadena)
                bCss = vaCss.bandera
                leCss = vaCss.lista_estados
                pthCss = vaCss.Path
                self.txtConsole.delete("1.0", END)
                for i in range(0,len(leCss)):
                        self.txtConsole.insert(END, leCss[i] + "\n")
                
                if bCss == True:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - Sin errores')
                else:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - La cadena tiene errores')
                    lCss = vaCss.lista_errores
                    self.ImpresionTokens(lCss)
                    webbrowser.open_new_tab(os.path.dirname(__file__) +"/errores.html")
                try:
                    archivo = open(pthCss + "/archivo.css",'w')
                    archivo.write(vaCss.cadenaCorrecta)
                except Exception:
                    messagebox.showinfo('Project 1', 'Error con la ruta de guardado')
                    
            elif(self.typeAnalizer.get() == '.rmt'):
                vaRmt = ARmt()
                vaRmt.lexer(cadena)
                bRmt = vaRmt.bandera
                
                if bRmt == True:
                    messagebox.showinfo('Project 1', 'Analisis lexico finalizado - Sin errores')
                    ltRmt = vaRmt.lista_tokens
                    ScRmt = ScannerRmt()
                    ScRmt.inicio(ltRmt)
                    bScRmt = ScRmt.bandera
                    
                    if bScRmt == True:
                        messagebox.showinfo('Project 1', 'Analisis sintactico - Tiene errores')
                    else:
                        messagebox.showinfo('Project 1', 'Analisis sintactico - Sin errores')
                else:
                    messagebox.showinfo('Project 1', 'Analisis lexico finalizado - La cadena tiene errores')
                    lRmt = vaRmt.lista_errores
                    self.ImpresionTokens(lRmt)
                    webbrowser.open_new_tab(os.path.dirname(__file__) +"/errores.html")
               
                
    def ImpresionTokens(self,listado):
        inicio = "<!DOCTYPE html>\n"\
            "<html lang=\"en\">\n"\
            "<head>\n"\
            "    <meta charset=\"UTF-8\">\n"\
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"\
            "    <link href=\""
        archCSS = os.path.dirname(__file__) + "/bootstrap.min.css\" " 
        medio = "rel=\"stylesheet\" type=\"text/css\">\n"\
            "<title>REPORTE</title>\n"\
            "</head>\n"\
            "<body>\n"\
            " <br>\n"\
            "<br>\n"\
            "<div class = \"jumbotron\">\n"\
            "<h2 class=\"display-3\">Lista de Errores</h2>\n"\
            "<table class=\"table table-hover\">\n"\
            "<thead>\n"\
            "<tr class=\"table-secondary\">\n"\
            "<th>No.</th>\n"\
            "<th>Linea</th>\n"\
            "<th>Columna</th>\n"\
            "<th>Descripcion</th>\n"\
            "</tr>\n"\
            "</thead>\n"\
            "<tbody>\n"  
        tokens = ""
        for i in range(0,len(listado)):
            tokens += "<tr class=\"table-light\">\n"
            tokens += "<td>"+ str(i) + "</td>\n"
            tokens += "<td>"+ str(listado[i].fila) + "</td>\n"
            tokens += "<td>"+ str(listado[i].columna) + "</td>\n"
            if listado[i].tipoError == TE.CARACTERINVALIDO:
                tokens += "<td> Caracter invalido:  "+ str(listado[i].lexema) + "</td>\n"
            elif listado[i].tipoError == TE.ERERRONEA:
                tokens += "<td> Expresion regular erronea:  "+ str(listado[i].lexema) + "</td>\n"
            tokens += "</tr>\n"
        final = "</tr>\n"\
            "</tbody>\n"\
            "</table>\n"\
            "</div>\n"\
            "</body>\n"\
            "</html>\n"
        contenido = inicio + archCSS + medio + tokens + final
        archHtml = os.path.dirname(__file__) + "/errores.html"
        archivo = open(archHtml,'w')
        archivo.write(contenido)        
                
if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
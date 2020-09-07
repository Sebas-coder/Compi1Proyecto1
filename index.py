from tkinter import ttk
from tkinter import * 
from tkinter import scrolledtext 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Button

from graphviz import Digraph
import os
import webbrowser

# Analizers class
from HtmlAnalizer.AnalizadorHtml import Analizador as AHtml
from CssAnalizer.AnalizadorCss import Analizador as ACss
from JsAnalizer.AnalizadorJs import Analizador as AJs

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
                lJs = vaJs.lista_errores
                
                if bJs == True:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - Sin errores')
                else:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - La cadena tiene errores')
                    self.ImpresionTokens(vaJs)
                
            elif(self.typeAnalizer.get() == '.html'):
                print("HTML")
                vaHtml = AHtml()
                vaHtml.lexer(cadena)
                bHtml = vaHtml.bandera
                lHtml = vaHtml.lista_errores
                if bHtml == True:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - Sin errores')
                else:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - La cadena tiene errores')
                    self.ImpresionTokens(lHtml)
                
                         
            elif(self.typeAnalizer.get() == '.css'):
                print("CSS")
                vaCss = ACss()
                vaCss.lexer(cadena)
                bCss = vaCss.bandera
                
                lCss = vaCss.lista_errores
                
                if bCss == True:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - Sin errores')
                else:
                    messagebox.showinfo('Project 1', 'Analisis finalizado - La cadena tiene errores')
                    self.ImpresionTokens(lCss)
                    
                
                    
            elif(self.typeAnalizer.get() == '.rmt'):
                print("RMT")
               
                
    def ImpresionTokens(self,listado):
        inicio = "<!DOCTYPE html>\n"\
            "<html lang=\"en\">\n"\
            "<head>\n"\
            "    <meta charset=\"UTF-8\">\n"\
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"\
            "    <link href=\""
        archCSS = os.path.dirname(__file__) + "/bootstrap.min.css\" " 
        medio = "rel=\"stylesheet\" type=\"text/css\">\n"\
            "<title>Document</title>\n"\
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
            "<tbody>\n"\
            "<tr class=\"table-light\">\n"   
        tokens = ""
        for i in range(0,len(listado)):
            tokens += "<td>"+ str(i) + "</td>\n"
            tokens += "<td>"+ str(listado[i].fila) + "</td>\n"
            tokens += "<td>"+ str(listado[i].columna) + "</td>\n"
            tokens += "<td>"+ str(listado[i].lexema) + "</td>\n"
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
        webbrowser.open_new_tab(os.path.dirname(__file__) +"/errores.html")
    
    def grafo(self, listaEstados):
        dot = Digraph()
        dot.attr(bgcolor='#15415D', label='agraph')
        dot.attr(rankdir='LR', size='8,5')
        
        dot.render('test-output/round-table.img', view=True)
                
if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
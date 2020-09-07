from graphviz import Digraph
import os
import webbrowser

dot = Digraph()

dot.attr(bgcolor='#15415D', label='agraph')
dot.attr(rankdir='LR', size='8,5')
 

dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
dot.node('LR_0')
dot.node('LR_5')
dot.node('DEPRERES')

dot.attr('node', shape='circle')
dot.edge('LR_0', 'LR_2', label='SS(B)')

print(dot.source)
dot.render('test-output/round-table.img', view=True)

contenido = "socxzcxzcxchimilco"

ruta = os.path.dirname(__file__) + "/nuevo1.html"
archivo = open(ruta,'w')
archivo.write(contenido)

print(os.path.abspath(__file__))
# Esta es la dasnfbdfij
print(os.path.dirname(__file__))
""" webbrowser.open_new_tab(os.path.dirname(__file__) +"/archivo.html") """
v = " sdgfb\n"\
    "sadffdsfewd"
print(v)
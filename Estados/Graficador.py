from graphviz import Digraph

class Graficador:
    a = 0
    b = 0
    c = 0
    def Graficar(self, Estados):
        self.a = Estados[0]
        self.b = Estados[1]
        self.c = Estados[2]
        
        dot = Digraph()

        dot.attr(bgcolor='#15415D')
        dot.attr(rankdir='LR', size='8,5')
        
        dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
        dot.node('S0')
        
        if a == 1 or b == 1 or c == 1:
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S1', label='[0-9]', color = 'orange', fontcolor="white")
            dot.edge('S1', 'S2', label='.', color = 'orange', fontcolor="white")
            dot.edge('S2', 'S2', label='[0-9]', color = 'orange', fontcolor="white")
            
        elif a == 2 or b == 2 or c == 2:
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S3', label='[a-zA-Z]', color = 'orange', fontcolor="white")
            dot.edge('S3', 'S3', label='[a-zA-Z-]', color = 'orange', fontcolor="white")

        elif a == 3 or b == 3 or c == 3:
            dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S4', label='/', color = 'orange', fontcolor="white")
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S4', 'S5', label='/', color = 'orange', fontcolor="white")
            dot.edge('S5', 'S5', label='[^SL]', color = 'orange', fontcolor="white")

        elif a == 4 or b == 4 or c == 4:
            dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S4', label='/', color = 'orange', fontcolor="white")
            dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S4', 'S6', label='*', color = 'orange', fontcolor="white")
            dot.edge('S6', 'S6', label='[^*]', color = 'orange', fontcolor="white")
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S6', 'S7', label='*', color = 'orange', fontcolor="white")
            dot.edge('S7', 'S6', label='[^*]', color = 'orange', fontcolor="white")
            dot.edge('S7', 'S7', label='/', color = 'orange', fontcolor="white")
        
        elif a == 5 or b == 5 or c == 5:
            dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S8', label='"', color = 'orange', fontcolor="white")
            dot.edge('S8', 'S8', label='[^"]', color = 'orange', fontcolor="white")
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S8', 'S9', label='"', color = 'orange', fontcolor="white")
            
        elif a == 6 or b == 6 or c == 6:
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S10', label='[=><!]', color = 'orange', fontcolor="white")
            dot.edge('S10', 'S11', label='=', color = 'orange', fontcolor="white")
        
        elif a == 7 or b == 7 or c == 7:
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S12', label='SA', color = 'orange', fontcolor="white")
       
        if a != 0 or b != 0 or c != 0:
            dot.render('test-output/round-table.img', view=True)
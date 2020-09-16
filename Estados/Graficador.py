from graphviz import Digraph

class Graficador:
    a = 0
    b = 0
    c = 0
    def Graficar(self, Estados):
        for i in range(0,len(Estados)):
            if i == 0:
                self.a = Estados[0]
            elif i == 1:
                self.b = Estados[1]
            elif i ==2:
                self.c = Estados[2]
        
        dot = Digraph()

        dot.attr(bgcolor='#15415D')
        dot.attr(rankdir='LR', size='8,5')
        
        dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
        dot.node('S0')
        
        if self.a == 1 or self.b == 1 or self.c == 1:
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S1', label='[0-9]', color = 'orange', fontcolor="white")
            dot.edge('S1', 'S2', label='.', color = 'orange', fontcolor="white")
            dot.edge('S2', 'S2', label='[0-9]', color = 'orange', fontcolor="white")
            
        if self.a == 2 or self.b == 2 or self.c == 2:
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S3', label='[a-zA-Z]', color = 'orange', fontcolor="white")
            dot.edge('S3', 'S3', label='[a-zA-Z\-0-9]', color = 'orange', fontcolor="white")

        if self.a == 3 or self.b == 3 or self.c == 3:
            dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S4', label='/', color = 'orange', fontcolor="white")
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S4', 'S5', label='/', color = 'orange', fontcolor="white")
            dot.edge('S5', 'S5', label='[^SL]', color = 'orange', fontcolor="white")

        if self.a == 4 or self.b == 4 or self.c == 4:
            dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S4', label='/', color = 'orange', fontcolor="white")
            dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S4', 'S6', label='*', color = 'orange', fontcolor="white")
            dot.edge('S6', 'S6', label='[^*]', color = 'orange', fontcolor="white")
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S6', 'S7', label='*', color = 'orange', fontcolor="white")
            dot.edge('S7', 'S6', label='[^*]', color = 'orange', fontcolor="white")
            dot.edge('S7', 'S7', label='/', color = 'orange', fontcolor="white")
        
        if self.a == 5 or self.b == 5 or self.c == 5:
            dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S8', label='"', color = 'orange', fontcolor="white")
            dot.edge('S8', 'S8', label='[^"]', color = 'orange', fontcolor="white")
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S8', 'S9', label='"', color = 'orange', fontcolor="white")
            
        if self.a == 6 or self.b == 6 or self.c == 6:
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S10', label='[=><!]', color = 'orange', fontcolor="white")
            dot.edge('S10', 'S11', label='=', color = 'orange', fontcolor="white")
        
        if self.a == 7 or self.b == 7 or self.c == 7:
            dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
            dot.edge('S0', 'S12', label='SA', color = 'orange', fontcolor="white")
       
        if self.a != 0 or self.b != 0 or self.c != 0:
            dot.render('test-output/round-table.img', view=True)
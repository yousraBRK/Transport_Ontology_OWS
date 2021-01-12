
import math

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import rdflib
from rdflib import Graph
g = Graph()
Owl_File = "TransportOntologyTurtle.owl"

#Show the file format
print(rdflib.util.guess_format(Owl_File))
g.parse(Owl_File, format="ttl")


class MyWindow(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.createMenuBar()
        
        # Fill the content of the window

        self.geometry( "500x300" )
        self.title( "Transport" )
    
    def createMenuBar(self):
        menuBar = Menu(self)
        
        

        menutrans = Menu(menuBar, tearoff=0)
        menutrans.add_command(label="Moyen de tranport", command=self.doAbout)
        menuBar.add_cascade( label="Moyen de tranport", menu=menutrans)

        menuMarie = Menu(menuBar, tearoff=0)
        menuMarie.add_command(label="Deplacement", command=self.doAboutM)
        menuBar.add_cascade( label="MarieDeplacement", menu=menuMarie)
        menuMarie.add_command(label="Bus", command=self.doAboutMBus)
        
        menuTour = Menu(menuBar, tearoff=0)
        menuTour.add_command(label="Information", command=self.doAbout)
        menuBar.add_cascade( label="La tour Eiffel", menu=menuTour)

        
        
        self.config(menu = menuBar)        

    


    def doAbout(self):
        d=[]
        qres = g.query("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX ex: <http://www.semanticweb.org/yousra/ontologies/2021/11/untitled-ontology-15#>
        SELECT ?subject
            WHERE { ?subject rdfs:subClassOf ex:Transport}
        """)
        for row in qres.result:
            print(row)
            d.append(row)

        print(d)
        messagebox.showinfo(self,text= d)




    def doAboutM(self):
        d=[]
        qres = g.query("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX ex: <http://www.semanticweb.org/yousra/ontologies/2021/11/untitled-ontology-15#>
        PREFIX ont: <http://www.co-ode.org/ontologies/ont.owl#>
        SELECT ?object
            WHERE { 
                    ?object  ont:est_pris_par   ont:Marie}
        """)
        for row in qres.result:
            print(row)
            d.append(row)

        print(d)
        messagebox.showinfo("MarieDeplacement", d)
    def doAboutMBus(self):
        d=[]
        qres = g.query(""" 
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX ex: <http://www.semanticweb.org/yousra/ontologies/2021/11/untitled-ontology-15#>
        PREFIX ont: <http://www.co-ode.org/ontologies/ont.owl#>
        SELECT ?object
            WHERE { ?object rdf:type ont:Bus.
                    ?object  ont:est_pris_par   ont:Marie .
        }
        """)
        for row in qres.result:
            print(row)
            d.append(row)

        print(d)
        messagebox.showinfo("MarieBus", d)




window = MyWindow()
window.mainloop()
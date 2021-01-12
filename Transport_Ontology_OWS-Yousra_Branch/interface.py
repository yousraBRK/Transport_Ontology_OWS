from tkinter import *
import webbrowser
import rdflib
from rdflib import Graph
g = Graph()
Owl_File = "TransportOntologyTurtle.owl"

#Show the file format
print(rdflib.util.guess_format(Owl_File))
g.parse(Owl_File, format="ttl")


class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Application")
        self.window.geometry("720x480")
        self.window.minsize(200, 300)
        
        

        # initialization des composants
        self.frame = Frame(self.window)

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.Liste_de_moyen_de_transport()
        self.Information_Tour_Eiffel()

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application", font=("Courrier", 20), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="IDF", font=("Courrier", 25), bg='#41B77F',
                               fg='white')
        label_subtitle.pack()

    def Liste_de_moyen_de_transport(self):
        yt_button = Button(self.frame, text="moyen_de transport", font=("Courrier", 25), bg='white', fg='#41B77F',
                           command=self.list)
        yt_button.pack(pady=25, fill=X)
    def list(self):
        top = Tk()
        var = StringVar()
        Lb1 = Label(self.frame, textvariable=var )
        
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
        var.set(d)
        Lb1.pack()

    def Information_Tour_Eiffel(self):
        yt_button = Button(self.frame, text="Tour_Eiffel", font=("Courrier", 20), bg='white', fg='#41B77F',
                           command=self.information)
        yt_button.pack(pady=25, fill=X)
    
    def information(self):
        top = Tk()

        Lb1 = Listbox(top)
        Lb1.insert(1, "Python")
        Lb1.insert(2, "Perl")
        Lb1.insert(3, "C")
        Lb1.insert(4, "PHP")
        Lb1.insert(5, "JSP")
        Lb1.insert(6, "Ruby")

        Lb1.pack()

# afficher
app = MyApp()
app.window.mainloop() 
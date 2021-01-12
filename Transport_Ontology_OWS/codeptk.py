from tkinter import *
import rdflib
from rdflib import Graph

g = Graph()
Owl_File = "TransportOntologyTurtle.owl"

#Show the file format
print(rdflib.util.guess_format(Owl_File))
g.parse(Owl_File, format="ttl")


root=Tk()
root.title("Application")
root.geometry("400x400")

my_menu=Menu(root)
root.config(menu=my_menu)


def hide_all():
	
	doAboutf.pack_forget()
	doAboutmm.pack_forget()
	doAboutstat.pack_forget()

def doAbout():
	hide_all()
	doAboutf.pack(fill="both",expand=1)
	my_label=Label(doAboutf,text="Moyens de transport : ",font=("Courier", 20),foreground="green", justify="left").pack() 
	#label=Label(doAboutf,text= "Moyens de transport : ",font=("Courier", 20),foreground="green", justify="left").pack() 
	qres = g.query("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX ex: <http://www.semanticweb.org/yousra/ontologies/2021/11/untitled-ontology-15#>
        SELECT ?subject
            WHERE { ?subject rdfs:subClassOf ex:Transport}
        """)
	d=[]
	for row in qres.result:
            print(row)
            d.append(row)
	for row in d:
		label=Label(doAboutf, text= row).pack()

def doAboutM():
	hide_all()
	doAboutmm.pack(fill="both",expand=1)
	my_label=Label(doAboutmm,text="Moyens de transport : ",font=("Courier", 20),foreground="green", justify="left").pack() 
	#label=Label(doAboutf,text= "Moyens de transport : ",font=("Courier", 20),foreground="green", justify="left").pack() 
	qres = g.query("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX ex: <http://www.semanticweb.org/yousra/ontologies/2021/11/untitled-ontology-15#>
        SELECT ?object
            WHERE { ?object  ont:est_pris_par   ont:Marie}
        """)
	d=[]
	for row in qres.result:
            print(row)
            d.append(row)
	for row in d:
		label=Label(doAboutmm, text= row).pack()



def doAboutstat():
	hide_all()
	doAboutmm.pack(fill="both",expand=1)
	my_label=Label(doAboutstat,text="Moyens de transport : ",font=("Courier", 20),foreground="green", justify="left").pack() 
	#label=Label(doAboutf,text= "Moyens de transport : ",font=("Courier", 20),foreground="green", justify="left").pack() 
	qres = g.query("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX ex: <http://www.semanticweb.org/yousra/ontologies/2021/11/untitled-ontology-15#>
        PREFIX ont: <http://www.co-ode.org/ontologies/ont.owl#>
        PREFIX per: <http://www.semanticweb.org/kaouter/ontologies/2021/11/untitled-ontology-7#>
        SELECT  ?lieu ?date (count(?personne)  as ?num)
            WHERE { 
                    ?personne  rdf:type  per:Personne.
                     ?personne  ont:prend  ont:Uber.
                    ?personne ont:se_rend  ?lieu.
                    ?personne ont:date_de_depart  ?date
          

        }group by ?lieu ?date
        """)
	d=[]
	for row in qres.result:
            print(row)
            #d.append(row)

	#for row in d:
	#	label=Label(doAboutstat, text= row).pack()

   
        
#create menu item



#application
menutrans = Menu(my_menu, tearoff=0)
menutrans.add_command(label="Moyen de tranport", command=doAbout)
my_menu.add_cascade( label="Moyen de tranport", menu=menutrans)

menuMarie = Menu(my_menu, tearoff=0)
menuMarie.add_command(label="Deplacement", command=doAboutM)
my_menu.add_cascade( label="MarieDeplacement", menu=menuMarie)

menustat = Menu(my_menu, tearoff=0)
menustat.add_command(label="Information", command=doAboutstat)
my_menu.add_cascade( label="Nombre de personnes qui prennent Uber par Date et destination", menu=menustat)



file_new_frame = Frame(root,width=400, height=400, bg="red")
edit_cut_frame=Frame(root,width=400, height=400, bg="blue")
doAboutf=Frame(root,width=400, height=400)
doAboutmm=Frame(root,width=400, height=400)
doAboutstat=Frame(root,width=400, height=400)


root.mainloop()
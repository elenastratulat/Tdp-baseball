from model.model import Model

myModel = Model()
myModel.getTeamsOfYear(2012)
myModel.creaGrafo()
nodi, archi = myModel.getGraphDetails()
print(f"Grafo creato! Il grafo ha {nodi} nodi e {archi} archi")

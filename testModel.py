from model.model import Model

myModel = Model()
myModel.getTeamsOfYear(2012)
myModel.creaGrafo(2012)
nodi, archi = myModel.getGraphDetails()
print(f"Grafo creato! Il grafo ha {nodi} nodi e {archi} archi")

v0 = myModel.getRandomNode()
path, score = myModel.getPathV2(v0)
print(f"Trovata soluzione lunga {len(path)} con somma pesi archi pari a {score}")
for p in path:
    print(p)

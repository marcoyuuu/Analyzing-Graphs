from collections import defaultdict # para lista de adjacencia

class Grafo:

    # constructor
    def __init__(self) -> None:
        # inicializando diferentes listas y variables
        self.adjList = defaultdict(list)
        self.miLista = []
        self.newList = []
        self.var1 = []
        self.var2 = []
        self.tiempo = 0
        self.vf = []

    # función para leer archivo txt y almacenar grafo en lista enlazada
    def leer(self, txt):
        file = open(txt, "r")
        f = file.readlines()
        # creando una lista para almacenar valores en archivo txt
        for line in f:
            self.newList.append(line[:-1])
        # inicializando v como número de vértices y u como número de aristas
        v = int(self.newList[0])
        u = int(self.newList[1])
        # llenando var1 con vértices u y var2 con vértices v, donde los vértices u están conectados a v (u,v)
        for i in range(2, u + 2):
            v1, v2 = [int(x) for x in self.newList[i].split()]
            self.var1.insert(i, v1)
            self.var2.insert(i, v2)
        # for loop para agregar todos los nodos a miLista
        for i in range(0, u):
            self.anadirNodo(self.var1[i])
            self.anadirNodo(self.var2[i])
            # print('miLista es: ',miLista)
        # for loop para agregar relaciones (u,v) a adjList
        for i in range(0, u):
            self.anadirArista(self.var1[i], self.var2[i])
        if self.gDG(txt) == False:
            # for loop para agregar relaciones (v,u) a adjList
            for i in range(0, u):
                if (
                    self.var1[i] not in self.adjList[self.var2[i]]
                ):  # si vertice u no esta conectado a vertice v
                    self.anadirArista(self.var2[i], self.var1[i])  # agrega relacion (v,u)
    
    # función para determinar si grafo es dirigido o no dirigido
    def gDG(self,str):
        results = []
        busc = ['D']
        for i in busc:
            if i in str:
                results.append(True)
            else:
                results.append(False)
        return results

    # función para agregar la relación (u,v) de los vértices a adjList
    def anadirArista(self, nodo1, nodo2):
        temp = []
        if nodo1 in self.miLista and nodo2 in self.miLista:
            if nodo1 not in self.adjList:  # nodo1 (v) no ha sido descubierto
                temp.append(nodo2)  # agrega vertice v a lista temp
                self.adjList[nodo1] = temp  # agrega relación (u,v) a adjList
                # print("adjList: ",adjList)
            elif (
                nodo1 in self.adjList
            ):  # nodo1 (u) ya existe, pero tiene otro vertice v al cual esta conectado
                temp.extend(
                    self.adjList[nodo1]
                )  # llama lista temp con vertices v conectados anteriormente
                temp.append(nodo2)  # agrega vertice v nueva a temp
                self.adjList[nodo1] = temp  # actualiza vertices v
        else:
            print("Nodo no existe.")

    # función para agregar nodos a miLista para obtener los nodos que existen en el grafo
    def anadirNodo(self, nodo):
        if nodo not in self.miLista:
            self.miLista.append(nodo)

    # función para hacer dfs al grafo dirigido
    def dfsDG1(self, nodo, visitado):
        visitado.add(nodo)  # agrega vertice v a conjunto visitado
        print(nodo, end=" ")  # imprime vertice v
        for neighbour in self.adjList[
            nodo
        ]:  # recursivamente busca vertices v, tratarlos como vertice u y buscar sus vertices v, tratarlos como vertice u...
            if neighbour not in visitado:
                self.dfsDG1(
                    neighbour, visitado
                )  # llama función dfDG2 nuevamente, pero con vertice v como vertice u nuevo

    # función para llamar a dfsDG1 recursivamente
    def dfsDG2(self, nodo):
        visitado = set()  # inicializa conjunto para almacenar vertices ya visitados
        print("Orden topológico es:")
        self.dfsDG1(nodo, visitado)  # llama a dfsDG1 recursivamente

    # función para hacer dfs al grafo no dirigido
    def dfsG1(self, nodo, visitado):
        u = int(self.newList[1])
        # for loop para agregar relaciones (v,u) a adjList
        for i in range(0, u):
            if (
                self.var1[i] not in self.adjList[self.var2[i]]
            ):  # si vertice u no esta conectado a vertice v
                self.anadirArista(self.var2[i], self.var1[i])  # agrega relacion (v,u)
        visitado.add(nodo)  # agrega vertice v a conjunto visitado
        print(nodo, end=" ")  # imprime vertice v
        for neighbour in self.adjList[
            nodo
        ]:  # recursivamente busca vertices v, tratarlos como vertice u y buscar sus vertices v, tratarlos como vertice u...
            if neighbour not in visitado:
                self.dfsG1(
                    neighbour, visitado
                )  # llama función dfsG2 nuevamente, pero con vertice v como vertice u nuevo

    # función para llamar a dfsDG1 recursivamente
    def dfsG2(self, nodo):
        visitado = set()  # inicializa conjunto para almacenar vertices ya visitados
        self.dfsG1(nodo, visitado)  # llama a dfsDG1 recursivamente

    # función para determinar ciclo/arista trasera
    def dfsCiclo1(self, nodo):
        v = int(self.newList[0])  # inicializando v como numero de vertices
        self.visit = [
            "white"
        ] * v  # inicializando lista visit de tamaño v y todos = False para saber si vertice ha sido visitado
        self.vi = [
            0
        ] * v  # inicializando lista vi de tamaño v y todos = 0 para almacenar tiempo de inicialización
        self.vf = [
            0
        ] * v  # inicializando lista vf de tamaño v y todos = 0 para almacenar tiempo de finalización
        if self.visit[nodo] == "white":
            self.dfsCiclo2(
                nodo
            )  # llama a función dfsCiclo2 para buscar recursivamente si hay arista trasera en grafo

    # función llamada recursivamente para determinar ciclo/arista trasera
    def dfsCiclo2(self, nodo):
        self.tiempo += 1  # incrementa tiempo por 1
        self.visit[nodo] = "gray"  # marcar nodo como visitado
        self.vi[nodo] = self.tiempo  # obtiene tiempo de inicialización
        for neighbour in self.adjList[nodo]:  # recursivamente busca vertices v de u
            if self.visit[neighbour] == "white":  # si no ha sido visitado
                self.dfsCiclo2(neighbour)
            else:
                self.detCiclo(nodo)
        self.visit[nodo] = "black"  # marcar nodo como visitado
        self.tiempo += 1  # incrementa tiempo por 1
        self.vf[nodo] = self.tiempo  # obtiene tiempo de inicialización

    # función llamada por dfsCiclo2 para detectar ciclos
    def detCiclo(self, nodo):
        for neighbour in self.adjList[nodo]:
            if (
                self.vi[nodo] > self.vi[neighbour] and self.vi[neighbour] != 0
            ):  # identifica arista trasera
                print("Ciclo de", str(nodo) + " ---> " + str(neighbour))

    # función para hacer BFS, llama a bfsRec recursivamente 
    def BFS(self, nodo):
        v = int(self.newList[0])  # inicializando v como numero de vertices
        self.visitado = []
        self.color = [
            "white"
        ] * v  # inicializando lista color de tamaño v y todos = 'white' para saber si vertice ha sido visitado
        self.t = [
            0
        ] * v  # inicializando lista t de tamaño v y todos = 0 para almacenar tiempo
        self.color[nodo] = "gray"
        self.q = [] # crea fila vacía
        self.q.append(nodo) # agrega vertice u a la pila q
        self.l = len(self.q) # almacena tamaño de pila q en l
        while self.l > 0:  # loop para visitar todos los nodos
            p = self.q.pop(0) # ejecuta pop a pila
            self.bfsRec(p) # llama recursivamente a bfsRec
            self.l = len(self.q) # actualiza tamaño de pila q en l
        print("Componente conexo es:", self.visitado)

    # función llamada recursivamente por BFS  
    def bfsRec(self, nodo):
        for neighbour in self.adjList[nodo]:  # visitar vertices v
            if self.color[neighbour] == "white": # si no ha sido visitado
                self.color[neighbour] = "gray" # indica vertice v como color 'gray'
                self.t[neighbour] = self.t[nodo] + 1 # almacena tiempo de vertice v como 1+ que vertice u
                self.q.append(neighbour) # operación push de vertice v a pila q
        self.color[nodo] = "black" # indica vertice u como color 'black'
        self.visitado.append(nodo) # agrega vertice u a lista de vertices visitados

    # función para determinar componentes conexos
    def compConexo(self):
        c = 0 # contador de componentes conexos
        v = int(self.newList[0])  # inicializando v como numero de vertices
        self.visitado = (
            [] * v
        )  # inicializando lista visitado de tamaño v para saber si vertice ha sido visitado
        for i in range(0, v): # recorre todos los vertices
            if i not in self.visitado: # si no ha sido visitado
                self.BFS(i) # hace BFS con vertice v
                c += 1 # añade 1 al contador
        print("Hay", c, "componente(s) conexo(s)")

    # función para crear menu
    def impMenu(self):
        print("1. Orden Topológico")
        print("2. Detectar ciclos")
        print("3. Componentes conexos")
        print("4. Salir")
        while True:
            ind = int(input()) # pide entrada a usuario
            if ind == 1: # busca orden topológico con función dfsDG2
                print("")
                self.dfsDG2(self.var1[0])
                print("\n")
                print("1. Orden Topológico")
                print("2. Detectar ciclos")
                print("3. Componentes conexos")
                print("4. Salir")
            elif ind == 2: # busca ciclos con función dfsCiclo1
                print("")
                self.dfsCiclo1(self.var1[0])
                print("")
                print("1. Orden Topológico")
                print("2. Detectar ciclos")
                print("3. Componentes conexos")
                print("4. Salir")
            elif ind == 3: # busca componentes conexos con función compConexo
                print("")
                self.compConexo()
                print("")
                print("1. Orden Topológico")
                print("2. Detectar ciclos")
                print("3. Componentes conexos")
                print("4. Salir")
            elif ind == 4: # acaba el programa
                break

# función main
if __name__ == "__main__":
    g = Grafo()
    g.leer('tinyDG.txt')
    g.impMenu()

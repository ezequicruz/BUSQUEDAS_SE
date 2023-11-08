from Node import Node
#funcion de busqueda recursiva, la funcion recibe como parametros, el nodo inicial, la lista de nodos, los antecesores, lista de nodos revisados,
#el nodo actual, la lista de todos los nodos, y la cola de sucesores
def cola_recursiva(init_node:Node, nodes:list, predecessors:list, nodes_review:list,actual_node:Node,bfs_node_list:list):
    node_cola_actual = [] #Inicializamos la cola actual como una lista vacia
    if init_node.num_node == actual_node.num_node: #Revisamos si nos encontramos en el nodo inicial
        predecessors.append(0)
        nodes.append(actual_node.num_node) #Agregamos a la lista de nodos el nodo actual en el que nos encontramos
    print(f''.center(50,'-'))
    print(f'Nodo actual: {actual_node.num_node}')   #Imprimimos el nodo actual
    print(f'Nodo: {nodes}\nRevisado:{actual_node.reviewed}\nPredecessors:{predecessors}') #Imprimimos la lista de nodos, si han sido revisados y sus predecesores
    for successor in actual_node.successors:
        if not (successor in nodes):  # Filtro para no agregar los nodos que ya se han agregado previamente
            node_cola_actual.append(successor)  # Agregamos a la cola el sucesor

    while not (len(node_cola_actual) == 0): #Ciclo hasta que se vacie la cola
        nodes_review.append(actual_node.reviewed)  # Agrega a la lista de revisiones que se ha revisado el nodo actual
        if actual_node.final: #Revisa el nodo actual es el final
            return actual_node #Si es el nodo final se regresa el nodo actual
        else:
            print(f''.center(50, '-'))
            print(f'Nodo actual: {actual_node.num_node}')  # Imprimimos el nodo actual
            print(f'Nodo: {nodes}\nRevisado:{nodes_review}\nPredecessors:{predecessors}')  # Imprimimos la lista de nodos, si han sido revisados y
            nodes_review.pop()
            actual_node.reviewed = True #Asigna el atributo de revisado al nodo actual
            nodes_review.append(actual_node.reviewed) #Agrega a la lista de revisiones que se ha revisado el nodo actual
            for successor in actual_node.successors: #Revisamos los sucesores que tiene el nodo actual
                if not (successor in nodes): #Filtro para no agregar los nodos que ya se han agregado previamente
                    nodes.append(successor) #Agregamos el sucesor del nodo a la lista de nodos
                    predecessors.append(actual_node.num_node) # Agregamos el antecesor correspondiente al sucesor por lo que agregamos el nodo actual
                    node_cola_actual.append(successor) #Agregamos a la cola el sucesor
            print(f''.center(50, '-'))
            print(f'Nodo actual: {actual_node.num_node}')  # Imprimimos el nodo actual
            print(f'Nodo: {nodes}\nRevisado:{nodes_review}\nPredecessors:{predecessors}')  # Imprimimos la lista de nodos, si han sido revisados y

            actual_node = bfs_node_list[node_cola_actual.pop(0) - 1] #Le asignamos el valor del primer sucesor a la cola
            print(f''.center(50, '-'))
            print(f'Nodo actual: {actual_node.num_node}')  # Imprimimos el nodo actual
            print(
                f'Nodo: {nodes}\nRevisado:{nodes_review}\nPredecessors:{predecessors}')  # Imprimimos la lista de nodos, si han sido revisados y sus predecesores

class Search():
    def __init__(self, ady_list: list):
        #Node list of the graph
        self.node_list = []
        for i in range(1, len(ady_list)):
            self.node_list.append(Node(i,ady_list[i][0],ady_list[i][1:]))

    def Breadth_first_search(self,num_init_node:int,num_final_node:int): #Firts searching method
        bfs_node_list = self.node_list.copy()
        init_pos = num_init_node - 1 #Initial position
        final_pos = num_final_node -1 #Final position
        init_node = bfs_node_list[init_pos]
        final_node = bfs_node_list[final_pos]
        init_node.initial = True
        final_node.final = True

        actual_node = init_node
        predecessors = []
        nodes_review = []
        nodes = []

        #Comienzo de la busqueda
        print(f'Nodo final encontrado:\n {cola_recursiva(init_node,nodes,predecessors,nodes_review,actual_node,bfs_node_list)}')

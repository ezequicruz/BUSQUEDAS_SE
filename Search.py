from Node import Node


def set_init_final_node(num_init_node: int, num_final_node: int,
                        node_list: list):  # Funcion para establecer los nodos iniciales y finales
    node_list = node_list.copy()
    init_pos = num_init_node - 1  # Initial position
    final_pos = num_final_node - 1  # Final position
    init_node = node_list[init_pos]
    final_node = node_list[final_pos]
    init_node.initial = True
    final_node.final = True
    del node_list  # Eliminamos la lista ya que no la vamos a ocupar mas
    return [init_node, final_node]


def get_nodevalues(num_init_node: int, num_final_node: int, node_values: list):
    if num_init_node > num_final_node:  # Preguntamos si el nodo inicial es mayor al final
        return node_values[num_init_node - 1][
            num_final_node - 1]  # si el nodo inicial es mayor comenzaremos la busqueda por esa fila
    return node_values[num_final_node - 1][
        num_init_node - 1]  # si el nodo final es mayor comenzaremos la busqueda por esa fila


# funcion de busqueda por cola, la funcion recibe como parametros, el nodo inicial, la lista de nodos, los antecesores, lista de nodos revisados,
# el nodo actual, la lista de todos los nodos, y la cola de sucesores
def node_cola_busqueda(init_node: Node, nodes: list, predecessors: list, nodes_review: list, actual_node: Node,
                       bfs_node_list: list):
    node_cola_actual = []  # Inicializamos la cola actual como una lista vacia
    if init_node.num_node == actual_node.num_node:  # Revisamos si nos encontramos en el nodo inicial
        predecessors.append(0)
        nodes.append(actual_node.num_node)  # Agregamos a la lista de nodos el nodo actual en el que nos encontramos
    print(f''.center(50, '-'))
    print(f'Nodo actual: {actual_node.num_node}')  # Imprimimos el nodo actual
    print(
        f'Nodo: {nodes}\nRevisado:{actual_node.reviewed}\nPredecessors:{predecessors}')  # Imprimimos la lista de nodos, si han sido revisados y sus predecesores
    for successor in actual_node.successors:
        if not (successor in nodes):  # Filtro para no agregar los nodos que ya se han agregado previamente
            node_cola_actual.append(successor)  # Agregamos a la cola el sucesor

    while not (len(node_cola_actual) == 0):  # Ciclo hasta que se vacie la cola
        nodes_review.append(actual_node.reviewed)  # Agrega a la lista de revisiones que se ha revisado el nodo actual
        if actual_node.final:  # Revisa el nodo actual es el final
            return actual_node  # Si es el nodo final se regresa el nodo actual
        else:
            print(f''.center(50, '-'))
            print(f'Nodo actual: {actual_node.num_node}')  # Imprimimos el nodo actual
            print(
                f'Nodo: {nodes}\nRevisado:{nodes_review}\nPredecessors:{predecessors}')  # Imprimimos la lista de nodos, si han sido revisados y
            nodes_review.pop()
            actual_node.reviewed = True  # Asigna el atributo de revisado al nodo actual
            nodes_review.append(
                actual_node.reviewed)  # Agrega a la lista de revisiones que se ha revisado el nodo actual
            for successor in actual_node.successors:  # Revisamos los sucesores que tiene el nodo actual
                if not (successor in nodes):  # Filtro para no agregar los nodos que ya se han agregado previamente
                    nodes.append(successor)  # Agregamos el sucesor del nodo a la lista de nodos
                    predecessors.append(
                        actual_node.num_node)  # Agregamos el antecesor correspondiente al sucesor por lo que agregamos el nodo actual
                    node_cola_actual.append(successor)  # Agregamos a la cola el sucesor
            print(f''.center(50, '-'))
            print(f'Nodo actual: {actual_node.num_node}')  # Imprimimos el nodo actual
            print(
                f'Nodo: {nodes}\nRevisado:{nodes_review}\nPredecessors:{predecessors}')  # Imprimimos la lista de nodos, si han sido revisados y

            actual_node = bfs_node_list[
                node_cola_actual.pop(0) - 1]  # Le asignamos el valor del primer sucesor a la cola


class Search():
    def __init__(self, ady_list: list, node_values: list):
        # Node list of the graph
        self.node_list = []
        for i in range(1, len(ady_list)):
            self.node_list.append(Node(i, ady_list[i][0], ady_list[i][1:]))  # Create the node list
        # Node list values with other nodes
        self.node_values = node_values.copy()

    def Breadth_first_search(self, num_init_node: int, num_final_node: int):  # Breadth-first search method
        bfs_node_list = self.node_list.copy()  # Copiamos la lista de nodos para trabajar con ella sin afectar a la lista original
        nodes_init_final = set_init_final_node(num_init_node, num_final_node,
                                               self.node_list)  # Set nodes initial and final
        final_node = nodes_init_final.pop()
        init_node = nodes_init_final.pop()
        # Set the actuall node and list for the algorithm
        actual_node = init_node
        predecessors = []
        nodes_review = []
        nodes = []
        route = []

        # Comienzo de la busqueda
        print(
            f'Nodo final encontrado:\n {node_cola_busqueda(init_node, nodes, predecessors, nodes_review, actual_node, bfs_node_list)}')  # Nodo encontrado
        # ESTABLECIMIENTO DE LA RUTA
        pred_node: int = final_node.num_node  # Comenzamos a trazar la ruta desde el nodo final
        while not (pred_node == 0):  # Mientras el nodo predecesor no sea 0 el ciclo continua
            route.append(pred_node)  # Agregamos el nodo predecesor a la ruta
            predecessor_index = nodes.index(pred_node)  # Obtenemos el indice de en donde se encuentra el predecesor
            pred_node = predecessors[
                predecessor_index]  # El predecesor se encuentra en el mismo indice de la lista de predecesores
        else:
            route.reverse()  # Invertimos la ruta para que se muestre del nodo inicial al nodo final
            return route  # Regresamos la ruta obtenida

    def Steepest_ascent_hill_climbing_search(self, num_init_node: int, num_final_node: int):
        sahcs_node_list = self.node_list.copy()  # Lista de nodos para no trabajar con la original
        sahcs_node_values = self.node_values.copy()  # Lista de los valores de los nodos para no trabajar con la original
        nodes_init_final = set_init_final_node(num_init_node, num_final_node,
                                               self.node_list)  # Set initial and final node
        final_node = nodes_init_final.pop()  # Asignamos el valor del nodo final
        init_node = nodes_init_final.pop()  # Asignamos el valor del nodo inicial
        actual_node = init_node  # Inicializamos el valor del nodo actual con el nodo inicial
        predecessors = []  # Declaramos las listas de trabajo
        values = []
        nodes = []
        route = []
        while not (actual_node == final_node):
            antecesor = actual_node.num_node  # Guardamos el valor del antecesor para colocarlo posteriormente a los sucesores
            nodes.append(actual_node.num_node)  # agregamos a la lista de nodos el nodo actual
            valor_actual = get_nodevalues(actual_node.num_node, num_final_node,
                                          sahcs_node_values)  # obtenemos el valor del nodo actual
            values.append(valor_actual)  # agregamos a la lista de valores el nodo actual
            if actual_node.num_node == num_init_node:  # Si el nodo actual es el nodo inicial su antecesor es 0
                predecessors.append(0)
            # Impresion del nodo actual
            print(''.center(50, '-'))
            print(f'Nodo actual:{actual_node.num_node}')
            print(f'Nodos:      {nodes}\n'
                  f'Valor:      {values}\n'
                  f'Antecesor:  {predecessors}')
            print(f'Lista para la ruta: {route}')
            # Limpieza de listas de trabajo
            predecessors.clear()
            values.clear()
            nodes.clear()
            # Agregamos el nodo actual a la ruta
            if actual_node.num_node == num_init_node:
                route.append([actual_node.num_node, valor_actual, 0])
            else:
                route.append([actual_node.num_node, valor_actual, antecesor])
            print(''.center(50, '-'))
            print(f'Nodo actual:{actual_node.num_node}')
            print(f'Nodos:      {nodes}\n'
                  f'Valor:      {values}\n'
                  f'Antecesor:  {predecessors}')
            print(f'Lista para la ruta: {route}')
            # Se generan los sucesores del nodo actual con sus respectivos valores
            for sucessor in actual_node.successors:
                nodes.append(sucessor)
                values.append(get_nodevalues(sucessor, num_final_node, sahcs_node_values))
                predecessors.append(actual_node.num_node)
            print(''.center(50, '-'))
            print(f'Nodo actual:{actual_node.num_node}')
            print(f'Nodos:      {nodes}\n'
                  f'Valor:      {values}\n'
                  f'Antecesor:  {predecessors}')
            print(f'Lista para la ruta: {route}')
            min_value = valor_actual  # Empezamos la busqueda de un mejor valor
            for value in values:
                if value < min_value:  # Si el valor actual es menor que el valor minimo, este se convierte en el valor minimo
                    min_value = value
            if min_value == valor_actual:  # Si ya no hay valores minimos al valor actual se termina la busqueda
                final_route = []  # y se imprime la ruta parcial
                for node in route:
                    final_route.append(node[0])
                print(''.center(50, '-'))
                return final_route
            best_sucessor = nodes[values.index(min_value)]  # se asigna el nodo que es el mejor sucesor
            actual_node = sahcs_node_list[best_sucessor - 1]  # el nodo actual se convierte en el mejor sucesor
            predecessors.clear()  # Se limpian las listas de trabajo
            values.clear()  # se limpian las listas de trabajo
            nodes.clear()
        else:  # Cuando se llego al nodo final se regresa la ruta completa desde el nodo incial hasta el final
            route.append([actual_node.num_node, valor_actual, antecesor])
            final_route = []
            for node in route:
                final_route.append(node[0])
            print(''.center(50, '-'))
            return final_route

    def Best_first_search(self, num_init_node: int, num_final_node: int):
        bfs_node_list = self.node_list.copy()  # Lista de nodos para no trabajar con la original
        bfs_node_values = self.node_values.copy()  # Lista de los valores de los nodos para no trabajar con la original
        nodes_init_final = set_init_final_node(num_init_node, num_final_node,
                                               self.node_list)  # Set initial and final node
        final_node = nodes_init_final.pop()  # Asignamos el valor del nodo final
        init_node = nodes_init_final.pop()  # Asignamos el valor del nodo inicial
        actual_node = init_node  # Inicializamos el valor del nodo actual con el nodo inicial
        # Declaramos las listas de trabajo
        predecessors = []
        nodes = [] #Nodos
        g = []     #valor de arco, valor del arco que lleva al nodo antecesor
        h = []     #valor de tabla, valor de la tabla del Nodo Actual respecto al nodo final
        f = []     #Funcion heuristica
        cerrado = [] #revisado
        route = [] #Ruta
        #Comenzamos insertando los valores del nodo inicial
        predecessors.append(0) # como es el nodo incial su predecesor es 0
        nodes.append(actual_node.num_node) #agregamos el nodo actual
        g.append(0) #Agregamos el valor de 0 ya que no tiene predecesor
        h.append(get_nodevalues(actual_node.num_node,final_node.num_node,bfs_node_values)) #Agregamos el valor del nodo inical respecto al nodo final
        indice_nodo_actual = nodes.index(actual_node.num_node) #obtenemos el indice del nodo actual
        f.append(g[indice_nodo_actual]+h[indice_nodo_actual]) # Agregamos el valor de la funcion heuristica
        cerrado.append(False) # El valor de cerrado lo asignamos como false ya que no lo hemos revisado
        #Imprimimos el primer nodo
        print(f'Nodo actual: {actual_node.num_node}')
        print(f'Antecesor\tNodo\tg + h\t = f\tCerrado')
        print(f'{predecessors}\t{nodes}\t{g} + {h}\t = {f}\t{cerrado} ')
        while not(actual_node.num_node == final_node.num_node): #Comenzamos con la busqueda
            if actual_node.num_node == init_node.num_node:
                cerrado.pop() #Quitamos el ultimo elemento de la lista de cerrado
                cerrado.append(True) #Agregamos el valor de true ya que ya lo evaluamos
            else:
                cerrado[indice_mejor_sucesor] = True
            #Imprimimos nuestra salida de la busqueda
            print(''.center(50,'-'))
            print(f'Nodo actual: {actual_node.num_node}')
            print(f'Antecesor\tNodo\tg + h\t = f\tCerrado')
            print(f'{predecessors}\t{nodes}\t{g} + {h}\t = {f}\t{cerrado} ')
            #Generar los sucesores y evaluar
            for sucessor in actual_node.successors_weights: #Asignamos los pesos de los nodos
                if not (sucessor[0] in nodes): #Filtramos que no se agreguen a la lista de nodos, aquellos que ya estaban previamente
                    predecessors.append(actual_node.num_node)   #Les agregamos como predecesor el nodo actual
                    nodes.append(sucessor[0])   #Agregamos a la lista de nodos el sucesor
                    g.append(sucessor[1])       #Agregamos el peso entre el sucesor y el nodo actual
                    h.append(get_nodevalues(sucessor[0],final_node.num_node,bfs_node_values))   #Agregamos el peso entre el sucesor y el nodo final
                    indice_nodo_actual = nodes.index(sucessor[0])   #obtenemos el indice del nodo con el que estamos trabajando
                    f.append(g[indice_nodo_actual] + h[indice_nodo_actual]) #Calculamos el valor de la funcion heuristica
                    cerrado.append(False) #Le asignamos al sucesor el valor de false
            print(''.center(50,'-'))
            print(f'Nodo actual: {actual_node.num_node}')
            print(f'Antecesor\tNodo\tg + h\t = f\tCerrado')
            print(f'{predecessors}\t{nodes}\t{g} + {h}\t = {f}\t{cerrado} ')
            #Seleccionar mejor nodo marcado como no revisado
            primer_nodo_no_revisado = cerrado.index(False)
            valor_minimo = [] #inicializamos una lista para los valores minimos
            for node in range(primer_nodo_no_revisado,len(cerrado)-1): #Recorremos los nodos que aun no han sido
                if not(cerrado[node] == True):                         #revisados y agregamos sus valores a la lista
                    valor_minimo.append(f[node])
            valor_minimo.sort()                                        #ordenamos la lista de menor a mayor
            indice_mejor_sucesor = f.index(valor_minimo[0])            #obtenemos el indice del valor minimo
            mejor_sucesor = nodes[indice_mejor_sucesor]                #obtenemos el nodo que es el mejor suscesor
            del valor_minimo                                           #eliminamos la lista de valores minimos
            actual_node = bfs_node_list[mejor_sucesor-1]               #El mejor sucesor se convierte en el nodo actual

        else:
            #Impresion del nodo final
            print('NODO ENCONTRADO'.center(50, '-'))
            print(f'Nodo actual: {actual_node.num_node}')
            print(f'Antecesor\tNodo\tg + h\t = f\tCerrado')
            print(f'{predecessors}\t{nodes}\t{g} + {h}\t = {f}\t{cerrado} ')
            print(f'Nodo encontrado : {actual_node}')
            #Establecemos la ruta
            indice_pred = nodes.index(actual_node.num_node) #Obtenemos el indice del nodo final
            antecesor = predecessors[indice_pred] #obtenemos el antecesor del nodo final
            route.append(actual_node.num_node) #Agregamos el nodo final a la ruta
            while not(antecesor == 0): #Mientras el antecesor no sea 0 continua el bucle
                route.append(antecesor) #Agregamos el antecesor a la ruta
                indice_pred = nodes.index(antecesor) #asignamos el indice del antecesor
                antecesor = predecessors[indice_pred] #Asignamos el siguiente antecesor
            route.reverse() #Invertimos el orden de la lista para que sea del nodo inicial al nodo final
            return route #Regresamos la ruta del nodo inicial al nodo final

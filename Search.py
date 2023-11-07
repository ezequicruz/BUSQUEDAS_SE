from Node import Node


class Search():
    def __init__(self, ady_list: list):
        #Node list of the graph
        self.node_list = []
        for i in range(1, len(ady_list)):
            self.node_list.append(Node(i,ady_list[i][0],ady_list[i][1:]))

    def Breadth_first_search(self,init_node:int,final_node:int): #Firts searching method
        init_pos = init_node - 1 #Initial position
        final_pos = final_node -1 #Final position
        self.node_list[init_pos].initial = True
        self.node_list[final_pos].final = True
        print(f'Nodo actual {self.node_list[init_pos].num_node}\nRevisado: ')


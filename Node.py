class Node():
    def __init__(self,num_node:int, num_successors:int,successors:list):
        self.num_node = num_node
        self.num_successors = num_successors
        self.successors = successors.copy()

    def __str__(self):
        return  f'Node: {self.num_node} | #Successors: {self.num_successors} | Successors: {self.successors}'


#Object Node
class Node():
    def __init__(self,num_node:int, num_successors:int,successors_weights:list, initial = False, final = False):
        self.num_node = num_node #Number of the node
        self.num_successors = num_successors #Number of successors
        self.successors_weights = successors_weights.copy() #Successors with them weights
        #Add only the successors without their weights
        self.successors =[]
        for successor in successors_weights:
            self.successors.append(successor[0])
        self.initial = initial #True if the node is initial. False as deafault value
        self.final = final #True if the node is final. False as default value

    def __str__(self): #Overwriting the method str
        return  f'Node: {self.num_node} | #Successors: {self.num_successors} | Successors: {self.successors}'

print("TEST NODE".center(50,'-'))
Node1 = Node(1,3,[[6,117],[13,699],[4,701]])
print(Node1)
print(len(Node1.successors))
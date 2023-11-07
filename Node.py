class Node():
    def __init__(self,num_node:int, num_successors:int,successors:list):
        self.num_node = num_node
        self.num_successors = num_successors
        self.successors = successors.copy()

    def __str__(self):
        return  f'Node: {self.num_node} | #Successors: {self.num_successors} | Successors: {self.successors}'
print("TEST NODE".center(50,'-'))
Node1 = Node(1,3,[6,13,4])
print(Node1)
print(len(Node1.successors))
# while node is not None:
#     for 


#     is the stack empty?
#         No?
#         pop off the top of the stackame

#         have we been here before?
#             no?
#                 mark as visited add to set
#                 put its neighbors on the stack
#             yes?
#                 is the stack empty?
#                     no?
#                 pop the top of stack

# using the stack allows us to do teh depth first traversal

# it could go depth all the way to the right
# or all the way to the down the
# or all the way to one end before backing up one node and going the other way



def dft(start_node):
    stack=[]
stack_len=len(stack)-1
    visited_nodes=()

    while stack is not None:
        curr_node is stack[stack_len]
        curr_node is not in visited_nodes
            visited_nodes.append(curr_node)

            neightbors= currnode.neightbors

            for neighbor in neighbors:
                stack.push(neighbor)

def bft(start_node):
    visited_nodes(set)
    #dont forget to prime the pump aka give a first node or start node so it doesnt end the while loop prematurely
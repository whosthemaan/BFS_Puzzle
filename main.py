# test case 1

start_state = [1,6,7], [2,0,5], [4,3,8]
goal_status = [1,4,7], [2,5,8], [3,0,6]

# test case 2

# start_state = [4,7,8], [2,1,5], [3,6,0]
# goal_status = [1,4,7], [2,5,8], [3,6,0]

def convert_to_required(start_state, goal_status):
    initial_state = []
    goal_state = []

    for i in range(3):
        for j in range(3):
            initial_state.append(start_state[j][i])

    for i in range(3):
        for j in range(3):
            goal_state.append(goal_status[j][i])

    return initial_state, goal_state            

def write_nodes(path, Node_State_i, NodesInfo):
    file =  open("nodePath.txt", "w+")
    for i in range(len(path)):
        for j in [0,3,6,1,4,7,2,5,8]:
            file.write(str(path[i][j]))
            file.write(" ")
        file.write("\n")
    file.close()

    file = open("Nodes.txt", "w+")
    for i in range(len(Node_State_i)):
        for j in range(len(Node_State_i[0])):
            file.write(str(Node_State_i[i][j]))
            file.write(" ")
        file.write("\n")
    file.close()

    file = open("NodesInfo.txt", "w+")
    for i in range(len(NodesInfo)):
        file.write(str(NodesInfo[i]))
        file.write("\n")
    file.close()

def swap(node, idx, next_idx):
    node[idx], node[next_idx] = node[next_idx], node[idx]
    return node

def give_state(node):
    tile_col = int(node.index(0)%3) + 1
    tile_row = int(node.index(0)/3) + 1
    pair = (tile_row, tile_col)
    return pair

def moveLeft(node):
    position = give_state(node)
    idx = node.index(0)
    if(position[1]==1):
        status = False
        NewNode = node
        # print("Cannot move tile anymore Left")
    else:
        status = True
        NewNode = swap(node.copy(), idx, idx-1)

    return status, NewNode

def moveRight(node):
    position = give_state(node)
    idx = node.index(0)
    if(position[1]==3):
        status = False
        NewNode = node
        # print("Cannot move tile anymore Right")
    else:
        status = True
        NewNode = swap(node.copy(), idx, idx+1)
    return status, NewNode

def moveUp(node):
    position = give_state(node)
    idx = node.index(0)
    if(position[0]==1):
        status = False
        NewNode = node
        # print("Cannot move tile anymore Up")
    else:
        status = True
        NewNode = swap(node.copy(), idx, idx-3)
    return status, NewNode

def moveDown(node):
    position = give_state(node)
    idx = node.index(0)
    if(position[0]==3):
        status = False
        NewNode = node
        # print("Cannot move tile anymore Down")
    else:
        status = True
        NewNode = swap(node.copy(), idx, idx+3)
    return status, NewNode

def generate_path(Node_State_i, nodes_info):
    path = []
    path.append(Node_State_i[-1])

    parent_index = len(Node_State_i)

    while(path[-1]!=Node_State_i[0]):
        parent_index = nodes_info[parent_index-1][1]
        val = nodes_info[parent_index-1][2]
        path.append(val)

    path.reverse()
    return path

def find_possible_states(initial_state, goal_state):
    Node_State_i = []
    nodes_info = []

    Node_State_i.append(initial_state)
    nodes_info.append([1, 0, initial_state])

    Node_Index_i = 2
    Parent_Node_Index_i = 0

    current_node = initial_state.copy()

    while(1):
        status, NewNode = moveLeft(current_node.copy())
        if(status==True and NewNode not in Node_State_i):
            Node_State_i.append(NewNode)
            nodes_info.append([Node_Index_i, Parent_Node_Index_i+1, NewNode])
            Node_Index_i = Node_Index_i + 1
            if(NewNode == goal_state):
                break

        status, NewNode = moveUp(current_node.copy())
        if(status==True and NewNode not in Node_State_i):
            Node_State_i.append(NewNode)
            nodes_info.append([Node_Index_i, Parent_Node_Index_i+1, NewNode])
            Node_Index_i = Node_Index_i + 1
            if(NewNode == goal_state):
                break

        status, NewNode = moveRight(current_node.copy())
        if(status==True and NewNode not in Node_State_i):
            Node_State_i.append(NewNode)
            nodes_info.append([Node_Index_i, Parent_Node_Index_i+1, NewNode])
            Node_Index_i = Node_Index_i + 1
            if(NewNode == goal_state):
                break

        status, NewNode = moveDown(current_node.copy())
        if(status==True and NewNode not in Node_State_i):
            Node_State_i.append(NewNode)
            nodes_info.append([Node_Index_i, Parent_Node_Index_i+1, NewNode])
            Node_Index_i = Node_Index_i + 1
            if(NewNode == goal_state):
                break

        Parent_Node_Index_i = Parent_Node_Index_i + 1
        current_node = Node_State_i[Parent_Node_Index_i]

    return Node_State_i, nodes_info

initial_state, goal_state = convert_to_required(start_state, goal_status)
Node_State_i, nodes_info = find_possible_states(initial_state, goal_state)
path = generate_path(Node_State_i, nodes_info)
write_nodes(path, Node_State_i, nodes_info)

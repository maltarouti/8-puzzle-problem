import time
from Queue import Queue
from PriorityQueue import PriorityQueue
from tree import tree, node, normal_node


class puzzle:
    # initialize the initial and goal state:
    def __init__(self):
        self.initial_state = []
        self.goal_state = []

    # helper method: reset everything
    def restart(self):
        self.initial_state.clear()
        self.goal_state.clear()

    # helper method: get 0 number index:
    def get_index(self, state, number):
        number = str(number)
        for x in range(len(state)):
            for y in range(len(state[x])):
                if(state[x][y] == number):
                    return (x, y,)

    # helper method: copy the 2d array:
    def copy_array(self, array):
        return list(map(list, array))

    # helper method: convert 2D to 1D
    def convertToList(self, array):
        temp = []
        for x in array:
            for y in x:
                temp.append(y)
        return temp

    # helper method: return initial/goal states as string:
    def get_states(self):
        string = ""
        string += "Initial State:\n"
        for state in self.initial_state:
            string += state[0] + " "+state[1]+" "+state[2]+"\n"
        string += "\n"

        string += "Goal State:\n"
        for state in self.goal_state:
            string += state[0] + " "+state[1]+" "+state[2]+"\n"
        string += "\n"
        return string

    # get_path: return the path as string of a given node:
    def get_path(self, node):
        path = []
        while(node.parent != None):
            path.append(node.data)
            node = node.parent
        path = path[::-1]
        string = ""
        for state in path:
            for row in state:
                string += row[0] + " "+row[1]+" "+row[2]+"\n"
            string += "\n"
        return string

    # read initial and goal state:
    def read_input(self, file_name):
        with open(file_name, 'r') as f:
            for x in range(7):
                temp = f.readline()
                temp = temp.replace(" ", "")
                temp = temp.replace("-", "0")
                temp = temp.replace("\n", "")
                row = []
                for x in temp:
                    if(len(row) != 3):
                        row.append(x)
                if(len(row) == 0):
                    pass
                elif(len(self.initial_state) != 3):
                    self.initial_state.append(row)
                elif(len(self.goal_state) != 3):
                    self.goal_state.append(row)

    # write the output:
    def write_output(self, file_name, data):
        string = self.get_states()
        string += data
        with open(file_name, "w") as f:
            f.write(string)

    # Successor function UP/DOWN & RIGHT/LEFT:
    def movements(self, current_state):
        location = self.get_index(current_state, "0")
        new_states = []

        # CORNER CASES:
        if (location == (0, 0)):
            # down
            temp = self.copy_array(current_state)
            temp[0][0] = temp[1][0]
            temp[1][0] = "0"
            new_states.append(temp)
            # right
            temp = self.copy_array(current_state)
            temp[0][0] = temp[0][1]
            temp[0][1] = "0"
            new_states.append(temp)
        elif(location == (0, 2)):
            # down
            temp = self.copy_array(current_state)
            temp[0][2] = temp[1][2]
            temp[1][2] = "0"
            new_states.append(temp)
            # left
            temp = self.copy_array(current_state)
            temp[0][2] = temp[0][1]
            temp[0][1] = "0"
            new_states.append(temp)
        elif(location == (2, 0)):
            # up
            temp = self.copy_array(current_state)
            temp[2][0] = temp[1][0]
            temp[1][0] = "0"
            new_states.append(temp)
            # right
            temp = self.copy_array(current_state)
            temp[2][0] = temp[2][1]
            temp[2][1] = "0"
            new_states.append(temp)
        elif(location == (2, 2)):
            # up
            temp = self.copy_array(current_state)
            temp[2][2] = temp[1][2]
            temp[1][2] = "0"
            new_states.append(temp)
            # left
            temp = self.copy_array(current_state)
            temp[2][2] = temp[2][1]
            temp[2][1] = "0"
            new_states.append(temp)

        # MIDDLE CASES:
        elif(location == (1, 0)):
            # up
            temp = self.copy_array(current_state)
            temp[1][0] = temp[0][0]
            temp[0][0] = "0"
            new_states.append(temp)
            # down
            temp = self.copy_array(current_state)
            temp[1][0] = temp[2][0]
            temp[2][0] = "0"
            new_states.append(temp)
            # right
            temp = self.copy_array(current_state)
            temp[1][0] = temp[1][1]
            temp[1][1] = "0"
            new_states.append(temp)
        elif(location == (1, 2)):
            # up
            temp = self.copy_array(current_state)
            temp[1][2] = temp[0][2]
            temp[0][2] = "0"
            new_states.append(temp)
            # down
            temp = self.copy_array(current_state)
            temp[1][2] = temp[2][2]
            temp[2][2] = "0"
            new_states.append(temp)
            # left
            temp = self.copy_array(current_state)
            temp[1][2] = temp[1][1]
            temp[1][1] = "0"
            new_states.append(temp)
        elif(location == (0, 1)):
            # down
            temp = self.copy_array(current_state)
            temp[0][1] = temp[1][1]
            temp[1][1] = "0"
            new_states.append(temp)
            # right
            temp = self.copy_array(current_state)
            temp[0][1] = temp[0][2]
            temp[0][2] = "0"
            new_states.append(temp)
            # left
            temp = self.copy_array(current_state)
            temp[0][1] = temp[0][0]
            temp[0][0] = "0"
            new_states.append(temp)
        elif(location == (2, 1)):
            # up
            temp = self.copy_array(current_state)
            temp[2][1] = temp[1][1]
            temp[1][1] = "0"
            new_states.append(temp)
            # right
            temp = self.copy_array(current_state)
            temp[2][1] = temp[2][2]
            temp[2][2] = "0"
            new_states.append(temp)
            # left
            temp = self.copy_array(current_state)
            temp[2][1] = temp[2][0]
            temp[2][0] = "0"
            new_states.append(temp)

        # CENTER CASE:
        elif(location == (1, 1)):
            # up
            temp = self.copy_array(current_state)
            temp[1][1] = temp[0][1]
            temp[0][1] = "0"
            new_states.append(temp)
            # down
            temp = self.copy_array(current_state)
            temp[1][1] = temp[2][1]
            temp[2][1] = "0"
            new_states.append(temp)
            # right
            temp = self.copy_array(current_state)
            temp[1][1] = temp[1][2]
            temp[1][2] = "0"
            new_states.append(temp)
            # left
            temp = self.copy_array(current_state)
            temp[1][1] = temp[1][0]
            temp[1][0] = "0"
            new_states.append(temp)
        return new_states

    # helper method: count the estimated cost f(n) for A* strategy:
    def estimated_cost(self, state):
        estimated_cost = 0
        current_state = self.convertToList(state)
        goal = self.convertToList(self.goal_state)

        # missed tiles:
        for x in range(len(current_state)):
            if(current_state[x] == goal[x] or current_state[x] == "0"):
                continue
            else:
                estimated_cost += 1

        # manhattan distance:
        for x in range(len(state)):
            for y in range(len(state[x])):
                if(state[x][y] != self.goal_state[x][y] and state[x][y] != "0"):
                    correct_index = self.get_index(
                        self.goal_state, state[x][y])
                    manhattan = abs(
                        x-correct_index[0]) + abs(y-correct_index[1])
                    estimated_cost += manhattan
        return estimated_cost

    # A* strategy:
    def A(self):
        A_tree = tree(self.initial_state)
        frontier = PriorityQueue(False)
        frontier.enqueue(A_tree.root)
        visited = []
        goal_node = None
        while(frontier.size != 0):
            temp = frontier.pop()

            if(self.goal_state == temp.data):
                print("Count of expanded nodes: ", len(visited))
                return temp

            adj = self.movements(temp.data)
            for state in adj.copy():
                for temp_node in visited:
                    if(state == temp_node.data):
                        adj.remove(state)
                        break

            for state in adj:
                cost = self.estimated_cost(state)
                adj_node = node(state, cost, temp)
                adj_node.cost = adj_node.cost + adj_node.parent.cost
                temp.adj.append(adj_node)
                frontier.enqueue(adj_node)

            visited.append(temp)

    # BFS strategy:
    def BFS(self):
        BFS_tree = tree(self.initial_state, False)
        frontier = Queue()
        frontier.enqueue(BFS_tree.root)
        visited = []
        goal_node = None

        while(frontier.size != 0):
            temp = frontier.pop()

            if(self.goal_state == temp.data):
                print("Count of expanded nodes: ", len(visited))
                return temp

            adj = self.movements(temp.data)
            for state in adj.copy():
                for temp_node in visited:
                    if(state == temp_node.data):
                        adj.remove(state)
                        break

            for state in adj:
                adj_node = normal_node(state, temp)
                temp.adj.append(adj_node)
                frontier.enqueue(adj_node)

            visited.append(temp)


if __name__ == "__main__":
    puzzle = puzzle()

    # Read and Solve sample 1:
    puzzle.read_input("input_sample1.txt")

    print("Started Solving Sample 1 using A*")
    # Solve by using A*:
    start_time = time.time()
    A_solution = puzzle.A()
    end_time = time.time()
    A_time = round((end_time - start_time), 5)
    print("Finished solving Sample 1 using A*. Time Cost: {}".format(A_time))

    print("Started Solving Sample 1 using BFS")
    # Solve by using BFS:
    start_time = time.time()
    BFS_solution = puzzle.BFS()
    end_time = time.time()
    BFS_time = round((end_time - start_time), 5)
    print("Finished solving Sample 1 using BFS. Time Cost: {}".format(BFS_time))

    puzzle.write_output("output_sample1.txt", "A* \ntime: {} seconds\n{} \nBFS \ntime: {} seconds\n{}".format(
        A_time, puzzle.get_path(A_solution), BFS_time, puzzle.get_path(BFS_solution)))

    puzzle.restart()
    # Read and Solve sample 2:
    puzzle.read_input("input_sample2.txt")

    print("Started Solving Sample 2 using A*")
    # Solve by using A*:
    start_time = time.time()
    A_solution = puzzle.A()
    end_time = time.time()
    A_time = round((end_time - start_time), 5)
    print("Finished solving Sample 1 using A*. Time Cost: {}".format(A_time))

    print("Started Solving Sample 2 using BFS")
    # Solve by using BFS:
    start_time = time.time()
    BFS_solution = puzzle.BFS()
    end_time = time.time()
    BFS_time = round((end_time - start_time), 5)
    print("Finished solving Sample 2 using BFS. Time Cost: {}".format(BFS_time))

    puzzle.write_output("output_sample2.txt", "A* \ntime: {} seconds\n{} \nBFS \ntime: {} seconds\n{}".format(
        A_time, puzzle.get_path(A_solution), BFS_time, puzzle.get_path(BFS_solution)))

    puzzle.restart()
    # Read and Solve sample 3:
    puzzle.read_input("input_sample3.txt")

    print("Started Solving Sample 3 using A*")
    # Solve by using A*:
    start_time = time.time()
    A_solution = puzzle.A()
    end_time = time.time()
    A_time = round((end_time - start_time), 5)
    print("Finished solving Sample 3 using A*. Time Cost: {}".format(A_time))

    print("Started Solving Sample 3 using BFS")
    # Solve by using BFS:
    start_time = time.time()
    BFS_solution = puzzle.BFS()
    end_time = time.time()
    BFS_time = round((end_time - start_time), 5)
    print("Finished solving Sample 3 using BFS. Time Cost: {}".format(BFS_time))

    puzzle.write_output("output_sample3.txt", "A* \ntime: {} seconds\n{} \nBFS \ntime: {} seconds\n{}".format(
        A_time, puzzle.get_path(A_solution), BFS_time, puzzle.get_path(BFS_solution)))

    print("Finished.")
    time.sleep(180)

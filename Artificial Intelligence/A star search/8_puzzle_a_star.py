"""
    A* Star
---------------

=> Complete, Optimal, O(b^d)

"""
# I have put a comment on where you need to write the code.
import copy
import queue
from math import sqrt

initial_state = [[1, 5, 4],
                 [8, 2, -1],
                 [3, 7, 6]]

# initial_state = [[1, 4, 2],
#                  [3, 5, -1],
#                  [6, 7, 8]]

# initial_state = [[3, 1, 2],
#                  [6, 4, 5],
#                  [7, 8, -1]]

final_state = [[-1, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]


class State(object):  # don't change this class
    def __init__(self, matrix):
        self.matrix = matrix
        self.f = 0
        self.g = 0
        self.h = 0

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return str(self.matrix[0]) + "\n" + str(self.matrix[1]) + "\n" + str(self.matrix[2])


def create_child(parent_state, move):
    i = 0
    j = 0
    found = False
    matrix = copy.deepcopy(parent_state)
    for i in range(len(parent_state)):
        for j in range(len(parent_state[i])):
            if parent_state[i][j] == -1:
                found = True
                break
        if found:
            break

    if move == "left":
        # write code for the left move from the parent state and
        # check whether it's a valid move. for invalid move return -1
        left = j - 1
        if left < 0:
            return -1

        # swap values
        matrix[i][j], matrix[i][left] = matrix[i][left], matrix[i][j]
        return matrix

    if move == "right":
        # write code for the right move from the parent state and
        # check whether it's a valid move for invalid move return -1
        right = j + 1
        if right >= len(matrix[0]):
            return -1

        matrix[i][j], matrix[i][right] = matrix[i][right], matrix[i][j]
        return matrix

    if move == "up":
        # write code for the up move from the parent state and return
        # check whether it's a valid move. for invalid move return -1
        up = i - 1
        if up < 0:
            return -1

        matrix[i][j], matrix[up][j] = matrix[up][j], matrix[i][j]
        return matrix

    if move == "down":
        # write code for the down move from the parent state and
        # check whether it's a valid move. for invalid move return -1
        down = i + 1
        if down >= len(matrix):
            return -1

        matrix[i][j], matrix[down][j] = matrix[down][j], matrix[i][j]
        return matrix


def heuristic1(current_matrix):
    distance = 0

    for i in range(len(current_matrix)):
        for j in range(len(current_matrix[i])):
            if current_matrix[i][j] != final_state[i][j]:
                distance += 1

    return distance


def calc_manhattan(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def find_idxs(matrix, element):
    for i, x in enumerate(matrix):
        if element in x:
            return (i, x.index(element))


def heuristic2(current_matrix):
    distance = 0
    # write code for heuristic two: sum of euclidean distances
    for i in range(len(current_matrix)):
        for j in range(len(current_matrix[i])):
            fi, fj = find_idxs(final_state, current_matrix[i][j])
            distance += calc_manhattan(fi, fj, i, j)

    return distance


def a_star(initial_state, final_state):
    unexplored = queue.PriorityQueue()
    explored = []
    current_state = State(initial_state)
    current_state.g = 0
    current_state.h = heuristic1(current_state.matrix)
    current_state.f = current_state.g + current_state.h
    unexplored.put(current_state, current_state.f)
    explored.append(current_state)

    while not unexplored.empty():

        possible_movements = ["up", "left", "down", "right"]
        current_state = unexplored.get()

        for move in possible_movements:

            if current_state.g > 31:
                print("Moves Exceeded")
                exit(0)
            new_matrix = create_child(current_state.matrix, move)
            # print(f"{move}: {new_matrix}", end='\n\n')

            if new_matrix != -1:

                if new_matrix == final_state:
                    print(f"Number of moves: {current_state.g}")
                    exit(0)
                else:
                    state = State(new_matrix)
                    state.g = current_state.g + 1
                    state.h = heuristic1(state.matrix)
                    state.f = state.g + state.h
                    if(state not in explored):
                        explored.append(state)
                        unexplored.put(state, state.f)


a_star(initial_state, final_state)

from collections import deque

GOAL = [['X', 1, 2], [3, 4, 5], [6, 7, 8]]


class State(object):

    def __init__(self, state, parent=None):
        self.state = state
        self.children = []
        self.parent = parent

    def is_goal(self):
        return self.state == GOAL

    def index_of_x(self):
        for i in range(0, len(self.state)):
            if self.state[i] == 'X':
                return i/3, i%3

    def is_valid_state(self, index):
        return index[0] in (0, 1, 2) and index[1] in (0, 1, 2)

    def generate_children(self):
        x_row, x_col = self.index_of_x()
        moves = [(x_row + 1, x_col), (x_row, x_col + 1), (x_row - 1, x_col), (x_row, x_col - 1)]
        filter(State.is_valid_state, moves)

    def get_children(self):
        if not self.children:
            self.children = self.generate_children()
        return self.children

    def solve(self):
        queue = deque()
        queue.append(self.state)
        while not queue.isEmpty():
            current = queue.popleft()
            if current.is_goal():
                # possible print
                return current
            deque.extend(current.get_children())
from collections import deque

GOAL = "X12345678"


def swap(state, current_pos, new_pos):
    pass


class State(object):

    def __init__(self, state, parent=None):
        self.state = state
        self.children = []
        self.parent = parent

    def is_goal(self):
        # return goal.distance == 0
        return self.state == GOAL

    def index_of_x(self):
        for i in range(0, len(self.state)):
            if self.state[i] == 'X':
                return i

    @staticmethod
    def is_valid_state(index):
        return index[0] in (0, 1, 2) and index[1] in (0, 1, 2)

    def generate_children(self):
        x_row, x_col = self.index_of_x()
        moves = [(x_row + 1, x_col), (x_row, x_col + 1), (x_row - 1, x_col), (x_row, x_col - 1)]
        filter(State.is_valid_state, moves)
        return [State(swap(self.state(x_row, x_col), move))for move in mooves]

    def compare(self, other_state):
        return self.distance - other_state.distance

    def get_position(self, element):
        for i in range(0, len(self.state)):
            if self.state[i] == element:
                return i

    @property
    def distance(self):
        distance = 0
        for i in range(0, len(GOAL)):
            pos = self.get_position(GOAL[i])
            x = (i % 3) - (pos % 3)
            y = (i / 3) - (pos / 3)
            distance += x + y
        return distance

    def get_children(self):
        if not self.children:
            self.children = self.generate_children()
        return self.children

    def solve(self):
        # use priority queue for weight
        queue = deque()
        queue.append(self.state)
        while not queue.isEmpty():
            current = queue.popleft()
            if current.is_goal():
                # possible print
                return current
            deque.extend(current.get_children())

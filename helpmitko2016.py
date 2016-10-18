from collections import deque


GOAL = None
ROWS, COLUMNS = 4, 5


class Node(object):

    def __init__(self, state, parent=None):
        self.mitko = state
        self.parent = parent
        self.children = None

    @classmethod
    def is_valid(cls, state):
        valid = state[0] >= 0 and state[1] >= 0
        valid = valid and state[0] < ROWS and state[1] < COLUMNS
        return valid

    def get_next(self):
        x, y = self.state
        moves = [(x, y+1), (x, y-1), (x+1, y), (x-1, y), (x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)]
        if not self.children:
            self.children.extend([Node(move) for move in filter(Node.is_valid, moves)])
        return self.children

    @staticmethod
    def get_distance(state):
        '''
        Possibility for more intelligent heuristics like considering diagonal moves and hurdles.
        ex. (x_distance + y_distance) * 1,5
        '''
        x_distance = abs(GOAL[0] - state[0])
        y_distance = abs(GOAL[1] - state[1])
        return x_distance + y_distance

    def solve(self, start):
        start_node = Node(start)
        queue = deque()
        queue.push(start_node)
        while queue:
            current = queue.popleft()
            if not current.get_distance():
                return current
            queue.extend(current.get_next())
            queue = sorted(key=lambda node: node.get_distance())
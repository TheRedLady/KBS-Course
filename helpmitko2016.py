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

    def get_cost(self):
        # if self.state.x == child.state.x || self.state.y == child.state.y: cost is 1
        # check terrain
        # if move is water : cost is 2
        # if diagonal move: cost is 1.5
        pass

    @staticmethod
    def get_distance(state):
        '''
        Possibility for more intelligent heuristics like considering diagonal moves and hurdles.
        ex. (x_distance + y_distance) * 1,5
        '''
        x_distance = abs(GOAL[0] - state[0])
        y_distance = abs(GOAL[1] - state[1])
        return x_distance + y_distance
        # abs(x_distance, y_distance) + sqrt(2 * min(x_distance, y_distance)^2) * 1,5

    def solve(self, start):
        visited = set()
        start_node = Node(start)
        queue = deque()
        # queue.push(start_node.get_cost + start_node.get_distance)
        queue.push(start_node)
        while queue:
            current = queue.popleft()
            visited.add(current)
            if not current.get_distance():
                return current
            if current in visited:
                continue
            # open and closed for nodes
            # algorithm not full
            # second option: filter open children
            # third option: queue contains pairs of node and priority/cost
            queue.extend(current.get_next())
            # third option: key node: node.get_cost + node.get_distance
            queue = sorted(key=lambda node: node.get_distance())

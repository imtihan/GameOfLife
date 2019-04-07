# Controller that starts the game and updates the state and board
from Board import *


class GameController(object):

    def __init__(self, params = {}):
        self.board = Board()
        return



import random


class PassageGame:
    def __init__(self):
        self.board = []
        self.objectBoard = []
        self.playerRed = {"name": "", "toBot": False, "movePriority": 0, "color": "red", "endpoint": -1}
        self.playerBlue = {"name": "", "toBot": False, "movePriority": 0, "color": "blue", "endpoint": -1}
        self.playerGreen = {"name": "", "toBot": False, "movePriority": 0, "color": "green", "endpoint": -1}
        self.playerYellow = {"name": "", "toBot": False, "movePriority": 0, "color": "yellow", "endpoint": -1}
        self.playersDict = {"red": self.playerRed, "blue": self.playerBlue, "green": self.playerGreen,
                            "yellow": self.playerYellow}
        self.queueOfPlayers = []
        self.ChipR1 = {"color": "red", "condition": "noActive", "steps": 0, "index": -1, "tag": 0}
        self.ChipR2 = {"color": "red", "condition": "noActive", "steps": 0, "index": -1, "tag": 1}
        self.ChipR3 = {"color": "red", "condition": "noActive", "steps": 0, "index": -1, "tag": 2}
        self.ChipB1 = {"color": "blue", "condition": "noActive", "steps": 0, "index": -1, "tag": 0}
        self.ChipB2 = {"color": "blue", "condition": "noActive", "steps": 0, "index": -1, "tag": 1}
        self.ChipB3 = {"color": "blue", "condition": "noActive", "steps": 0, "index": -1, "tag": 2}
        self.ChipG1 = {"color": "green", "condition": "noActive", "steps": 0, "index": -1, "tag": 0}
        self.ChipG2 = {"color": "green", "condition": "noActive", "steps": 0, "index": -1, "tag": 1}
        self.ChipG3 = {"color": "green", "condition": "noActive", "steps": 0, "index": -1, "tag": 2}
        self.ChipY1 = {"color": "yellow", "condition": "noActive", "steps": 0, "index": -1, "tag": 0}
        self.ChipY2 = {"color": "yellow", "condition": "noActive", "steps": 0, "index": -1, "tag": 1}
        self.ChipY3 = {"color": "yellow", "condition": "noActive", "steps": 0, "index": -1, "tag": 2}
        self.DictChips = {"red": (self.ChipR1, self.ChipR2, self.ChipR3),
                          "blue": (self.ChipB1, self.ChipB2, self.ChipB3),
                          "green": (self.ChipG1, self.ChipG2, self.ChipG3),
                          "yellow": (self.ChipY1, self.ChipY2, self.ChipY3)}


    def diceRoll(self):
        return random.randint(1, 6)

    def nameInput(self, name, color):
        self.playersDict[color]["name"] = name

    def toBot(self, color, value):
        if value:
            self.playersDict[color]["toBot"] = True
        else:
            self.playersDict[color]["toBot"] = False


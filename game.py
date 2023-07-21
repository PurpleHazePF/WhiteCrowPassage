import sys
from main import PassageGame
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from random import randint
import sqlite3

SCREEN_SIZE = [800, 600]

con = sqlite3.connect("mapCoords")
cur = con.cursor()
result = cur.execute("""SELECT * FROM coords """).fetchall()


class CrowGame(QMainWindow, PassageGame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, *SCREEN_SIZE)
        self.setWindowTitle('White Crow Passage')
        self.setFixedSize(800, 650)
        self.mapC = []
        self.mapNames = ["-", "classic1.png", "eternityRun1.png", "cicles1.png", "portalGame.png"]
        self.leaderboardButton = QtWidgets.QPushButton(self)
        self.leaderboardButton.setGeometry(QtCore.QRect(120, 170, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.leaderboardButton.setFont(font)
        self.leaderboardButton.setObjectName("leaderboardButton")
        self.leaderboardButton.setText("Cписки лидеров")
        self.leaderboardButton.hide()
        self.startButton = QtWidgets.QPushButton(self)
        self.startButton.setGeometry(QtCore.QRect(120, 160, 221, 61))
        font3 = QtGui.QFont()
        font3.setPointSize(9)
        font4 = QtGui.QFont()
        font4.setPointSize(14)
        self.HowTo = QLabel(self)
        self.HowTo.setText(
            "Расслабьтесь, обязательно позовите друзей\nПо очереди кидайте кости\nпобедит тот, кто первый доведёт все 3 фишки до финиша")
        self.HowTo.move(200, 400)
        self.HowTo.resize(570, 120)
        self.HowTo.setFont(font4)
        self.HowTo.hide()
        self.welcomlabel = QLabel(self)
        self.welcomlabel.setGeometry(QtCore.QRect(450, 230, 350, 91))
        self.welcomlabel.setFont((font3))
        self.welcomlabel.setText(
            "Белая ворона большая редкость в природе\nкто знает, куда вас может привести эта птица")
        font1 = QtGui.QFont()
        font1.setPointSize(24)
        font2 = QtGui.QFont()
        font2.setPointSize(14)
        self.startButton.setFont(font1)
        self.startButton.setObjectName("startButton")
        self.startButton.setText("Старт")
        self.trainingButton = QtWidgets.QPushButton(self)
        self.trainingButton.setGeometry(QtCore.QRect(120, 230, 221, 51))
        self.trainingButton.setFont(font)
        self.trainingButton.setObjectName("trainingButton")
        self.trainingButton.setText("Как играть?")
        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setGeometry(QtCore.QRect(120, 300, 221, 61))
        self.exitButton.setText("Выход")
        self.exitButton.setFont(font)
        self.continueBtn = QtWidgets.QPushButton(self)
        self.continueBtn.setGeometry(QtCore.QRect(200, 200, 400, 120))
        self.continueBtn.setFont(font)
        self.continueBtn.setText("Продолжить игру")
        self.newGame = QtWidgets.QPushButton(self)
        self.newGame.setGeometry(QtCore.QRect(200, 230, 400, 120))
        self.newGame.setFont(font)
        self.newGame.setText("Новая игра")
        self.newGame.hide()
        self.continueBtn.hide()
        self.chooseLabel = QLabel(self)
        self.chooseLabel.setText("      Куда отправимся?")
        self.chooseLabel.move(200, 5)
        self.chooseLabel.resize(670, 100)
        self.chooseLabel.setFont(font1)
        self.chooseLabel.hide()
        self.crowPicture = QLabel(self)
        self.crowPicture.setPixmap(QPixmap("whiteCrow.png"))
        self.crowPicture.resize(295, 249)
        self.crowPicture.move(505, 0)
        self.miniClassic = QLabel(self)
        self.miniClassic.hide()
        self.menuButton = QtWidgets.QPushButton(self)
        self.menuButton.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.menuButton.setFont(font)
        self.menuButton.setText("←")
        self.menuButton.hide()
        self.minimap = QLabel(self)
        self.minimap.setPixmap(QPixmap("miniMaps.png"))
        self.minimap.setGeometry(QtCore.QRect(0, 50, 800, 200))
        self.minimap.hide()
        x = 0
        self.test = []
        self.desctxt = ["Классика", "Бесконечные бега", "Циклы", "Портальная игра"]
        self.cBtns = []
        for i in range(4):
            self.desc = QLabel(self)
            self.desc.setText(self.desctxt[i])
            self.desc.resize(200, 40)
            self.desc.setFont(font2)
            self.desc.move(10 + x, 290)
            self.desc.hide()
            self.test.append(self.desc)
            self.minimap2 = QLabel(self)
            self.miniBtn = QPushButton(self)
            self.miniBtn.setText("▶")
            self.miniBtn.setFont(font)
            self.miniBtn.setGeometry(QtCore.QRect(10 + x, 250, 180, 40))
            self.miniBtn.hide()
            self.cBtns.append(self.miniBtn)
            x += 200
        self.nMap = 0
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(QtCore.QRect(10, 250, 180, 35))
        self.name_input.setFont(font2)
        self.name_input2 = QLineEdit(self)
        self.name_input2.setGeometry(QtCore.QRect(210, 250, 180, 35))
        self.name_input2.setFont(font2)
        self.name_input3 = QLineEdit(self)
        self.name_input3.setFont(font2)
        self.name_input3.setGeometry(QtCore.QRect(410, 250, 180, 35))
        self.name_input3.setFont(font2)
        self.name_input4 = QLineEdit(self)
        self.name_input4.setGeometry(QtCore.QRect(610, 250, 180, 35))
        self.name_input4.setFont(font2)
        self.miniChips = QLabel(self)
        self.miniChips.setPixmap(QPixmap("nChips.png"))
        self.miniChips.setGeometry(QtCore.QRect(0, 200, 800, 40))
        self.readyButton = QPushButton(self)
        self.readyButton.setGeometry(QtCore.QRect(580, 530, 200, 100))
        self.readyButton.setFont(font2)
        self.readyButton.setText("Готово")
        self.ready = [self.name_input, self.name_input2, self.name_input3, self.name_input4, self.readyButton,
                      self.miniChips]
        self.nicknames = [self.name_input, self.name_input2, self.name_input3, self.name_input4]
        for i in self.ready:
            i.hide()
        self.cNumber = 0
        self.turn = 0
        self.cubics = [0, 0]
        self.dice1 = QLabel(self)
        self.dice1.setPixmap(QPixmap("diceR1.png"))
        self.dice1.resize(80, 80)
        self.dice1.move(0, 560)
        self.dice2 = QLabel(self)
        self.dice2.setPixmap(QPixmap("diceR2.png"))
        self.dice2.resize(80, 80)
        self.dice2.move(0, 560)
        self.dice3 = QLabel(self)
        self.dice3.setPixmap(QPixmap("diceR3.png"))
        self.dice3.resize(80, 80)
        self.dice3.move(0, 560)
        self.dice4 = QLabel(self)
        self.dice4.setPixmap(QPixmap("diceR4.png"))
        self.dice4.resize(80, 80)
        self.dice4.move(0, 560)
        self.dice5 = QLabel(self)
        self.dice5.setPixmap(QPixmap("diceR5.png"))
        self.dice5.resize(80, 80)
        self.dice5.move(0, 560)
        self.dice6 = QLabel(self)
        self.dice6.setPixmap(QPixmap("diceR6.png"))
        self.dice6.resize(80, 80)
        self.dice6.move(0, 560)
        self.dices = [self.dice1, self.dice2, self.dice3, self.dice4, self.dice5, self.dice6]
        self.diceSounds = ["diceRoll1.mp3", "diceRoll2.mp3", "diceRoll4.mp3", ]
        for i in self.dices:
            i.hide()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PlayerTurn = QLabel(self)
        self.PlayerTurn.resize(500, 120)
        self.PlayerTurn.move(0, 470)
        self.PlayerTurn.setFont(font)
        self.PlayerMsg = QLabel(self)
        self.PlayerMsg.resize(400, 60)
        self.PlayerMsg.move(10, 550)
        self.PlayerMsg.setFont(font)
        self.skipTurn = QPushButton("Пропустить ход", self)
        self.skipTurn.resize(110, 30)
        self.skipTurn.move(530, 530)
        self.skipTurn.setEnabled(False)
        self.GoChip1 = QPushButton("Сходить фишкой №1", self)
        self.GoChip1.resize(170, 30)
        self.GoChip1.move(350, 530)
        self.GoChip1.setEnabled(False)
        self.GoChip2 = QPushButton("Сходить фишкой №2", self)
        self.GoChip2.resize(170, 30)
        self.GoChip2.move(350, 565)
        self.GoChip2.setEnabled(False)
        self.GoChip3 = QPushButton("Сходить фишкой №3", self)
        self.GoChip3.resize(170, 30)
        self.GoChip3.move(350, 600)
        self.GoChip3.setEnabled(False)
        self.chipCommands = [self.GoChip1, self.GoChip2, self.GoChip3]
        self.rollTheDice = QPushButton("Бросить кубик", self)
        self.rollTheDice.resize(110, 30)
        self.rollTheDice.move(530, 570)
        self.gameButtons = [self.GoChip1, self.GoChip2, self.GoChip3, self.skipTurn, self.rollTheDice, self.PlayerTurn]
        for i in self.gameButtons:
            i.hide()
        self.load_mp3(self.diceSounds[randint(0, 2)])
        self.exitButton.clicked.connect(self.appExit)
        self.menuButton.clicked.connect(self.inMenu)
        self.startButton.clicked.connect(self.chooseOrContinue)
        self.newGame.clicked.connect(self.gameNew)
        self.rollTheDice.clicked.connect(self.player.play)
        self.rollTheDice.clicked.connect(self.roll)
        self.GoChip1.clicked.connect(self.chipN1)
        self.GoChip1.clicked.connect(self.goChip)
        self.GoChip2.clicked.connect(self.chipN2)
        self.GoChip2.clicked.connect(self.goChip)
        self.GoChip3.clicked.connect(self.chipN3)
        self.GoChip3.clicked.connect(self.goChip)
        self.skipTurn.clicked.connect(self.tskip)
        self.cBtns[0].clicked.connect(self.map1)
        self.cBtns[1].clicked.connect(self.map2)
        self.cBtns[2].clicked.connect(self.map3)
        self.cBtns[3].clicked.connect(self.map4)
        self.readyButton.clicked.connect(self.mapCheck)
        self.trainingButton.clicked.connect(self.rules)

    def rules(self):
        self.HowTo.show()

    def appExit(self):
        sys.exit(app.exec())

    def chooseOrContinue(self):
        self.startButton.hide()
        self.exitButton.hide()
        self.trainingButton.hide()
        self.crowPicture.hide()
        self.welcomlabel.hide()
        self.newGame.show()
        self.menuButton.show()
        self.HowTo.hide()

    def inMenu(self):
        self.startButton.show()
        self.exitButton.show()
        self.trainingButton.show()
        self.crowPicture.show()
        self.newGame.hide()
        self.menuButton.hide()
        self.chooseLabel.hide()
        self.desc.hide()
        self.minimap.hide()
        self.welcomlabel.show()
        self.chooseLabel.setText("      Куда отправимся?")
        for i in self.test:
            i.hide()
        for i in self.cBtns:
            i.hide()
        for i in self.ready:
            i.hide()

    def gameNew(self):
        self.newGame.hide()
        self.continueBtn.hide()
        self.chooseLabel.show()
        self.desc.show()
        self.minimap.show()
        self.miniBtn.show()
        for i in self.test:
            i.show()
        for i in self.cBtns:
            i.show()

    def createGame(self):
        for i in self.ready:
            i.hide()
        self.background2 = QLabel(self)
        self.background2.setPixmap(QPixmap("classicBackground.png"))
        self.background2.resize(800, 500)
        self.background2.move(0, 0)
        self.background2.show()
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(self.mapNames[self.nMap]))
        self.background.resize(800, 500)
        self.background.move(0, 0)
        self.background.show()
        for i in self.gameButtons:
            i.show()
        for elem in result:
            if elem[self.nMap] == "end":
                break
            a = elem[self.nMap].find(":")
            self.mapC.append((int(elem[self.nMap][:a]), int(elem[self.nMap][a + 1:])))
        self.nameInput(self.nicknames[0].text(), "red")
        self.nameInput(self.nicknames[1].text(), "blue")
        self.nameInput(self.nicknames[2].text(), "green")
        self.nameInput(self.nicknames[3].text(), "yellow")
        self.queueOfPlayers.append(self.playerRed)
        self.queueOfPlayers.append(self.playerBlue)
        self.queueOfPlayers.append(self.playerGreen)
        self.queueOfPlayers.append(self.playerYellow)
        self.playersCount = 4
        pointLen = len(self.mapC) // self.playersCount
        startPoint = - pointLen
        for i in range(self.playersCount):
            startPoint += pointLen
            self.queueOfPlayers[i]["endpoint"] = startPoint
        self.turnColor = self.queueOfPlayers[self.turn]["color"]
        self.PlayerTurn.setText("Ход игрока из команды: " + self.turnColor)
        self.cRed1 = QLabel(self)
        self.cRed1.setPixmap(QPixmap("chipR1.png"))
        self.cRed1.resize(50, 40)
        self.cRed1.move(self.mapC[35][0], self.mapC[35][1])
        self.cRed2 = QLabel(self)
        self.cRed2.setPixmap(QPixmap("chipR2.png"))
        self.cRed2.resize(50, 40)
        self.cRed2.move(10, 0)
        self.cRed3 = QLabel(self)
        self.cRed3.setPixmap(QPixmap("chipR3.png"))
        self.cRed3.resize(50, 40)
        self.cRed3.move(20, 0)
        self.cBlue1 = QLabel(self)
        self.cBlue1.setPixmap(QPixmap("chipB1.png"))
        self.cBlue1.resize(50, 40)
        self.cBlue1.move(self.mapC[0][0], self.mapC[0][1])
        self.cBlue2 = QLabel(self)
        self.cBlue2.setPixmap(QPixmap("chipB2.png"))
        self.cBlue2.resize(50, 40)
        self.cBlue2.move(40, 0)
        self.cBlue3 = QLabel(self)
        self.cBlue3.setPixmap(QPixmap("chipB3.png"))
        self.cBlue3.resize(50, 40)
        self.cBlue3.move(50, 0)
        self.cGreen1 = QLabel(self)
        self.cGreen1.setPixmap(QPixmap("chipG1.png"))
        self.cGreen1.resize(50, 40)
        self.cGreen1.move(self.mapC[0][0], self.mapC[0][1])
        self.cGreen2 = QLabel(self)
        self.cGreen2.setPixmap(QPixmap("chipG2.png"))
        self.cGreen2.resize(50, 40)
        self.cGreen2.move(self.mapC[0][0], self.mapC[0][1])
        self.cGreen3 = QLabel(self)
        self.cGreen3.setPixmap(QPixmap("chipG3.png"))
        self.cGreen3.resize(50, 40)
        self.cGreen3.move(self.mapC[0][0], self.mapC[0][1])
        self.cYellow1 = QLabel(self)
        self.cYellow1.setPixmap(QPixmap("chipY1.png"))
        self.cYellow1.resize(50, 40)
        self.cYellow1.move(90, 0)
        self.cYellow2 = QLabel(self)
        self.cYellow2.setPixmap(QPixmap("chipY2.png"))
        self.cYellow2.resize(50, 40)
        self.cYellow2.move(100, 0)
        self.cYellow3 = QLabel(self)
        self.cYellow3.setPixmap(QPixmap("chipY3.png"))
        self.cYellow3.resize(50, 40)
        self.cYellow3.move(110, 0)
        self.cRed1.hide()
        self.cRed2.hide()
        self.cRed3.hide()
        self.cBlue1.hide()
        self.cBlue2.hide()
        self.cBlue3.hide()
        self.cGreen1.hide()
        self.cGreen2.hide()
        self.cGreen3.hide()
        self.cYellow3.hide()
        self.cYellow2.hide()
        self.cYellow1.hide()
        self.win = QLabel(self)
        self.win.setPixmap(QPixmap("winner.png"))
        self.win.resize(800, 500)
        self.win.move(0, 0)
        self.win.hide()
        font1 = QtGui.QFont()
        font1.setPointSize(26)
        self.tWin = QLabel(self)
        self.tWin.setText("")
        self.tWin.setFont(font1)
        self.tWin.resize(600, 100)
        self.tWin.move(200, 200)
        self.tWin.hide()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rp = 0
        self.bp = 0
        self.gp = 0
        self.yp = 0
        self.winner = {"red": self.rp, "blue": self.bp, "green": self.gp, "yellow": self.yp}
        self.chipsVis = {"red": (self.cRed1, self.cRed2, self.cRed3),
                         "blue": (self.cBlue1, self.cBlue2, self.cBlue3),
                         "green": (self.cGreen1, self.cGreen2, self.cGreen3),
                         "yellow": (self.cYellow1, self.cYellow2, self.cYellow3)}
        self.mapLen = len(self.mapC)
        self.mapEntity = [self.ChipR1, self.ChipR2, self.ChipR3,
                          self.ChipB1, self.ChipB2, self.ChipB3,
                          self.ChipG1, self.ChipG2, self.ChipG3,
                          self.ChipY1, self.ChipY2, self.ChipY3]
        self.PlayerTurn.setText(
            "Ход игрока " + self.playersDict[self.turnColor]["name"] + "\nиз команды: " + self.turnColor)

    def map1(self):
        self.nMap = 1
        self.nNames()

    def map2(self):
        self.nMap = 2
        self.nNames()

    def map3(self):
        self.nMap = 3
        self.nNames()

    def map4(self):
        self.nMap = 4
        self.nNames()

    def nNames(self):
        for i in self.test:
            i.hide()
        for i in self.cBtns:
            i.hide()
        self.minimap.hide()
        for i in self.ready:
            i.show()
        self.chooseLabel.setText("Введите имена\n(не более 12 симв.)")

    def mapCheck(self):
        names = ""
        colors = ["Красного, ", "Синего, ", "Зелёного, ", "Жёлтого, "]
        for i in range(4):
            if len(self.nicknames[i].text()) > 12 or len(self.nicknames[i].text()) == 0:
                names += colors[i]
        if names:
            msg = "Некорректные ники у\n" + names[:-2]
            self.chooseLabel.setText(msg)
        else:
            self.createGame()

    def load_mp3(self, filename):
        self.media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def roll(self):
        if self.cubics[0] == 0:
            self.cubics[1] = self.diceRoll() - 1
            self.dices[self.cubics[1]].show()
            self.cubics[0] += 1
        else:
            self.dices[self.cubics[1]].hide()
            self.cubics[1] = self.diceRoll() - 1
            self.dices[self.cubics[1]].show()
        self.GoChip1.setEnabled(True)
        self.GoChip2.setEnabled(True)
        self.GoChip3.setEnabled(True)
        self.rollTheDice.setEnabled(False)
        self.skipTurn.setEnabled(True)

    def goChip(self):
        value = "void"
        notFriend = True
        enP = ""
        if self.DictChips[self.turnColor][self.cNumber - 1]["condition"] == "noActive":
            # Выход на старт
            for i in self.mapEntity:
                if self.playersDict[self.turnColor]["endpoint"] == i["index"]:
                    print(2)
                    if i["color"] == self.turnColor:
                        value = "friend"
                        break
                    elif i["color"] != self.turnColor:
                        value = "enemy"
                        print(enP)
                        break
            if value == "void":
                self.DictChips[self.turnColor][self.cNumber - 1]["condition"] = "active"
                self.DictChips[self.turnColor][self.cNumber - 1]["index"] = self.playersDict[self.turnColor]["endpoint"]
                self.chipsVis[self.turnColor][self.cNumber - 1].move(
                    self.mapC[self.playersDict[self.turnColor]["endpoint"]][0],
                    self.mapC[self.playersDict[self.turnColor]["endpoint"]][1])
                self.chipsVis[self.turnColor][self.cNumber - 1].show()
            if value == "friend":
                notFriend = False
            if value == "enemy":
                self.DictChips[self.turnColor][self.cNumber - 1]["condition"] = "active"
                for i in self.mapEntity:
                    if self.playersDict[self.turnColor]["endpoint"] == i["index"]:
                        i["index"] = -1
                        i["condition"] = "noActive"
                        self.chipsVis[i["color"]][i["tag"]].hide()
                        i["steps"] = 0
                self.DictChips[self.turnColor][self.cNumber - 1]["index"] = self.playersDict[self.turnColor]["endpoint"]
                self.chipsVis[self.turnColor][self.cNumber - 1].move(
                    self.mapC[self.playersDict[self.turnColor]["endpoint"]][0],
                    self.mapC[self.playersDict[self.turnColor]["endpoint"]][1])
                self.chipsVis[self.turnColor][self.cNumber - 1].show()
        elif self.DictChips[self.turnColor][self.cNumber - 1]["condition"] == "finished":
            self.PlayerTurn.setText("Эта фишка уже финишировала")
            notFriend = False
        elif self.DictChips[self.turnColor][self.cNumber - 1]["condition"] == "active":
            # Обычный ход
            if self.DictChips[self.turnColor][self.cNumber - 1]["index"] + self.cubics[1] + 1 >= self.mapLen:
                a = self.cubics[1] + 1 - (self.mapLen - self.DictChips[self.turnColor][self.cNumber - 1]["index"])
                for i in self.mapEntity:
                    if a == i["index"] and self.turnColor != "red":
                        if i["color"] == self.turnColor:
                            value = "friend"
                            break
                        elif i["color"] != self.turnColor:
                            value = "enemy1"
                            break
            else:
                for i in self.mapEntity:
                    if self.DictChips[self.turnColor][self.cNumber - 1]["index"] + self.cubics[1] + 1 == i["index"]:
                        if i["color"] == self.turnColor:
                            value = "friend"
                            break
                        elif i["color"] != self.turnColor:
                            value = "enemy"
                            break
            if value == "void":
                if self.DictChips[self.turnColor][self.cNumber - 1]["index"] + self.cubics[1] + 1 >= self.mapLen:
                    a = self.cubics[1] + 1 - (self.mapLen - self.DictChips[self.turnColor][self.cNumber - 1]["index"])
                    self.DictChips[self.turnColor][self.cNumber - 1]["steps"] += self.cubics[1] + 1
                    self.DictChips[self.turnColor][self.cNumber - 1]["index"] = a
                    self.chipsVis[self.turnColor][self.cNumber - 1].move(
                        self.mapC[self.DictChips[self.turnColor][self.cNumber - 1]["index"]][0],
                        self.mapC[self.DictChips[self.turnColor][self.cNumber - 1]["index"]][1])
                    self.chipsVis[self.turnColor][self.cNumber - 1].show()
                else:
                    self.DictChips[self.turnColor][self.cNumber - 1]["index"] = \
                        self.DictChips[self.turnColor][self.cNumber - 1]["index"] + self.cubics[1] + 1
                    self.DictChips[self.turnColor][self.cNumber - 1]["steps"] += self.cubics[1] + 1
                    self.chipsVis[self.turnColor][self.cNumber - 1].move(
                        self.mapC[self.DictChips[self.turnColor][self.cNumber - 1]["index"]][0],
                        self.mapC[self.DictChips[self.turnColor][self.cNumber - 1]["index"]][1])
                    self.chipsVis[self.turnColor][self.cNumber - 1].show()
                # На пустую клетку
            if value == "friend":
                notFriend = False
            if value == "enemy":
                for i in self.mapEntity:
                    if self.DictChips[self.turnColor][self.cNumber - 1]["index"] + self.cubics[1] + 1 == i["index"]:
                        i["index"] = -1
                        i["condition"] = "noActive"
                        self.chipsVis[i["color"]][i["tag"]].hide()
                        i["steps"] = 0
                self.DictChips[self.turnColor][self.cNumber - 1]["index"] = \
                    self.DictChips[self.turnColor][self.cNumber - 1]["index"] + self.cubics[1] + 1
                self.DictChips[self.turnColor][self.cNumber - 1]["steps"] += self.cubics[1] + 1
                self.chipsVis[self.turnColor][self.cNumber - 1].move(
                    self.mapC[self.DictChips[self.turnColor][self.cNumber - 1]["index"]][0],
                    self.mapC[self.DictChips[self.turnColor][self.cNumber - 1]["index"]][1])
                self.chipsVis[self.turnColor][self.cNumber - 1].show()
            if value == "enemy1":
                a = self.cubics[1] + 1 - (self.mapLen - self.DictChips[self.turnColor][self.cNumber - 1]["index"])
                for i in self.mapEntity:
                    if a == i["index"]:
                        i["index"] = -1
                        i["condition"] = "noActive"
                        self.chipsVis[i["color"]][i["tag"]].hide()
                        i["steps"] = 0
                self.DictChips[self.turnColor][self.cNumber - 1]["index"] = a
                self.DictChips[self.turnColor][self.cNumber - 1]["steps"] += self.cubics[1] + 1
                self.chipsVis[self.turnColor][self.cNumber - 1].move(
                    self.mapC[self.DictChips[self.turnColor][self.cNumber - 1]["index"]][0],
                    self.mapC[self.DictChips[self.turnColor][self.cNumber - 1]["index"]][1])
                self.chipsVis[self.turnColor][self.cNumber - 1].show()
        if notFriend:
            if self.DictChips[self.turnColor][self.cNumber - 1]["steps"] >= self.mapLen:
                self.DictChips[self.turnColor][self.cNumber - 1]["condition"] = "finished"
                self.DictChips[self.turnColor][self.cNumber - 1]["index"] = -1
                self.chipsVis[self.turnColor][self.cNumber - 1].hide()
                self.winner[self.turnColor] += 1
            if self.winner[self.turnColor] == 3:
                self.GoChip1.setEnabled(False)
                self.GoChip2.setEnabled(False)
                self.GoChip3.setEnabled(False)
                self.rollTheDice.setEnabled(False)
                self.skipTurn.setEnabled(False)
                self.tWin.setText("Побеждает игрок\n" + self.playersDict[self.turnColor]["name"])
                self.win.show()
                self.tWin.show()
            for i in self.chipCommands:
                i.setEnabled(False)
            if self.winner[self.turnColor] != 3:
                self.rollTheDice.setEnabled(True)
            self.skipTurn.setEnabled(False)
            self.turn += 1
            if self.turn == 4:
                self.turn = 0
            self.turnColor = self.queueOfPlayers[self.turn]["color"]
            self.PlayerTurn.setText(
                "Ход игрока " + self.playersDict[self.turnColor]["name"] + "\nиз команды: " + self.turnColor)
        else:
            self.PlayerTurn.setText("Вы не можете сходить\nэтой фишкой")

    def tskip(self):
        for i in self.chipCommands:
            i.setEnabled(False)
        self.rollTheDice.setEnabled(True)
        self.skipTurn.setEnabled(False)
        self.turn += 1
        if self.turn == 4:
            self.turn = 0
        self.turnColor = self.queueOfPlayers[self.turn]["color"]
        self.PlayerTurn.setText(
            "Ход игрока " + self.playersDict[self.turnColor]["name"] + "\nиз команды: " + self.turnColor)

    def chipN1(self):
        self.cNumber = 1

    def chipN2(self):
        self.cNumber = 2

    def chipN3(self):
        self.cNumber = 3


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CrowGame()
    ex.show()
    sys.exit(app.exec())

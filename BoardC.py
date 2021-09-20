#The Board

from PyQt5.QtGui import QMouseEvent, QPaintEvent, QPainter, QPixmap, QColor, QPen
from PyQt5.QtCore import QPointF, QRectF, QSize, QUrl, Qt, QCoreApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import random as Random
import Core
import time as Time

class Board(QWidget):
    def __init__(self, parent):
        """ The class of the widget board """
        super().__init__(parent=parent)
        self.parent = parent
        self.size_ = QSize(200, 200)
        self.board = QPixmap(self.size_)
        self.down_pos = (-1, -1)
        self.up_pos = (-1, -1)
        self.score = 0
        self.plus_score = 10
        self.is_merge = False
        self.painter = QPainter()
        self.pop = QMediaContent(QUrl("qrc:/wav/Pop.wav"))
        self.pop_player = QMediaPlayer()
        self.pop_player.setMedia(self.pop)
        self.blip = QMediaContent(QUrl("qrc:/wav/Blip.wav"))
        self.blip_player = QMediaPlayer()
        self.blip_player.setMedia(self.blip)
        self.board_list = [
        0, 0, 0, 0, 
        0, 0, 0, 0, 
        0, 0, 0, 0, 
        0, 0, 0, 0
        ]
        index1 = Random.randint(0, 15)
        self.board_list[index1] = 2
        index2 = Random.randint(0, 15)
        while index1 == index2:
            index2 = Random.randint(0, 15)
        self.board_list[index2] = 2
        self.draw_board()
        Time.sleep(1)

    def retry(self):
        """ Clear the board and restart """
        self.board_list = [
        0, 0, 0, 0, 
        0, 0, 0, 0, 
        0, 0, 0, 0, 
        0, 0, 0, 0
        ]
        index1 = Random.randint(0, 15)
        self.board_list[index1] = 2
        index2 = Random.randint(0, 15)
        while index1 == index2:
            index2 = Random.randint(0, 15)
        self.board_list[index2] = 2
        self.score = 0
        self.plus_score = 10
        self.draw_board()
        self.parent.Score.setText(QCoreApplication.translate("MainWindow", "SCORE:" + str(self.score)))
    
    def draw_board(self):
        """ Draw the board to a picture """
        self.board.fill(Qt.gray)
        self.painter.begin(self.board)
        self.painter.setPen(QPen(QColor(0, 0, 0)))
        self.painter.drawLine(0, 50, 200, 50)
        self.painter.drawLine(0, 100, 200, 100)
        self.painter.drawLine(0, 150, 200, 150)
        self.painter.drawLine(50, 0, 50, 200)
        self.painter.drawLine(100, 0, 100, 200)
        self.painter.drawLine(150, 0, 150, 200)
        def rect(x, y, num):
            color = QColor(Qt.gray)
            if num == 2:
                color = QColor(255, 0, 0)
            elif num == 4:
                color = QColor(0, 255, 0)
            elif num == 8:
                color = QColor(153, 37, 114)
            elif num == 16:
                color = QColor(255, 255, 0)
            elif num == 32:
                color = QColor(221, 121, 7)
            elif num == 64:
                color = QColor(156, 107, 48)
            elif num == 128:
                color = QColor(138,90,131)
            elif num == 256:
                color = QColor(160, 33, 40)
            elif num == 512:
                color = QColor(100, 100, 100)
            elif num == 1024:
                color = QColor(74 ,32, 59)
            elif num == 2048:
                color = QColor(255, 255, 255)
            self.painter.setPen(QPen(color))
            self.painter.drawRect(x, y, 47, 47)
            self.painter.setPen(QPen(color, 10))
            self.painter.drawText(QPointF(x + 23, y + 23), str(num))
        for col in range(4):
            for row in range(4):
                index = (row) * 4 + col
                x = col * 53 - 1
                y = row * 53 - 1
                num = self.board_list[index]
                rect(x, y, num)
        self.painter.end()
        self.update()

    def add_2(self):
        """ Add 2 or 4 to the board """
        while True:
            index = Random.randint(0, 15)
            num = Random.choice([2, 2, 2, 2, 4])
            if self.board_list[index] == 0:
                self.board_list[index] = num
                self.draw_board()
                break

    def check_board(self):
        """ Check the board """
        if Core.is_2048(self.board_list) == True:
            self.painter.begin(self.board)
            self.painter.setPen(QPen(QColor(0, 255, 0)))
            self.painter.drawLine(0, 100, 100, 200)
            self.painter.drawLine(100, 200, 200, 0)
            self.painter.end()
            self.score += 1000
            score_txt = "SCORE:" + str(self.score)
            self.parent.Score.setText(QCoreApplication.translate("MainWindow", score_txt))
            self.update()
        else:
            if Core.can_move(self.board_list) == False:
                self.painter.begin(self.board)
                self.painter.setPen(QPen(QColor(255, 0, 0)))
                self.painter.drawLine(0, 0, 200, 200)
                self.painter.drawLine(0, 200, 200, 0)
                self.painter.end()
                self.update()
                self.blip_player.play()

    def move(self, mode):
        """ Move the board and update """
        answer = Core.move(self.board_list, mode)
        self.board_list = answer[0]
        self.draw_board()
        self.is_merge = answer[1]
        if self.is_merge:
            self.plus_score += 10
        else:
            self.plus_score = 0
        self.score += self.plus_score
        score_txt = "SCORE:" + str(self.score)
        self.parent.Score.setText(QCoreApplication.translate("MainWindow", score_txt))

    
    def paintEvent(self, paintEvent:QPaintEvent):
        """ On paint """
        self.painter.begin(self)
        self.painter.drawPixmap(0, 0, self.board)
        self.painter.end()

    def mousePressEvent(self, mouseEvent:QMouseEvent):
        """ On mouse down"""
        x = mouseEvent.pos().x()
        y = mouseEvent.pos().y()
        self.down_pos = [x, y]


    def mouseReleaseEvent(self, mouseEvent:QMouseEvent):
        """ On mouse up """
        x = mouseEvent.pos().x()
        y = mouseEvent.pos().y()
        self.up_pos = [x, y]
        if self.down_pos != (-1, -1) and self.up_pos != (-1, -1) and Core.can_move(self.board_list) == True and Core.is_2048(self.board_list) == False:
            x_change = self.up_pos[0] - self.down_pos[0]
            y_change = self.up_pos[1] - self.down_pos[1]
            abs_x = abs(x_change)
            abs_y = abs(y_change)
            if abs_x + abs_y > 50:
                self.pop_player.play()
                if abs_x > abs_y:
                    if x_change > 0:
                        self.move(Core.RIGHT)
                    else:
                        self.move(Core.LEFT)
                    self.add_2()
                    self.check_board()
                else:
                    if y_change > 0:
                        self.move(Core.DOWN)
                    else:
                        self.move(Core.UP)
                    self.add_2()
                    self.check_board()

import Sounds_rc

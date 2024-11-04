import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QSizeGrip, QFileDialog, QMessageBox
from interface import Ui_Form
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QPixmap
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import sqlite3


class Book_reader(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("BOOKZ.db")
        self.cur = self.con.cursor()
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setWindowTitle('BOOKZ')

        QSizeGrip(self.size_grip)

        self.tool_frame.mouseMoveEvent = self.move_window
        self.tool_frame.mousePressEvent = self.lkm_press

        self.roll_up_but.clicked.connect(lambda: self.showMinimized())
        self.close_but.clicked.connect(lambda: self.close())

        self.size_but.clicked.connect(lambda: self.restore_or_maximize_window())

        self.add_but.clicked.connect(lambda: self.add_book())

        self.remove_but.clicked.connect(lambda: self.remove_book())

        self.listclose_but.clicked.connect(lambda: self.slideLeftMenu())

        self.page_number_but.clicked.connect(lambda: self.page_number_find())

        self.fav_but.clicked.connect(self.favourite_book)

        self.spisok_knig.itemClicked.connect(lambda: self.load_book_to_show())

        self.pages = []
        self.books = []
        self.count_pages = 0
        self.page_num = 1
        self.flag = False
        self.count_books = 0

        for i in self.cur.execute("""SELECT book_name FROM Books""").fetchall():
            self.count_books += 1

        if self.cur.execute("""SELECT book_name FROM Books WHERE favourite = ?""", (1, )).fetchone():
            self.book_name = self.cur.execute("""SELECT book_name FROM Books WHERE favourite = ?""", (1, )).fetchone()
            self.book_name = self.book_name[0]
        else:
            self.book_name = ''
            self.flag = True

        self.rightslide.clicked.connect(lambda: self.next_page())

        self.leftslide.clicked.connect(lambda: self.prev_page())

        books_cort = self.cur.execute("""SELECT book_name FROM Books""").fetchall()

        for i in books_cort:
            self.books.append(i[0])

        for i in self.books:
            self.spisok_knig.addItem(i)

        if self.cur.execute("""SELECT book_name FROM Books WHERE favourite =?""", (1, )).fetchall():
            self.load_book_to_show()
            self.flag = True

    def slideLeftMenu(self):
        width = self.leaf_frame_container.width()
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.leaf_frame_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InBack)
        self.animation.start()

    def move_window(self, event):
        if event.buttons() == Qt.LeftButton:
            if not self.isMaximized() and self.clicked_position:
                self.move(self.pos() + event.globalPos() - self.clicked_position)
                self.clicked_position = event.globalPos()

    def lkm_press(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked_position = event.globalPos()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def add_book(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать книгу', '', 'Файл (*.pdf)')[0]
        book_name = fname.split('/')[-1][:-4]
        if book_name in self.books:
            temp = QMessageBox()
            temp.information(self, 'Ты че дурак?', "<p style='color: white;'> Вы уже добавляли эту книгу </p>")
        else:
            self.cur.execute(""" INSERT INTO Books(book, fav_page, book_name, favourite)
            VALUES(?, ?, ?, ?)""", (fname, 1, book_name, 0))
            self.con.commit()
            self.spisok_knig.addItem(book_name)
            self.books.append(book_name)
            self.count_books += 1
            self.flag = False
            print(self.book_name)
            self.book_name = book_name
            print(self.book_name)
            self.load_book_to_show()

    def remove_book(self):
        book_name = self.spisok_knig.selectedItems()
        if not book_name: return
        for i in book_name:
            temp = self.spisok_knig.takeItem(self.spisok_knig.row(i)).text()
            self.cur.execute(""" DELETE from Books WHERE book_name = ?""", (temp, ))
            self.con.commit()
            self.books.remove(temp)
            self.page_number_LineEdit.setText('')
            self.count_books -= 1
            if self.count_books:
                self.load_book_to_show()
            else:
                self.page_pixmap.clear()


    def load_book_to_show(self):
        if self.flag:
            self.book_name = self.spisok_knig.currentItem().text()
        file_path = self.cur.execute(""" SELECT book FROM Books
        WHERE book_name = ?""", (self.book_name, )).fetchone()
        pdf_file = open(file_path[0], "rb")
        pdf_file = PdfFileReader(pdf_file)
        self.count_pages = pdf_file.getNumPages()
        self.pages = convert_from_path(file_path[0], self.count_pages, poppler_path = r"C:\Users\artem\Documents\poppler-22.04.0\Library\bin")
        self.page_num = self.cur.execute("""SELECT fav_page FROM Books
        WHERE book_name = ?""", (self.book_name, )).fetchone()[0]
        self.page_number_LineEdit.setText(str(self.page_num))
        self.show_page(self.page_num)


    def show_page(self, page_num):
        page = self.pages[page_num - 1]
        page.save('page.jpg', 'JPEG')
        pix = QPixmap('page.jpg')
        self.page_pixmap.setPixmap(pix)

    def next_page(self):
        if self.page_num < self.count_pages:
            self.page_num += 1
            self.show_page(self.page_num)
            self.cur.execute("""UPDATE Books
            SET fav_page = ?
            WHERE book_name = ?""", (self.page_num, self.book_name))
            self.page_number_LineEdit.setText(str(self.page_num))
            self.con.commit()

    def prev_page(self):
        if self.page_num > 1:
            self.page_num -= 1
            self.show_page(self.page_num)
            self.cur.execute("""UPDATE Books
            SET fav_page = ?
            WHERE book_name = ?""", (self.page_num, self.book_name))
            self.page_number_LineEdit.setText(str(self.page_num))
            self.con.commit()

    def page_number_find(self):
        if self.count_pages >= int(self.page_number_LineEdit.text()):
            self.page_num = abs(int(self.page_number_LineEdit.text()))
            self.show_page(int(self.page_number_LineEdit.text()))

    def favourite_book(self):
        self.cur.execute("""UPDATE Books
        SET favourite = ?
        WHERE favourite = ?""", (0, 1))
        self.cur.execute("""UPDATE Books
        SET favourite = ?
        WHERE book_name LIKE ?""", (1, self.book_name))
        self.con.commit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.prev_page()
        if event.key() == Qt.Key_D:
            self.next_page()

def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Book_reader()
    ex.show()
    sys.__excepthook__ = except_hook
    sys.exit(app.exec_())

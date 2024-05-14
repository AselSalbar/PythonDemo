# программа в стиле GUI
import tkinter as gui
from const import *

# создать главное окно программы
win = gui.Tk()

#создать размеры окна
win.geometry(INIT_WIN_SIZE )

#задать заголовок
win.title(MAIN_TITLE )

#запустить окно (программу)
win.mainloop()
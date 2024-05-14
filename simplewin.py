# программа в стиле GUI
import tkinter as gui
from const import *

# создать главное окно программы
win = gui.Tk()

#создать размеры окна
win.geometry(INIT_WIN_SIZE)

#задать заголовок
win.title(MAIN_TITLE)

# создать систему меню
# 1. Создаётся главный объект меню.
# 2. Создаётся группа - она соответствует пункту первого уровня,
#    который раскрывает группу подпунктов.
# 3. В подгруппе создаётся столько пунктов, сколько требуется.
# 4. Затем вся группа подключается к главному объекту меню.
# 5. В случае, если есть другие группы, шаги со 2-го по 4-й
# повторяются для каждой группы.
# 6. В финале главный обёект меню подключается к главному окну программы.
main_menu = gui.Menu(win)
# создать первую группу
file_item = gui.Menu(main_menu)

# пункты первой группы меню
file_item.add_command(label=FILE_NEW)
file_item.add_command(label=FILE_OPEN)
file_item.add_command(label=FILE_SAVE)
# разделитель
file_item.add_separator()
file_item.add_command(label=FILE_EXIT)
# подключить группу к главному меню
main_menu.add_cascade(label=MAIN_ITEM_FILE, menu=file_item)
# подключить меню к окну
win.config(menu=main_menu)

# запустить окно (программу)
win.mainloop()


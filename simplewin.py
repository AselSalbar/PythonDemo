# программа в стиле GUI
import tkinter as gui
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from const import *
import os

def exit_clik():
    # обработчик выбора пункта выход
    win.quit()

def new_click():
    # обработчик выбора пункта Новый
    editor.delete(1.0, gui.END)
def open_click():
    # обработчик выбора пункта Открыть
    file = filedialog.askopenfile(filetypes=(('Python файл','.py'),
                                                ('Текстовый файл', '.html'),
                                                 ('ПДФ файл', '.pdf')))
    # в заголовке имя файла
    win.title(os.path.basename(file.name))
    # очистить редактор
    new_click()
    # загрузить текст из файла в редактор
    editor.insert(gui.END, file.read())


def save_click():
    # обработчик выбора пункта Сохранить
    filedialog.asksaveasfilename()

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
file_item.add_command(label=FILE_NEW, command=new_click)
file_item.add_command(label=FILE_OPEN, command=open_click)
file_item.add_command(label=FILE_SAVE, command=save_click)
# разделитель
file_item.add_separator()
file_item.add_command(label=FILE_EXIT, command=exit_clik)
# подключить группу к главному меню
main_menu.add_cascade(label=MAIN_ITEM_FILE, menu=file_item)
# подключить меню к окну
win.config(menu=main_menu)

# разместить в окне редактор текста
editor = scrolledtext.ScrolledText(win, font=FONT_SIZE, wrap=gui.WORD)
editor.pack(expand=True, fill=gui.BOTH)

# запустить окно (программу)
win.mainloop()


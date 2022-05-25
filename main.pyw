from tkinter import *

import os
import winreg


def launch_panzer(value: str, type: int) -> None:
    '''


    :param value:
    :param type:
    :return:
    '''
    save_registry(value, type)

    os.startfile('steam://rungameid/268400')

    root.destroy()


def read_registry() -> tuple:
    '''
    Get value to registry

    :return:
    '''
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Slitherine\Panzer Corps') as key:
        return winreg.QueryValueEx(key, 'ActiveExpansion')


def save_registry(value: str, type: int) -> None:
    '''
    Save value to registry

    :param value:
    :param type:
    :return:
    '''

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Slitherine\Panzer Corps', 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, 'ActiveExpansion', 0, type, value)


def get_key(options_dict: dict, search_value: str) -> str:
    '''
    Search dictionary key to value

    :param options_dict:
    :param search_value:
    :return:
    '''
    for key, value in options_dict.items():
        if value == search_value:
            return key


if __name__ == '__main__':

    reg_value, reg_type = read_registry()
    # print(reg_value)

    save_registry('pc', reg_type)

    options = {'Panzer corps': 'pc',
               'Allied corps': 'ac',
               'Afrika korps': 'ak',
               'Soviet corps': 'sc'}

    root = Tk()

    root.title('Panzer Corps')

    root.geometry('200x100')

    clicked = StringVar()

    clicked.set(get_key(options, reg_value))

    drop = OptionMenu(root, clicked, *options.keys())
    drop.pack()

    launch_button = Button(root, text='Launch Panzer Corps', command=lambda: launch_panzer(options.get(clicked.get()),
                                                                                         reg_type))
    launch_button.pack()

    root.mainloop()

import os
import re
import ascii_arts
import colorama
from code_window import run_code_window


# comands here
def show_comands():
    print(*swich_dict.keys())


def green():
    print(colorama.Fore.GREEN)


def red():
    print(colorama.Fore.RED)


def color_reset():
    print(colorama.Fore.RED)


def do_quit():
    print(f'{colorama.Fore.RED}press control + c to close!{colorama.Fore.RESET}')
    exit()


swich_dict = {
    '.code': run_code_window,
    '.quit':  do_quit,
    '.plane': ascii_arts.plane,
    '.world': ascii_arts.world,
    '.tower': ascii_arts.tower,
    '.smoke': ascii_arts.no_smoke,
    '.comands': show_comands,
    '.green': green,
    '.red': red,
    '.color-reset': color_reset,
}


def _is_comand(string: str):
    return True if re.fullmatch(r'[.]\w*', string) else False


def string_comand(string: str) -> str:
    if _is_comand(string):
        return swich_dict.get(string, string)()  # aways must be a funcition
    else:
        return string


if '__main__' == __name__:
    # simulates msgs on console
    while True:
        msg = string_comand(input('__________________\n'))
        print(msg)


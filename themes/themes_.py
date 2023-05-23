import PySimpleGUI as sg
from .theme_store import *

def init_themes():
    theme_list = [theme for theme in theme_dicts]
    for theme in theme_list:
        sg.theme_add_new(theme["NAME"], theme)
import PySimpleGUI as sg
from .theme_store import *
import toml
import sys, os

lin_dar = ["linux", "darwin"]

win = ["win32", "cygwin"]

if sys.platform in lin_dar:
    slash = "/"
elif sys.platform in win:
    slash = "\\"

config = toml.load(f"{os.getcwd()}{slash}config.toml")

def init_themes():
    theme_list = [theme for theme in theme_dicts]
    for theme in theme_list:
        sg.theme_add_new(theme["NAME"], theme)
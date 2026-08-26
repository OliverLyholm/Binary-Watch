import tkinter as tk
from datetime import datetime
from functions.functions import updateClock
from .menu import createMenu


def createWindow():
    window = tk.Tk()
    window.title("Digital Watch")
    window.geometry("450x150")

    timezone = tk.StringVar(value="Europe/Copenhagen")

    clock = tk.Label(window, font=("Arial", 40), text="Test")
    clock.pack()

    timezoneLabel = tk.Label(window, font=("Arial", 20))
    timezoneLabel.pack()

    createMenu(window, timezone)

    updateClock(window, clock, timezoneLabel, timezone)

    return window

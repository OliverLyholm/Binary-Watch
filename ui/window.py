import tkinter as tk
from datetime import datetime
from functions.functions import updateClock
from .menu import createMenu


def createWindow():
    """Creates the main window

    Returns:
        tk.tk: Main window to show clock on
    """
    window = tk.Tk()
    window.title("Binary Watch")
    window.geometry("400x400")

    timezone = tk.StringVar(value="Europe/Copenhagen")

    clock = tk.Canvas(window, width=320, height=300, bg="black")
    clock.pack(pady=10)

    timezoneLabel = tk.Label(window, font=("Arial", 28))
    timezoneLabel.pack()

    createMenu(window, timezone)

    updateClock(window, clock, timezoneLabel, timezone)

    return window
